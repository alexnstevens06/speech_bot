import os

from xai_sdk import Client
from xai_sdk.chat import user, assistant, system

import readchar

import access_config

import datetime

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
TRANSCRIPT_PATH = os.path.join(access_config.get_transcript_path(), f"{timestamp}.txt")



print("Prepping client")
client = Client(
    api_key=os.getenv(access_config.get_api_env_key()),
    timeout = 3600
)
print("Client prepared, prepping chat")
chat = client.chat.create(model = access_config.get_model_name())


system_prompt = access_config.get_system_prompt()
chat.append(
    system(system_prompt)
)

user_persona_prompt = input("Please input the persona you wish to take(leave empty for default): ")
if(user_persona_prompt==""):
    user_persona_prompt = access_config.get_base_user_persona()
chat.append(
    user(user_persona_prompt)
)



ai_persona_prompt = input("Please input the persona you wish your AI roleplay CYOA partner to take(leave empty for default): ")
if(ai_persona_prompt==""):
    ai_persona_prompt = access_config.get_base_AI_persona()
chat.append(
    assistant(ai_persona_prompt)
)


scenario_prompt = input("Please input the scenario in which you would like the CYOA roleplay to take place(leave empty for default): ")
if(scenario_prompt == ""):
    scenario_prompt = access_config.get_base_scenario_prompt()
chat.append(
    user(scenario_prompt)
)



#start main loop

with open(TRANSCRIPT_PATH, "w") as transcript:
        

    print("Are you ready to start? Input 'y' to begin or '0' to escape, '0' is also the way to escape during the adventure")
    key = readchar.readkey()
    while(key not in ['y', '0']):
        print("Ensure you press a valid key")
        key = readchar.readkey()




    response = None

    while(key!="0"):
            for response, chunk in chat.stream():
                print(chunk.content, end="", flush=True)
            else:
                
                try:
                    if response is not None:
                        transcript.write(response.content)
                        transcript.write("\n")
                        #enforce key is betweeen 0 and 3
                        print("\n\nChoose action (1-3) or 0 to quit: ", end="", flush=True)
                        while True:
                            # Read key instantly
                            potential_key = readchar.readkey()
                            
                            # Validate
                            if potential_key in ['0', '1', '2', '3']:
                                key = potential_key # Update the main loop variable
                                print(key) # Visually echo the choice to the user
                                break # Exit the validation loop
                        transcript.write(f'\n{key}\n')
                        chat.append(
                            assistant(response.content)
                        )
                        chat.append(
                            user(key)
                        )
                        transcript.flush()
                    else:
                        raise ValueError("Response was empty for some reason")
                except ValueError as e:
                    print(f"Value error associated with response occurred {e}")
            
