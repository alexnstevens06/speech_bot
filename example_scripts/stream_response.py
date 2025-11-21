import os
import time  # Import the time module
from xai_sdk import Client
from xai_sdk.chat import user, system, assistant

import access_config

# 1. Start the timer
last_checkpoint = time.perf_counter()

model_name = access_config.get_model_name()
env_key = access_config.get_api_env_key()

print("starting to initialize client")
client = Client(
    api_key=os.getenv(env_key),
    timeout=3600
)

# 2. Calculate time for client init and reset checkpoint
current_time = time.perf_counter()
print(f"finished initializing client (took {current_time - last_checkpoint:.4f}s)")
last_checkpoint = current_time

chat = client.chat.create(model=model_name)

# 3. Calculate time for chat creation
current_time = time.perf_counter()
print(f"initialized chat (took {current_time - last_checkpoint:.4f}s)")
last_checkpoint = current_time

chat.append(
    system("what is the answer to life the universe and everything")
)

# 4. Calculate time for appending system prompt
current_time = time.perf_counter()
print(f"appended system prompt (took {current_time - last_checkpoint:.4f}s)")
last_checkpoint = current_time

chat.append(
    user("please enlighten me")
)

# 5. Calculate time for appending user prompt
current_time = time.perf_counter()
print(f"added user part (took {current_time - last_checkpoint:.4f}s)")
# Do NOT reset checkpoint here if you want to time the stream startup + execution together
last_checkpoint = current_time 

print("Starting stream...")
response = None

# 6. The loop executes
for response, chunk in chat.stream():
    print(chunk.content, end="", flush=True)
else:
    # 7. Calculate time for the total stream generation
    
    current_time = time.perf_counter()
    print(f"\n\nStream finished (took {current_time - last_checkpoint:.4f}s)")
    
    try:
        if response is None:
            raise ValueError("chat was empty so response never initialized")
        else:
            chat.append(
                assistant(response.content)
            )
            with open(access_config.get_temp_file(), "w") as file:
                file.write(response.content)
                # file.close() is automatic in a 'with' block, removed for cleanliness
            
    except ValueError as e:    
        print(f'Something happened saving full stream {e}')
