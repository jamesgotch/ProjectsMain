import sqlite3
import pandas as pd
import gradio as gr


conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
    WITH top_hitters AS (SELECT people.nameFirst, people.nameLast
    FROM batting INNER JOIN people
    ON batting.playerID = people.playerID
    WHERE teamID = 'PHI'
    GROUP BY batting.playerID
    ORDER BY sum(HR) DESC
    LIMIT 10)

    SELECT CONCAT(nameFirst, ' ', nameLast) AS player
    FROM top_hitters
    ORDER BY nameLast ASC
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()


players = []
for record in records:
    players.append(record[0])

def get_player_data(player):
    return f"Data for {player}"

iface = gr.Interface(
    fn = get_player_data,
    inputs = gr.Dropdown(choices = players, label = "Select a Player"),
    outputs = gr.Textbox(label = "Player Data")
)
iface.launch()