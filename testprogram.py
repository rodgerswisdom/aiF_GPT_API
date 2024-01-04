
from openai import OpenAI
#client = OpenAI(api_key="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")
#client = OpenAI(api_key="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")

from api_keys import API_KEY

client = OpenAI(api_key=API_KEY)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!Whats the capital of Kenya?"}
  ]
)

print(completion.choices[0].message)
