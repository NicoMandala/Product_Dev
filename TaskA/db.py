import sqlite3

# Not being able to create new database because of the restrictions IT has on the system.
# I will use the tutorials.db database to create the table

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
        ingredient_9 VARCHAR(50)
    );
    """)


show_table = cur.execute("SELECT * FROM cocktails")

for row in show_table:
    print(row)

    
conn.commit()
conn.close()