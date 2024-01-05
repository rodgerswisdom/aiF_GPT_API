
from openai import OpenAI
from api_keys import API_KEY
import pandas as pd

user_input = "Interior design AI generator"

client = OpenAI(api_key=API_KEY)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": f"Expand the one-liner description below to 55 words using 2 sentences:{user_input}"}
  ]
)

print(completion.choices[0].message)


