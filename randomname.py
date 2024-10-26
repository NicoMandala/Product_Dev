#here i'm trying to understand the sample names and times that the api get request forms
# while there is slight redundancy(first names start with alphabet and local time zone can be calculated), I want to understand the sample of users first. 
# oh well! I realized that the users are from all over the world and the first letter is not always in english alphabet. 
# Approaches considered for task B
# iteration 1 : Address english alphabet only
    # Examine how many cocktails have names 
    # Examine how many users have first name in english alphabet
    # Generating a list of about 120 cocktails to cover all the alphabets - missing u and x
    # Generating a list of 150 cocktails to check if that covers all the alphabets
# iteration 2 : Translate the name it english and address the first letter

import requests
import datetime
from typing import List
from pydantic import BaseModel


# Make a GET request to the API
response = requests.get('https://randomuser.me/api/?results=30')

# Get the current UTC time
utc_time = datetime.datetime.utcnow()

def first_letter_parser(first_name:str):
    # Parse the first letter of the first name
    first_letter = first_name[0].lower()
    if first_letter.isalpha():
        return first_letter
    else:
        return None
    

def offset_parser(offset_str:str):
    offset_str = offset_str.replace(':','')
    sign = offset_str[0]
    minutes = int(offset_str[-2:])
    hours = offset_str.strip





# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the first name and local time of each user
    for user in data['results']:
        first_name = user['name']['first']
        local_time_offset = user['location']['timezone']['offset']
        first_letter = first_letter_parser(first_name)
        # local_time = utc_time + datetime.timedelta(hours=local_time_offset)

        # Print the first name and local time
        print(f"First Name: {first_name}")
        print(f"First Letter: {first_letter}")
        print(f"Local Time: {local_time_offset}")
        print()
else:
    print("Failed to fetch data from the API.")

def parse_offset(offset_str):
    # Parse the offset string
    sign = offset_str[0]
    # hours

