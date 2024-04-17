
# Savable

**Savable** is a Python utility for making child classes savable, 
providing methods to save and load objects using various formats 
such as pickle, zip, dict, and json. 
It also offers a mechanism to exclude certain attributes from being saved, 
useful for non-serializable class attributes or those not needed to be saved.

## Installation

The package can be installed via pip:

```bash
pip install savable
```

## Usage

### Basic Usage

```python
from savable import Savable

class MyClass(Savable):
    def __init__(self, name):
        self.name = name
        self.surname = 'none'
        

obj = MyClass("example")
obj.surname = 'example_surname' # change instance attribute after initialization
obj.save("example.pkl")  # Save object to pickle file
obj.to_dict()  # Output: {"name": "example","surname":"example_surname"}
obj.to_json("example.json")  # Save object to JSON file
obj.to_zip("example.zip")  # Save object to zip file
```

### Usage with dataclasses

```python
from savable import Savable
from dataclasses import dataclass

@dataclass
class MyActor(Savable):
    name:str 
    surname:str
    kind:str = 'human'    

 
obj = MyActor(name='jack',surname='black') 
obj.to_dict()  # Output: {"name": "jack","surname":"black","kind":"human"}
MyActor.from_dict(obj.to_dict()) # Output: MyActor(name='jack', surname='black', kind='human')
```

### Loading from File
The class will inference the file format from the extension.
Supported extensions are: 
1) from_pickle (.pkl,.pickle) 
2) from_zip (.zip)
3) from_json (.json, .cfg)


```python
loaded_obj = MyClass.load("example.pkl")  # Load object from pickle file
print(loaded_obj.name)  # Output: example
```

### Dealing with Dictionary serialization
To save and load an object from a dictionary, you can use the `to_dict` and `from_dict` methods.

When creating an instance from a given dictionary, the class will try to bind the dictionary 
keys to the class __init__ signature. 
If all the mandatory arguments are present, (i.e. the class is *easy-serializable*) 
the class will **first call 
the __init__ method**, and **then it will overwrite the attributes** with corresponding dictionary values.


If the dictionary is
missing some mandatory arguments, by default the class will raise a *NotSimplySerializable* exception.

However, specifying the `force` parameter to True, a new instance will be created, 
**without calling the __init__ method**.

This is useful when the class is not *easy-serializable* or 
when you want to forse instance creation from a dictionary exported from an old version of the class.

```python
class MyClass(Savable):
    def __init__(self, name,mandatory_arg):
        self.name = str(name) + str(mandatory_arg) 
        # mandatoy_arg is not saved as attribute so the class is not easy-serializable
        

obj = MyClass("example","_mandatory_arg")
obj_dict = obj.to_dict()
print(obj_dict)  # Output: {"name": "example_mandatory_arg"}
new_obj = MyClass.from_dict(obj_dict) # raise NotSimplySerializable exception
new_obj = MyClass.from_dict(obj_dict,force=True) # create a new instance without calling __init__ method

```







### Excluding Attributes from Saving

You can specify attributes to exclude from saving by providing a list to `exclude_from_saving` parameter in the class constructor:

```python
class MyClass(Savable):
    def __init__(self, name, logger):
        self.name = name
        self.logger = logger
        super().__init__(exclude_from_saving=["logger"])

obj = MyClass("example", logger)
obj.save("example.pkl")
```


### Supported Formats

The `Savable` class supports saving and loading objects in the following formats:

- **Pickle (.pkl)**: Binary serialization format.
- **Zip (.zip)**: Compressed archive containing pickle file.
- **JSON (.json)**: JSON serialization format.

## Documentation

For more detailed documentation, including additional options and methods, please refer to the [API Documentation](https://github.com/your-username/savable).

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request with any improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

