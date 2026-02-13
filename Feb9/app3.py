import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
    SELECT teamID, sum(HR)
    FROM batting
    WHERE yearID = 2025
    GROUP BY teamID
    HAVING sum(HR) > 200 -- HAVING is filtering results of what you grouped by. 
    ORDER BY sum(HR) DESC
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records, columns=['teamID', 'sum(HR)'])
print(records_df)