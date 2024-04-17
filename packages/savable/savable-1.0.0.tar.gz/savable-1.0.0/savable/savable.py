import pickle
import shutil
from pathlib import Path
from typing import List, Union
import json
import inspect
from copy import deepcopy
import logging

__version__ = '1.0.0'
__author__ = 'Giacomo Tanzi'
__doc__ = '''A Python utility for making child classes savable, 
providing methods to save and load objects using various formats such as pickle, zip, dict, and json.'''

logger = logging.getLogger(__name__)


class NotSimplySerializable(TypeError):
    pass


class MissingMandatoryArgument(KeyError):
    pass


def _is_pickable(obj):
    try:
        s = pickle.dumps(obj)
        pickle.loads(s)
        return True
    except pickle.PicklingError:
        return False


def _bind_signature_dict(obj_class, d):
    """
    Bind a dictionary to an object's __init__ signature.

    Parameters:
    -----------
    obj_class : class
        The class whose __init__ signature will be used for binding.
    d : dict
        The dictionary containing values to bind to the signature parameters.

    Returns:
    --------
    signature : inspect.BoundArguments
        A bound signature object with parameters bound to values from the dictionary.
    """

    # Get the signature of the class's __init__ method
    obj_init_signature = inspect.signature(obj_class)
    bind_args = []
    bind_kwargs = {}

    for k, parameter in obj_init_signature.parameters.items():
        # VAR_POSITIONAL and VAR_KEYWORD parameters are ignored

        not_var_parameter = parameter.kind in [inspect.Parameter.POSITIONAL_ONLY,
                                               inspect.Parameter.POSITIONAL_OR_KEYWORD,
                                               inspect.Parameter.KEYWORD_ONLY]

        has_default = parameter.default != inspect.Parameter.empty

        if not_var_parameter and not has_default:
            # Determine mandatory arguments and args with default values
            if k not in d:
                raise MissingMandatoryArgument(f'Signature of class "{obj_class}" can not be resolved since '
                                               f'its missing the required argument "{k}"')

            if parameter.kind == inspect.Parameter.POSITIONAL_ONLY:
                bind_args.append(d[k])
            else:
                bind_kwargs[k] = d[k]

        elif not_var_parameter and has_default:
            # KEYWORD parameters with default are not mandatory but are used if present
            if k in d:
                bind_kwargs[k] = d[k]

    # Bind positional and keyword arguments found in the dictionary
    bind_signature = obj_init_signature.bind(*bind_args, **bind_kwargs)
    # Apply defaults
    bind_signature.apply_defaults()
    return bind_signature


def _make_path(path: Union[str, Path], suffix: Union[str, List[str]]) -> Path:
    """
    This function checks if a path is valid and has the correct extension.
    """
    path = Path(path)
    suffix = [suffix] if isinstance(suffix, str) else suffix + ['']
    if any(char in str(path.name) for char in ':*<>?"|'):
        raise ValueError('Special characters are not allowed in file names')
    if path.suffix not in suffix:
        raise ValueError(f'Extension "{path.suffix}" not valid. Did you mean "{suffix[0]}"? ')
    return path.with_suffix(suffix[0])


