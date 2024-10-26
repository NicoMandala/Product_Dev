import sqlite3
import requests

# Not being able to create new database because of the restrictions IT has on the system.
# I will use the tutorials.db database to create the table

"""The Aim of this script is to collect a database of cocktails and their ingredients ready to call based on the first letter of the first name in person api
    The list of cocktails will be generated from modified cocktail API in task 1
    """

link = 'http://127.0.0.1:8000/random_cocktail/'

# sqlite3 cocktails.db
conn = sqlite3.connect('tutorials.db')

cur = conn.cursor()
# Check if the table 'cocktails' exists
cur.execute("""
SELECT name FROM sqlite_master WHERE type='table' AND name='cocktails';
""")

# Fetch the result
table_exists = cur.fetchone()

# If the table does not exist, create it
if not table_exists:
    cur.execute("""
    CREATE TABLE cocktails(
	id INT,
  	name VARCHAR(50),
    first_letter VARCHAR(1),
  	tagline VARCHAR(250),
  	ingredient_1 VARCHAR(50),
	ingredient_2 VARCHAR(50),
	ingredient_3 VARCHAR(50),
	ingredient_4 VARCHAR(50),
	ingredient_5 VARCHAR(50),
  	ingredient_6 VARCHAR(50),
  	ingredient_7 VARCHAR(50),
  	ingredient_8 VARCHAR(50), 
  	ingredient_9 VARCHAR(50), 
  	ingredient_10 VARCHAR(50),
  	ingredient_11 VARCHAR(50), 
  	ingredient_12 VARCHAR(50), 
  	ingredient_13 VARCHAR(50), 
  	ingredient_14 VARCHAR(50), 
  	ingredient_15 VARCHAR(50),
	instructions VARCHAR(250)
    );
    """)

for i in range(1,15):
    f"ingredient_{i} = ''"

# Insert a new row into the table
for i in range(2,151):
    try:
        response = requests.get(link)
        print("connected to the API")
        if response.status_code == 200:
            data = response.json()

            # Extract the cocktail details from the response
            id = i
            name = data['name']
            tagline = data['tagline']
            ingredients = data['ingredients']
            instructions = data['instructions']

            # handle the exception for ingredients that are not available
            ingredients += [''] * (15 - len(ingredients))
            ingredient_values = ingredients[:15]

            # Insert the cocktail details into the table
            cur.execute("""
                        INSERT INTO cocktails (
                        id,
                        name,
                        first_letter,
                        tagline,
                        ingredient_1, ingredient_2, ingredient_3, ingredient_4, ingredient_5,
                        ingredient_6, ingredient_7, ingredient_8, ingredient_9,ingredient_10,
                        ingredient_11, ingredient_12, ingredient_13, ingredient_14, ingredient_15,
                        instructions)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                        (
                        id,
                        name,
                        name[0].upper(),
                        tagline,
                        *ingredients,
                        instructions))
    
            conn.commit() # Commit the transaction

            print(f"Inserted {name} into the table.")
        else:
            print("Failed to fetch data from the API.")            
    except Exception as e:
        print(f"Error occurred for cocktail {i + 1}: {e}")       



show_table = cur.execute("SELECT * FROM cocktails")
rows = cur.fetchall()

print(rows)


conn.commit()
conn.close()