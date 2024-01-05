import pandas as pd
from openai import OpenAI
from api_keys import API_KEY  # Make sure to replace this with your actual API key

# Set your OpenAI API key
openai.api_key = API_KEY

# Function to generate expanded descriptions using OpenAI ChatGPT API
def generate_expanded_description(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_tokens=200
    )
    return response['choices'][0]['message']['content']

# Example user input
user_input = "Hello! What's the capital of Kenya?"

# Generate expanded description
expanded_description = generate_expanded_description(user_input)

# Create a DataFrame to store the result
result_df = pd.DataFrame({"User Input": [user_input], "Expanded Description": [expanded_description]})

# Save the DataFrame to an Excel file
result_df.to_excel("output_result.xlsx", index=False)

# Display the result
print(result_df)
