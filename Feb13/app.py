import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
    SELECT batting.yearID, teams.name, batting.HR
    FROM batting inner join teams 
    ON batting.yearID = teams.yearID and batting.teamID = teams.teamID
    WHERE playerID = 'ruthba01'
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records, columns = ['yearID', 'name', 'HR'])
print(records_df)