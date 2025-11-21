import os

from xai_sdk import Client
from xai_sdk.chat import user, assistant, system

import readchar

import access_config


client = Client(
    api_key=os.getenv(access_config.get_api_env_key()),
    timeout = 3600
)

chat = client.chat.create(model = access_config.get_model_name())

ai_persona_prompt = input("Please input the persona you wish your AI roleplay CYOA partner to take(leave empty for default): ")
if(ai_persona_prompt==""):
    persona_prompt = access_config.get_base_AI_persona()

user_persona_prompt = input("Please input the persona you wish to take(leave empty for default): ")
if(user_persona_prompt==""):
    user_persona_prompt = access_config.get_base_user_persona()

scenario_prompt = input("Please input the scenario in which you would like the CYOA roleplay to take place(leave empty for default): ")
if(scenario_prompt == ""):
    scenario_prmpt = access_config.get_base_scenario_prompt()

system_prompt = access_config.get_system_prompt()

chat.append(
    system(system_prompt)
)
chat.append(
    user(user_persona_prompt)
)
chat.append(
    assistant(ai_persona_prompt)
)
chat.append(
    user(scenario_prompt)
)



#start main loop
key = readchar.readkey()

response = None

while(key!="0"):
        for chunk,response in chat.stream():
            pass
        
        else:
            try:
                if response is None
            except:
        
