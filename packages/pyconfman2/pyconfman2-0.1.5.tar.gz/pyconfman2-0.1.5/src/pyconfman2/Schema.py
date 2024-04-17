import os
import yaml

from .Exceptions import InvalidPropertyError, EmptyValueProperty, KeyExistsError

class ConfigSchema():
    properties = None

    def __init__(self, default_schema={}, filepath=None, default_config=None) -> None:
        if type(default_schema) != dict:
            raise InvalidPropertyError
        
        self.properties = default_schema
        if default_config:
            if os.path.isfile(default_config):
                self.load(default_config)

        # config.yaml is sorted to the top if it exists otherwise it attempts to load config.yml.
        if not filepath:
            config_file = [item for item in os.listdir() if item == "config.yaml" or item == "config.yml"]
            for item in config_file:
                if os.path.getsize(item) > 0:
                    self.load(item)
                    break
        else:
            if os.path.isfile(filepath):
                self.load(filepath)
    
    def __str__(self) -> str:
        return str(self.properties)
    
    def add(self, nkey, nvalue=None, override=True) -> None:
        if type(nkey) == dict:
            if override:
                self.properties.update(nkey)
            else:
                self.properties = dict(list(nkey.items()) + list(self.properties.items())) 
        else:
            if nvalue == None:
                raise EmptyValueProperty
            self.properties[nkey] = nvalue
    
    def get(self, key, strict=False):
        try:
            return self.properties[key]
        except KeyError as e:
            if strict: raise e
    
    def remove(self, key, strict=False):
        try:
            self.properties.pop(key)
        except KeyError as e:
            if strict: raise e

    
    def load(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundException
        
        with open(filepath, "r") as fh:
            config_file = yaml.safe_load(fh)
        
        self.add(config_file)
    
    def items(self):
        return self.properties.items()
