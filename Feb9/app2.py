import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()

# For LIKE, 'ch%' looks for any playerID (in this case) that BEGINS WITH "ch". '%ch%' looks for any playerID with "ch" IN IT.
# '%ch' looks for any playerID that ENDS WITH "ch". 
query = """
    SELECT playerID
    FROM Batting
    WHERE playerID LIKE '%ch%'
    GROUP BY playerID
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records, columns=['playerID'])
print(records_df)