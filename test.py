import sqlite3

# Połącz się z bazą danych lub stwórz nową bazę danych
conn = sqlite3.connect('moja_baza_danych.db')
cursor = conn.cursor()

# Utwórz tabelę z unikalnym licznikiem jako ID
cursor.execute('''CREATE TABLE IF NOT EXISTS dane (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nazwa TEXT
                )''')

# Dodaj przykładowe dane
cursor.execute("INSERT INTO dane (nazwa) VALUES (?)", ('Rekord 1',))
cursor.execute("INSERT INTO dane (nazwa) VALUES (?)", ('Rekord 2',))
cursor.execute("INSERT INTO dane (nazwa) VALUES (?)", ('Rekord 3',))

# Wyświetl dane
cursor.execute("SELECT * FROM dane")
print("Dane przed usunięciem:")
for row in cursor.fetchall():
    print(row)

# Usuń rekord z ID 2
cursor.execute("DELETE FROM dane WHERE id = 2")

# Wyświetl dane ponownie
cursor.execute("SELECT * FROM dane")
print("\nDane po usunięciu:")
for row in cursor.fetchall():
    print(row)

# Zamknij połączenie z bazą danych
conn.commit()
conn.close()
