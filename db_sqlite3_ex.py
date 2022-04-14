import sqlite3

conn = sqlite3.connect("main")
uc = conn.cursor()

try:
    uc.execute("CREATE TABLE movies(id INTEGER,"
               "movie TEXT,"
               "year TEXT,"
               "rating REAL,"
               "studio TEXT"
               ")")
except sqlite3.OperationalError:
    pass

uDataset = ((1, "Up", 2009, 8.3, "Pixar"),
            (2, "Toy Story", 2007, 8.5, "Pixar"),
            (3, "Finding Nemo", 2011, 9.3, "Disney"),
            (4, "Avengers", 2011, 9.3, "Marvel"),
            (5, "Mona", 2009, 8.9, "Disney"))
for item in uDataset:
    uc.execute("INSERT INTO movies VALUES (?, ?, ?, ?, ?)", item)
    conn.commit()

uQuery = uc.execute("SELECT * from movies")

print("Movie Database Output")
for row in uQuery:
    for column in row:
        print(column)
    print("-----")
conn.close()
