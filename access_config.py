import json
CONFIG_FILE = "config.json"

try:

    with open(CONFIG_FILE, 'r') as file:
        config_accessor = json.load(file)

except FileNotFoundError:
    config_accessor = {}
    print(f'WARNING CONFIG ACCESSOR FAILED TO OPEN FILE')


def get_model_name():
    return config_accessor["model"]


def get_api_env_key():
    return config_accessor["api_key_environment_name"]