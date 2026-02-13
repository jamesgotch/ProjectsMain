import sqlite3
import pandas as pd

# conn  = sqlite3.connect('baseball.db') creates a connection to the database,
# cursor = conn.cursor() creates a cursor object that allows you to execute SQL commands. 
conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()

# Query commands consist of SELECT, FROM, WHERE, ORDER BY, LIMIT, and GROUP BY. SELECT is what you want 
# to pull, FROM is the table you want to pull from, WHERE is the conditions for what you want to pull, 
# ORDER BY is how you want to order the data, LIMIT is how many records you want to pull (5 or 10), and 
# GROUP BY is how you want to group the data. Example: by year (GROUP BY yearID).
query = """ 
    SELECT playerID,yearID,teamID,HR
    FROM batting
    WHERE yearID = 1976 and teamID = 'PHI' and HR != 0
    GROUP BY playerID
    ORDER BY HR desc
    HAVING HR > 10
    LIMIT 10
"""

# Cursor.execute(query) runs the query you defined above, and fetchall() pulls all the records that meet
# the conditions of the query (you defined). Finally, you close the connection to the database.
cursor.execute(query)
records = cursor.fetchall()
conn.close()

# Name/define the dataframe with "records" then _df for dataframe, and then reference "records" in the
# dataframe because thats where you are pulling the data from. Then you have columns = [the ID's you want
# listed inside the dataframe]). And finally you print records_df.
records_df = pd.DataFrame(records, columns = ['playerID','yearID','teamID','HR'])
print(records_df) 