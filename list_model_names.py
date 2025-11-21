import os

from xai_sdk import Client
#client holds connection and verification to api

#setup time is time that data needs to arrive early for state register to operate correctly
#full time is sequential logic+propogation logic+startup time

client = Client(
    api_key = os.getenv("GROK_API_KEY"),
    timeout = 3600
)

response = client.models.list_language_models()

for i in response:
    print(i.name)