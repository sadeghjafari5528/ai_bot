
import sqlite3
import json

import numberize
conn = sqlite3.connect("ai_db.db")
cur = conn.cursor()
dataSet = open('argumentDataSet.json' , 'w')

l = cur.execute("select text from sample")
for sample in list(l):
    text = sample[0]
    s = numberize.numberize(text)
    data = {}
    data['sentence'] = s
    data['tag'] = []
    dataSet.writelines(str(data) + ",\n")

dataSet.close()