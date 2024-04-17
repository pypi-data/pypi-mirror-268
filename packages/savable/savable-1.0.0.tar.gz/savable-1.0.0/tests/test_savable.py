import unittest
from tempfile import TemporaryDirectory
from pathlib import Path
import os
from context import Savable, NotSimplySerializable, _make_path, _bind_signature_dict, MissingMandatoryArgument


class MyObject(Savable):
    def __init__(self, a, b, c=None):
        self.a = a
        self.b = b
        self.c = c if c is not None else {}


class TestSavable(unittest.TestCase):
    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        self.test_data = {'a': 1, 'b': [1, 2, 3], 'c': {'x': 'y'}}
        self.test_obj = MyObject(**self.test_data)
        self.test_pickle_path = os.path.join(self.temp_dir.name, 'test.pkl')
        self.test_zip_path = os.path.join(self.temp_dir.name, 'test.zip')
        self.test_json_path = os.path.join(self.temp_dir.name, 'test.json')

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_to_pickle(self):
        self.test_obj.to_pickle(self.test_pickle_path)
        self.assertTrue(os.path.exists(self.test_pickle_path))

    def test_to_zip(self):
        self.test_obj.to_zip(self.test_zip_path)
        self.assertTrue(os.path.exists(self.test_zip_path))

    def test_to_json(self):
        self.test_obj.to_json(self.test_json_path)
        self.assertTrue(os.path.exists(self.test_json_path))

    def test_load_pickle(self):
        self.test_obj.to_pickle(self.test_pickle_path)
        loaded_obj = MyObject.from_pickle(self.test_pickle_path)
        self.assertEqual(self.test_obj.__dict__, loaded_obj.__dict__)

    def test_load_json(self):
        self.test_obj.to_json(self.test_json_path)
        loaded_obj = MyObject.from_json(self.test_json_path)
        self.assertEqual(self.test_obj.__dict__, loaded_obj.__dict__)

    def test_load_zip(self):
        self.test_obj.to_zip(self.test_zip_path)
        loaded_obj = MyObject.from_zip(self.test_zip_path)
        self.assertEqual(self.test_obj.__dict__, loaded_obj.__dict__)

    def test__make_path(self):
        # Test valid path
        valid_path = os.path.join(self.temp_dir.name, 'test.pkl')
        checked_path = _make_path(valid_path, '.pkl')
        self.assertEqual(Path(valid_path), checked_path)

        # Test invalid path
        invalid_path = os.path.join(self.temp_dir.name, 'invalid:path.pkl')
        with self.assertRaises(ValueError):
            _make_path(invalid_path, '.pkl')

    def test_exclude_from_saving(self):
        class MyObjectWithExclusion(Savable):
            def __init__(self, a, b, c=None):
                self.a = a
                self.b = b
                self.c = c if c is not None else {}
                self.not_serializable_method = lambda x:x + 1
                super().__init__(exclude_from_saving=['not_serializable_method'])

        test_obj = MyObjectWithExclusion(**self.test_data)
        test_obj_dict = test_obj.to_dict()
        self.assertIsNone(test_obj_dict.get('not_serializable_method'))

        new_obj = MyObjectWithExclusion.from_dict(test_obj_dict)
        self.assertIsNone(getattr(new_obj, 'long_list', None))

    def test_to_dict(self):
        self.assertEqual(self.test_obj.__dict__,
                         MyObject.from_dict(self.test_obj.to_dict()).__dict__)

    def test_not_serializable(self):
        class NotSerializableClass(Savable):
            def __init__(self, a, b, c=3):
                self.a = a + b + c

        not_serializable_obj = NotSerializableClass(1, 2)

        with self.assertRaises(MissingMandatoryArgument):
            _bind_signature_dict(NotSerializableClass, dict(a=12))

        with self.assertLogs(level='WARNING'):
            bad_dict = not_serializable_obj.to_dict()

        with self.assertLogs(level='WARNING'):
            NotSerializableClass.from_dict(bad_dict,force=True)

        with self.assertRaises(NotSimplySerializable):
            random_dict = dict(b=2)
            NotSerializableClass.from_dict(random_dict)


if __name__ == '__main__':
    unittest.main()
