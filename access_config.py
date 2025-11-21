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

def get_temp_file():
    return config_accessor["temp_file_write"]

def list_elements():
    print(config_accessor.keys())

def get_base_AI_persona():
    return config_accessor["base_AI_persona"]

def get_base_user_persona():
    return config_accessor["base_user_persona"]

def get_base_scenario_prompt():
    return config_accessor["base_scenario_prompt"]

def get_system_prompt():
    return config_accessor["system_prompt"]