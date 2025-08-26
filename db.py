import sqlite3

conn = sqlite3.connect('growly.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS crops (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    plant_start DATE NOT NULL,
    plant_end DATE NOT NULL,
    harvest_start DATE NOT NULL,
    harvest_end DATE NOT NULL
)''')
conn.commit()

cur.execute("INSERT INTO crops (name, plant_start, plant_end, harvest_start, harvest_end) VALUES (?, ?, ?, ?, ?)",
            ("Tomato", "2023-03-01", "2023-03-15", "2023-07-01", "2023-07-15"))
cur.execute("INSERT INTO crops (name, plant_start, plant_end, harvest_start, harvest_end) VALUES (?, ?, ?, ?, ?)",
            ("Pepper", "2023-03-01", "2023-03-15", "2023-07-01", "2023-07-15"))
cur.execute("INSERT INTO crops (name, plant_start, plant_end, harvest_start, harvest_end) VALUES (?, ?, ?, ?, ?)",
            ("Cucumber", "2023-02-01", "2023-02-15", "2023-06-01", "2023-06-15"))
cur.execute("INSERT INTO crops (name, plant_start, plant_end, harvest_start, harvest_end) VALUES (?, ?, ?, ?, ?)",
            ("Letttuce", "2023-02-01", "2023-02-15", "2023-06-01", "2023-06-15"))
conn.commit()

cur.close()
conn.close()