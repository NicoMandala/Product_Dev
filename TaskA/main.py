# The aim of this script is the following
# 1. Use Person API to get the local time and first name of the user 
# 2. if the local time is daytime, suggest a random cocktail from the database
# 3. if the local time is nighttime, suggest a cocktail with the first letter of the first name of the user
# 4. if the local time is not available, suggest a random cocktail from the database

# import the necessary libraries
import requests
import sqlite3
import datetime
from fastapi import FastAPI

from TaskA.person import get_person

# connect to the database
# conn = sqlite3.connect('tutorials.db')

# cur = conn.cursor()
# get the person details
# first_name, first_letter, local_time = get_person()

app = FastAPI()

def suggest_cocktail():
    # connect to the database
    conn = sqlite3.connect('tutorials.db', check_same_thread=False)

    cur = conn.cursor()

    try:
        # get the person details
        first_name, first_letter, local_time = get_person()
        # check if the local time is available
        if local_time:
            # check if it is daytime
            if local_time.hour >= 6 and local_time.hour < 18:
                # suggest a random cocktail from the database
                cur.execute(""" SELECT * FROM cocktails Order by RANDOM() LIMIT 1;""")
                random_cocktail = cur.fetchone()
                print("Selecting a random cocktail from the database because it is daytime")
                print(f"ehi {first_name}, why don't you try a {random_cocktail[1]}?")

                return ({"first_name":first_name,
                         "first_letter":first_letter,
                         "local_time":local_time,
                         "suggestion":f"ehi {first_name}, why don't you try a {random_cocktail[1]}?"
                         })
            else:
                # night time
                # suggest a cocktail with the first letter of first name if it exists in the list
                # if the name is not in english alphabet or there is no cocktail matching the first name, suggest a random cocktail
                if first_letter.isalpha():
                    try:
                        cur.execute("""SELECT * FROM cocktails 
                                    WHERE first_letter = ?
                                    ORDER BY RANDOM() 
                                    LIMIT 1;""",
                                    (first_letter,))
                        
                        cocktail = cur.fetchone()
                        print("Selecting a cocktail from the database based on the first letter of the first name")
                        print(f"ehi {first_name}, why don't you try a {cocktail[1]}?")
                        return ({"first_name":first_name,
                         "first_letter":first_letter,
                         "local_time":local_time,
                         "suggestion":f"ehi {first_name}, why don't you try a {cocktail[1]}?"
                         })
                    
                    except:
                        cur.execute("""SELECT * FROM cocktails 
                                    ORDER BY RANDOM() 
                                    LIMIT 1;""")
                        cocktail = cur.fetchone()
                        print("Selecting a random cocktail from the database because there is no matching cocktail for the first name")
                        print(f"ehi {first_name}, how about a cocktail just made for you {cocktail[1]}?")
                        return ({"first_name":first_name,
                         "first_letter":first_letter,
                         "local_time":local_time,
                         "suggestion":f"ehi {first_name}, how about a cocktail just made for you {cocktail[1]}?"
                         })
                        
                else:
                    try:
                        cur.execute("""SELECT * FROM cocktails 
                                    ORDER BY RANDOM() 
                                    LIMIT 1;""")
                        cocktail = cur.fetchone()
                        print("Selecting a random cocktail from the database because the first name is not in English alphabet")
                        print(f"ehi {first_name}, how about a {cocktail[1]}?")

                        return {"first_name":first_name,
                         "first_letter":first_letter,
                         "local_time":local_time,
                         "suggestion":f"ehi {first_name}, how about a {cocktail[1]}?"
                         }
                    
                    except Exception as e:
                        print(f"Print an error occurred: {e}")
    except Exception as e:  
        print(f"An error occurred: {e}")
                      
    finally:
        cur.close()
        conn.close()

@app.get("/suggestion/")
def get_suggestion():
    return suggest_cocktail()

if __name__ == "__main__":
    from person import get_person
    suggest_cocktail()