import sqlite3
import pandas as pd

conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()
query = """
    SELECT playerID,yearID,teamID,HR
    FROM batting
    WHERE yearID = 1976
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records, columns = ['playerID','yearID','teamID','HR'])
print(records_df)