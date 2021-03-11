import os
import json
import pprint


class Utils:
    
    def __init__(self):
        self.path = None
        self.pp = pprint.PrettyPrinter()

    # Must be called before reading from json or serialization       
    def set_path(self, path):
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        self.path = path

    def serialize_json(self, filename, data):
        with open(f"{self.path}/{filename}", "w", encoding="utf8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Data serialized to path: {self.path}/{filename}")

    def read_json(self, file_name):
        complete_path = f"{self.path}/{file_name}"
        if os.path.exists(complete_path):
            with open(complete_path, "r", encoding="utf8") as file:
                data = json.load(file)
            print(f"Data read from path: {complete_path}")
            return data
        else:
            print(f"No data found at path: {complete_path}")
            return {}
        
    def pretty_print(self, data):
        self.pp.pprint(data)
