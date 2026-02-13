import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
    SELECT yearID, sum(HR) as SeasonHR
    FROM batting
    WHERE teamID = 'PHI'
    GROUP BY yearID
    ORDER BY SeasonHR desc
    LIMIT 10
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records, columns=['yearID', 'sum(HR)'])
print(records_df)