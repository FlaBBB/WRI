import json
import sqlite3

def convert(db_name):
    conn = sqlite3.connect(f'{db_name}.db')

    cursor = conn.cursor()
    
    
    with open(f'{db_name}.json', 'r') as json_file:
        data = json.load(json_file)
        
    cursor.execute('''
CREATE TABLE IF NOT EXISTS dummy(
    id TEXT PRIMARY KEY,
    guid TEXT,
    balance TEXT,
    age INT,
    name TEXT,
    gender TEXT,
    company TEXT,
    email TEXT
)
''')
    
    for item in data:
        try:
            cursor.execute(f'''
INSERT INTO dummy VALUES
    (
        '{item["_id"]}',
        '{item["guid"]}',
        '{item["balance"]}',
        {item["age"]},
        '{item["name"]}',
        '{item["gender"]}',
        '{item["company"]}',
        '{item["email"]}'
    )
''')
        except:
            continue
    conn.commit()
    conn.close()

convert("my-database-2")