import sqlite3
from sqlite3 import Error
import json
import pandas as pd
import datetime

# connect to sqlite3
conn = sqlite3.connect('rasa.db')

cur = conn.cursor()
cur.execute("select * from events")  # events store all the conversation data

rows = cur.fetchall()
conv_output = pd.DataFrame()
for row in rows:
  sessionID = row[0]
  info_json = json.loads(row[6])
  info_df = pd.json_normalize(info_json)
  info_df['sessionID'] = sessionID
  conv_output = pd.concat([conv_output, info_df])

# to find today's date
date_info = datetime.date.today()
conv_output.to_csv(str(date_info) + "_conversation_history.csv", index=False)
