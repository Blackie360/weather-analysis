import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('weather.db')
cursor = conn.cursor()

# Fetch some data from the table
cursor.execute("SELECT * FROM weather_data LIMIT 5;")
rows = cursor.fetchall()
print("Sample data from 'weather_data' table:")
for row in rows:
    print(row)

# Close the connection
conn.close()
