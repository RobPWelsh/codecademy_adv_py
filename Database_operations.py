import sqlite3

con = sqlite3.connect("toys.db")
curs = con.cursor()

# curs.execute('''CREATE TABLE toys (id INTEGER, name TEXT, price REAL, type TEXT)''')  # run once to create table

# curs.execute('''INSERT INTO toys VALUES(2244560, 'Ultimate Ninja Fighter', 24.99, 'action')''')  # add a single row

# new_toys = [(2244561, 'Hot Wheels', 1.99, 'car'), (2244562, 'Barbie', 34.99, 'doll'), (2244563, 'Jarts', 44.99, 'danger')]

# curs.executemany('''INSERT INTO toys VALUES(?,?,?,?)''', new_toys) # add multiple rows

# con.commit()  # Saves changes to database

# one = curs.execute("SELECT * FROM toys").fetchone()
# print(one)

# three = curs.execute("SELECT * FROM toys").fetchmany(3)
# print(three)

# all_items = curs.execute("SELECT * FROM toys").fetchall()
# print(all_items)

barbie = curs.execute('''SELECT * FROM toys WHERE name = 'Barbie';''').fetchall()
print(barbie)

con.close()  # close the connection
