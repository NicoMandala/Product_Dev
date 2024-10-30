#here i'm trying to understand the sample names and times that the api get request forms
# while there is slight redundancy(first names start with alphabet and local time zone can be calculated), I want to understand the sample of users first. 
# oh well! I realized that the users are from all over the world and the first letter is not always in english alphabet. 
# Approaches considered for task A
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

# Get the current UTC time
utc_time = datetime.datetime.utcnow()

def offset_parser(offset_str:str):
    offset_str = offset_str.replace(':','')
    sign = offset_str[0]
    minutes = int(offset_str[-2:])
    hours = int(offset_str[1:-2])

    sign = -1 if sign == '-' else 1
    return sign, hours, minutes


def get_person():
    # Make a GET request to the API
    response = requests.get('https://randomuser.me/api/')
    try:
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract the first name and local time of each user
            for user in data['results']:
                first_name = user['name']['first']
                local_time_offset = user['location']['timezone']['offset']
                sign, hours, minutes = offset_parser(local_time_offset)

                first_letter = first_name[0].upper()
                local_time = utc_time + datetime.timedelta(hours=sign*hours, minutes=sign*minutes)

                # Print the first name and local time
                print(f"First Name: {first_name}")
                print(f"First Letter: {first_letter}")
                print(f"Local Time: {local_time}")
                
                return first_name, first_letter, local_time
                
        else:
            pass
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None

if __name__ == "__main__":
    get_person()
