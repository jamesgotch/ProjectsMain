import sqlite3
import pandas as pd
import gradio as gr


conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
    WITH top_hitters AS (SELECT nameFirst, nameLast, batting.playerID
    FROM batting INNER JOIN people
    ON batting.playerID = people.playerID
    WHERE teamID = 'PHI'
    GROUP BY batting.playerID
    ORDER BY sum(HR) DESC
    LIMIT 20)

    SELECT CONCAT(nameFirst, ' ', nameLast) AS player, playerID
    FROM top_hitters
    ORDER BY nameLast ASC
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()


# players = []
# for record in records:
#     players.append(record[0])

def get_data(player):
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT yearID, HR
        FROM batting
        WHERE playerID = ?
    """
    cursor.execute(query, (player,))
    data = cursor.fetchall()
    conn.close()
    df = pd.DataFrame(data, columns=['yearID', 'HR'])
    return df

with gr.Blocks() as iface:
    dropdown = gr.Dropdown([(r[0], r[1]) for r in records], interactive=True)
    plot = gr.LinePlot(x='yearID', y='HR')
    dropdown.change(get_data, inputs=dropdown, outputs=plot)

iface.launch()