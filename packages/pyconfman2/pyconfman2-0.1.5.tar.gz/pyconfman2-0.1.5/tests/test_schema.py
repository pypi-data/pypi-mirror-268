import os
import sys
import unittest

sys.path.append("../src/pyconfman2")

from Schema import ConfigSchema
from Exceptions import InvalidPropertyError, EmptyValueProperty, KeyExistsError

class TestSchemaClass(unittest.TestCase):
    # Initialization
    def test_init(self):
        test_init_schema = ConfigSchema()
        self.assertEqual(str(test_init_schema), "{'file_loaded': 'yaml'}")
    
    def test_init_with_config_override(self):
        test_init_schema = ConfigSchema(filepath="config.yml")
        self.assertEqual(str(test_init_schema), "{'file_loaded': 'yml'}")
    
    def test_init_with_default_config_override(self):
        test_init_schema = ConfigSchema(default_config="test_default_config.yml")
        self.assertEqual(str(test_init_schema), "{'file_loaded': 'yaml', 'testing': 'default'}")
    
    def test_init_with_default_schema(self):
        default_schema = { "fookey": "foo", "barkey": "bar" }
        validated_schema = { "fookey": "foo", "barkey": "bar", 'file_loaded': 'yaml'}
        test_default_schema = ConfigSchema(default_schema)
        self.assertEqual(str(test_default_schema), str(validated_schema))
    
    def test_init_raises_invalid_property_error(self):
        default_schema = "{ 'test' }"
        def test_func():
            ConfigSchema(default_schema)
        self.assertRaises(InvalidPropertyError, test_func)
    
    def test_init_with_bad_schema_1(self):
        default_schema = "{ 'test' }"
        def test_func():
            ConfigSchema(default_schema)
        self.assertRaises(InvalidPropertyError, test_func)
    
    def test_init_with_bad_schema_2(self):
        default_schema = "{'test': '123' "
        def test_func():
            ConfigSchema(default_schema)
        self.assertRaises(InvalidPropertyError, test_func)
    
    def test_init_with_bad_schema_3(self):
        default_schema = "abc"
        def test_func():
            ConfigSchema(default_schema)
        self.assertRaises(InvalidPropertyError, test_func)
    
    def test_init_with_bad_schema_4(self):
        default_schema = "123"
        def test_func():
            ConfigSchema(default_schema)
        self.assertRaises(InvalidPropertyError, test_func)
    
    def test_init_with_default_config(self):
        default_schema = "123"
        def test_func():
            ConfigSchema(default_schema)
        self.assertRaises(InvalidPropertyError, test_func)

    # ToString
    def test_str(self):
        default_schema = { "fookey": "foo", "barkey": "bar" }
        test_schema = ConfigSchema(default_schema)
        self.assertEqual(str(test_schema), str(default_schema))

    # Add
    def test_add_new_key_and_value(self):
        default_schema = { "fookey": "foo", "barkey": "bar" }
        validated_schema = { "fookey": "foo", "barkey": "bar", 'file_loaded': 'yaml', "newkey": "value"}
        
        test_schema = ConfigSchema(default_schema)
        test_schema.add("newkey", "value")
    
        self.assertEqual(str(test_schema), str(validated_schema))
    
    def test_add_new_dict(self):
        default_schema = { "fookey": "foo", "barkey": "bar" }
        new_value = { "newkey": "value" }
        validated_schema = { "fookey": "foo", "barkey": "bar",'file_loaded': 'yaml', "newkey": "value" }

        test_schema = ConfigSchema(default_schema)
        test_schema.add(new_value)
    
        self.assertEqual(str(test_schema), str(validated_schema))
    
    def test_add_new_dict_with_override(self):
        default_schema = { "fookey": "foo", "barkey": "bar", "newkey": "value" }
        new_value = { "newkey": "new_value", "newkey_2": "new_value" }
        validated_schema = { "fookey": "foo", "barkey": "bar", "newkey": "new_value", 'file_loaded': 'yaml', "newkey_2": "new_value" }

        test_schema = ConfigSchema(default_schema)
        test_schema.add(new_value)
    
        self.assertEqual(str(test_schema), str(validated_schema))
    
    def test_add_new_dict_without_override(self):
        default_schema = { "fookey": "foo", "barkey": "bar", "newkey": "value" }
        new_value = { "newkey": "new_value", "newkey_2": "new_value" }
        validated_schema = {"newkey": "value", "newkey_2": "new_value", "fookey": "foo", "barkey": "bar", 'file_loaded': 'yaml'}

        test_schema = ConfigSchema(default_schema)
        test_schema.add(new_value, override=False)
    
        self.assertEqual(str(test_schema), str(validated_schema))
    
    def test_add_empty_value(self):
        default_schema = { "fookey": "foo", "barkey": "bar", "newkey": "value" }
        new_value = { "newkey" }

        test_schema = ConfigSchema(default_schema)
        def test_func(): 
            test_schema.add(new_value)

        self.assertRaises(EmptyValueProperty, test_func)
    
    # Get
    def test_get_valid_value(self):
        default_schema = { "fookey": "foo", "barkey": "bar", "newkey": "value" }
        test_schema = ConfigSchema(default_schema)
        self.assertEqual("foo", test_schema.get("fookey"))
    
    def test_get_invalid_value_not_strict(self):
        default_schema = { "fookey": "foo", "barkey": "bar", "newkey": "value" }
        test_schema = ConfigSchema(default_schema)
        self.assertEqual(None, test_schema.get("not_a_key"))
    
    def test_get_invalid_value_strict(self):
        default_schema = { "fookey": "foo", "barkey": "bar", "newkey": "value" }
        test_schema = ConfigSchema(default_schema)
        def test_func():
            test_schema.get("not_a_key", strict=True)
        self.assertRaises(KeyError, test_func)

    # Remove
    def test_remove_valid_key(self):
        default_schema = { "fookey": "foo", "barkey": "bar" }
        validated_schema = { "barkey": "bar", 'file_loaded': 'yaml' }

        test_schema = ConfigSchema(default_schema)
        test_schema.remove("fookey")

        self.assertEqual(str(test_schema), str(validated_schema))

    def test_remove_invalid_key_not_strict(self):
        default_schema = { "fookey": "foo", "barkey": "bar" }
        validated_schema = { "fookey": "foo", "barkey": "bar", 'file_loaded': 'yaml' }

        test_schema = ConfigSchema(default_schema)
        test_schema.remove("no_key")
        
        self.assertEqual(str(test_schema), str(validated_schema))
    
    def test_remove_invalid_key_strict(self):
        default_schema = { "fookey": "foo", "barkey": "bar" }
        validated_schema = { "fookey": "foo", "barkey": "bar" }

        test_schema = ConfigSchema(default_schema)
        def test_func():
            test_schema.remove("no_key", strict=True)
        
        self.assertRaises(KeyError, test_func)
    
    # Load
    def test_load_valid_file(self):
        validated_schema = {
            'file_loaded': 'yaml',
            "specific": True,
            "learn": 194.3,
            "fish": {
                "spell": {
                "crop": False,
                "happen": 6690.3106,
                "taste": "three",
                "replace": False
                },
                "satellites": False,
                "vegetable": True,
                "powerful": "amount"
                },
            "flat": -64.27,
            "hole": False,
            "lot": False
        }

        test_schema = ConfigSchema(default_schema={})
        test_schema.load("test_schema_config.yml")
        self.assertEqual(str(test_schema), str(validated_schema))