import json

from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate


class JsonUtil:
    @staticmethod
    def get_json_str_from_dict(json_dict: dict, clsEncoder=None) -> str:
        """To get json str from a json dict
        """
        json_str = json.dumps(json_dict, indent=4, cls=clsEncoder)
        return json_str

    @staticmethod
    def get_json_dict_from_str(json_str: str) -> object:
        """To get json dict object from a json str
        """
        json_obj = json.loads(json_str)
        return json_obj

    @staticmethod
    def get_json_dict_from_file(filepath: str) -> object:
        """ To get json dict object from a json file
        """
        try:
            with open(filepath, mode='r') as f:
                data = json.load(f)
        except FileNotFoundError:
            assert False, 'File not found: ' + filepath
        return data

    @staticmethod
    def get_json_str_from_file(filepath: str) -> str:
        """ To get json str object from a json file
        """
        try:
            with open(filepath, mode='r') as f:
                data = json.load(f)
                data = JsonUtil.get_json_str_from_dict(data)
        except FileNotFoundError:
            assert False, 'File not found: ' + filepath
        return data

    @staticmethod
    def get_json_dict_val(json_dict, path):
        """To get value for a json path(eg: person.address.name)
        """
        keys = path.split('.')

        for key in keys:
            isCurrKeyList = True if '[' in key else False
            arrIndex = key[key.find("[") + 1:key.find("]", key.find("["))] if isCurrKeyList and key.find(
                "[") + 1 != key.find("]") else '' if isCurrKeyList else None
            calcArrIndex = 0 if arrIndex is None or arrIndex == '' else int(arrIndex)
            calcKey = key.replace(f'[{arrIndex}]', '') if isCurrKeyList else key

            if isCurrKeyList:
                json_dict = json_dict[calcKey][calcArrIndex]
            else:
                json_dict = json_dict.get(key, None)

        return json_dict

    @staticmethod
    def compare_json_val(json_dict, json_path, json_val):
        """Compare single json val and returns True/False
        """
        act_json_val = JsonUtil.get_json_dict_val(json_dict, json_path)

        isMatched = True if f"{act_json_val}" == f"{json_val}" else False
        if isMatched:
            print(f"{json_path} matched with {json_val}")
        else:
            print(f"{json_path} didnt match, actual {act_json_val}, expected {json_val}")

        return isMatched

    @staticmethod
    def compare_json_type(class_name, required_keys, json_dict=None, json_str=None):
        """class_name: Json is of which type
        required_keys: All required keys in json dict
        """
        assert json_dict is not None or json_str is not None, 'Both json params are None'

        isMatched = False
        try:
            '''Parse the json str into a dict'''
            if json_dict is None:
                json_dict = json.loads(json_str)

            '''Check if all required keys are in the dict'''
            if all(key in json_dict for key in required_keys):
                '''Try to create an object of the given class from the dict'''
                obj = class_name(**json_dict)
                isMatched = True
        except Exception as e:
            print(f"Error: {e}")
            isMatched = False

        if isMatched:
            print(f"Json type matched with {class_name} for {required_keys}")
        else:
            print(f"Json type didnt match with {class_name} for {required_keys}")

        return isMatched

    @staticmethod
    def compare_json_schema(json_dict, json_schema):
        """Compare json dict with schema
        """
        isMatched = False
        try:
            validate(json_dict, json_schema)
            isMatched = True
        except ValidationError as e:
            print(str(e))

        if isMatched:
            print(f"Json schema matched with {json_schema}")
        else:
            print(f"Json schema didnt match with {json_schema}")

        return isMatched
