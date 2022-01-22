import sqlite3

name = "KaiYi"
sport = "Diving"

db = sqlite3.connect("./froshims.db")

db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", (name, sport))

db.execute("SELECT * FROM registrants")