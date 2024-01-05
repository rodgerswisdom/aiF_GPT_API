
from openai import OpenAI
#from api_keys import API_KEY
import pandas as pd


client = OpenAI(api_key="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")
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello"}
  ]
)

print(completion.choices[0].message)


