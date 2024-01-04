"""
    Use openai api to expand one-liner description to 55 words, in two sentences
    - Read excel file
    - Make a request to openai
    - save response in excel
"""
#import important modules
from openai import OpenAI
import os.path
import requests
import pandas as pd
from api_keys import API_KEY

#function to read excel file
def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df








