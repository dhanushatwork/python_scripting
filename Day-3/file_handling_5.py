import json
import yaml

def yml_to_json(yaml_file, json_file):
    with open("config.yml", "r") as file:
        data = yaml.safe_load(file)  
        print(data) 

    with open("config.json", "w") as jfile:
        json.dump(data, jfile, indent=4)

yml_to_json("config.yml", "config.json")        
print("Conversion completed")