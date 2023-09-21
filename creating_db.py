import sqlite3

def createDestinantionTable():
    cur.execute("""CREATE TABLE destinations(
                                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                name TEXT UNIQUE NOT NULL,
                                country TEXT NOT NULL,
                                town TEXT NOT NULL,
                                description TEXT,
                                costs INTEGER,
                                attractions INTEGER,
                                transport INTEGER,
                                gastronomy INTEGER,
                                landscapes INTEGER,
                                score_avarge REAL)""")

def createTravelsTable():
    cur.execute("""CREATE TABLE travels(
                                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                name TEXT UNIQUE NOT NULL,
                                budget REAL NOT NULL,
                                from_date TEXT NOT NULL,
                                to_date TEXT NOT NULL,
                                total_expenses REAL NOT NULL)""")

def createTravel_DestinationsTable():
    cur.execute("""CREATE TABLE travel_destinations(
                                travel_id INTEGER,
                                destination_id INTEGER,
                                FOREIGN KEY (travel_id) REFERENCES travels (id),
                                FOREIGN KEY (destination_id) REFERENCES destinations (id))""")

## Destinations,Travel db
## All expenses db

con = sqlite3.connect("database.db")
cur = con.cursor()

createDestinantionTable()
createTravel_DestinationsTable()
createTravelsTable()


#cur.execute("INSERT INTO destinations (name, country, town, description, costs,attractions, transport, gastronomy, landscapes, score_avarge) VALUES ('test1', 'Polska', 'Rakszawa', 'Brak', 1 , 1, 2, 2, 4, 5)")
#cur.execute("INSERT INTO travels (name,budget,from_date,to_date,total_expenses) VALUES ('testTravel', 1234.3, '13-2000', '15-2000', 1000.4)")
#cur.execute("INSERT INTO travel_destinations (travel_id, destination_id) VALUES (3, 4)")
#con.commit()