class Savable:
    """
    Make child classes savable, providing methods to save and load objects using various formats such as pickle, zip,
     dict and json.
    To handle dict/json serialization, the class uses the __dict__ attribute of the object, which is checked against
    the __init__ signature of the class to ensure that the object can be recreated from the dictionary.

    It also provides a mechanism to exclude certain attributes from being saved. This is useful when an attribute is
    not serializable or when it's not needed to be saved (e.g. a logger object, lambda functions, temporary data, ...).

    Attributes:
    ----------
    exclude_from_saving : list of str, optional
        List of attributes or attribute names to be excluded from saving.
        These attributes will be set to None when loading back.
    """

    def __init__(self, exclude_from_saving: List[str] = None, **kwargs):
        if exclude_from_saving is not None and len(exclude_from_saving) > 0:
            self._exclude_from_saving = exclude_from_saving
        super().__init__(**kwargs)

    def to_pickle(self, path: Union[str, Path]):
        if not _is_pickable(self):
            logger.warning('This object is not pickable! You may have problems loading it back.')

        path_as_pkl = _make_path(path, suffix=['.pkl', '.pickle'])
        with open(path_as_pkl, 'wb') as f:
            pickle.dump(self, f)
        logger.debug(f'{self} saved to "{path_as_pkl}"')

    def to_zip(self, path: Union[str, Path]):
        path_as_zip = _make_path(path, suffix='.zip')
        base_folder = path_as_zip.parent
        file_name = path_as_zip.stem
        tmp_folder = base_folder / f"{file_name}_tmp"
        tmp_folder.mkdir(parents=True, exist_ok=True)

        try:
            tmp_pickle = tmp_folder / f"{file_name}.pkl"
            self.to_pickle(tmp_pickle)
            shutil.make_archive(path_as_zip.with_suffix(''), 'zip', tmp_folder)
            logger.debug(f'{self} saved to "{path_as_zip}"')
        finally:
            shutil.rmtree(tmp_folder)

    def to_dict(self) -> dict:
        out = self.__getstate__()
        try:
            _bind_signature_dict(self.__class__, out)
        except MissingMandatoryArgument as e:
            logger.warning(f'This object is not simply serializable,'
                           f' since its __dict__ can not be bound to its __init__ signature ({e}).'
                           f'\nConsider implementing a custom "to_dict" method.')

        return out

    @classmethod
    def from_dict(cls, d: dict, force=False):
        d = deepcopy(d)  # avoid modifying original dict
        try:
            bind_signature = _bind_signature_dict(cls, d)
            out = cls(*bind_signature.args, **bind_signature.kwargs)  # create object with signature
        except MissingMandatoryArgument as e:
            # check if class name is in dict to avoid creating a new object with a random dictionary
            if force:
                logger.warning(f'This object was created despite not being simply serializable'
                               f' {e}'
                               f'\nConsider implementing a custom "from_dict" method.')
                out = cls.__new__(cls)  # create object without calling __init__

            else:
                raise NotSimplySerializable(f'A new object of class {cls} can not be created from the given dictionary.'
                                            '\nYou must implement a custom "from_dict" method or '
                                            'provide another dictionary.') from e

        # override attributes with values taken from dict
        for k, v in d.items():
            setattr(out, k, v)
        return out

    def to_json(self, path: Union[str, Path]):
        path_as_json = _make_path(path, suffix=['.json', '.cfg'])
        with open(path_as_json, 'w') as f:
            json.dump(self.to_dict(), f, indent=4, sort_keys=True)
        logger.debug(f'{self} saved to "{path_as_json}"')

    def save(self, path: Union[str, Path]):
        if Path(path).suffix == '.zip':
            self.to_zip(path)
        elif Path(path).suffix in ['.json', '.cfg']:
            self.to_json(path)
        else:
            self.to_pickle(path)

    @classmethod
    def from_pickle(cls, path: Union[str, Path]):
        path_as_pkl = _make_path(path, suffix=['.pkl', '.pickle'])
        with open(path_as_pkl, 'rb') as f:
            return pickle.load(f)

    @classmethod
    def from_json(cls, path: Union[str, Path], force=False):
        path_as_json = _make_path(path, suffix=['.json', '.cfg'])
        with open(path_as_json, 'r') as f:
            _dict = json.load(f)
            return cls.from_dict(_dict, force=force)

    @classmethod
    def from_zip(cls, path: Union[str, Path]):
        path_as_zip = _make_path(path, suffix='.zip')
        base_folder = path_as_zip.parent
        file_name = path_as_zip.stem
        tmp_folder = base_folder / f"{file_name}_tmp"
        tmp_pickle = tmp_folder / f"{file_name}.pkl"
        try:
            shutil.unpack_archive(path_as_zip, tmp_folder, 'zip')
            return cls.from_pickle(tmp_pickle)
        finally:
            shutil.rmtree(tmp_folder)

    @classmethod
    def load(cls, path: Union[str, Path, dict]):
        if isinstance(path, dict):
            return cls.from_dict(path)
        elif Path(path).suffix == '.zip':
            return cls.from_zip(path)
        elif Path(path).suffix in ['.json', '.cfg']:
            return cls.from_json(path)
        else:
            return cls.from_pickle(path)

    def __getstate__(self):
        state = self.__dict__.copy()
        exclusion_list = getattr(self, "_exclude_from_saving", [])
        for k, v in state.items():
            if (k in exclusion_list) or (v in exclusion_list):
                # Exclude attribute value from being saved
                state[k] = None
                continue

        return state

    def __setstate__(self, state):
        self.__dict__.update(state)

#
