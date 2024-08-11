import sqlite3
import pandas as pd
import os

# Define the file path
csv_file_path = 'Weather Data.csv'

# Check if the file exists
if not os.path.isfile(csv_file_path):
    raise FileNotFoundError(f"The file '{csv_file_path}' does not exist. Please check the file path.")

# Connect to the SQLite database
conn = sqlite3.connect('weather.db')
cursor = conn.cursor()

# Create the table with the correct column names
cursor.execute('''
CREATE TABLE IF NOT EXISTS weather_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    "Date/Time" TEXT,
    "Temp_C" REAL,
    "Dew Point Temp_C" REAL,
    "Rel Hum_%" REAL,
    "Wind Speed_km/h" REAL,
    "Visibility_km" REAL,
    "Press_kPa" REAL,
    "Weather" TEXT
)
''')

# Load data from CSV
df = pd.read_csv(csv_file_path)

# Insert data into the table
df.to_sql('weather_data', conn, if_exists='append', index=False)

# Commit changes and close the connection
conn.commit()
conn.close()

df = pd.read_csv(csv_file_path)
print(df.columns)
