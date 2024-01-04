"""
    Use openai api to expand one-liner description to 55 words, int two sentences
    - Read excel file
    - Make a request to openai
    - save response in excel
"""

"""
import openai
import os.path
import pandas as pd
import requests
"""
"""#Read excel
def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df

# Function to display data
def display_data(data):
    print(data)


# Set your OpenAI API key
#openai.api_key = ' AIzaSyDfajqnwObckLr6eip0qf9BjiCs-ajYfM8'
    
#main function
    
def main():
    file_path = "Description.xlsx"
    data = read_excel(file_path)
    display_data(data)"""

#import pandas as pd
#import openai

"""# Set your OpenAI API key
openai.api_key = 'AIzaSyDfajqnwObckLr6eip0qf9BjiCs-ajYfM8'

# Function to generate descriptions using OpenAI API
def generate_description(tool_description):
    prompt = tool_description
    params = {
        'model': 'text-davinci-003',
        'prompt': prompt,
        'temperature': 0.7,
        'max_tokens': 200,
        'n': 1,
    }
    response = openai.Completion.create(**params)
    return response['choices'][0]['text']

# Read tool descriptions from Excel
df = pd.read_excel('Description.xlsx.xlsx', sheet_name='Sheet1')

# Number of rows to process before saving
batch_size = 50
num_rows = df.shape[0]

# Generate descriptions using OpenAI API and store in a new column
for i in range(0, num_rows, batch_size):
    try:
        end_index = min(i + batch_size, num_rows)
        df.loc[i:end_index, 'Description'] = df.loc[i:end_index, 'Description'].apply(generate_description)
        # Save the updated DataFrame to a new Excel sheet
        df.to_excel(f'output_tool_descriptions_{i + 1}_{end_index}.xlsx', index=False)
    except Exception as e:
        print(f"Error processing rows {i + 1} to {end_index}: {str(e)}")

print("Processing complete. Check output_tool_descriptions files for results.")
#import pandas as pd
#import openai

# Set your OpenAI API key
openai.api_key = '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'

# Function to generate descriptions using OpenAI API
def generate_description(tool_description):
    prompt = f"Expand the following short description to about 55 words using only two sentences{tool_description}"
    response = openai.chat.completions.create(
        #engine="text-davinci-003",
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=200,
        n=1,
    )
    return response['choices'][0]['text']

# Read tool descriptions from Excel
df = pd.read_excel('Description.xlsx.xlsx', sheet_name='Sheet1')

# Number of rows to process before saving
batch_size = 50
num_rows = df.shape[0]

# Generate descriptions using OpenAI API and store in a new column
for i in range(0, num_rows, batch_size):
    try:
        end_index = min(i + batch_size, num_rows)
        df.loc[i:end_index, 'Description'] = df.loc[i:end_index, 'Description'].apply(generate_description)
        # Save the updated DataFrame to a new Excel sheet
        df.to_excel(f'output_tool_descriptions_{i + 1}_{end_index}.xlsx', index=False)
    except Exception as e:
        print(f"Error processing rows {i + 1} to {end_index}: {str(e)}")

print("Processing complete. Check output_tool_descriptions files for results.")"""

#from openai import OpenAI
import openai

openai.api_key = "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"
#client = OpenAI(api_key)

completion = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)



