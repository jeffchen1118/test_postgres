import psycopg2

# Connect to the 'chinook' database
connection = psycopg2.connect(database='chinook')

# Create a cursor object of the connection
cursor = connection.cursor()

# Query 1 - select all records from the 'Artist' table
# cursor.execute('SELECT * FROM "Artist";')

# Query 2 - select only the "Name" column from the 'Artist' table
# cursor.execute('SELECT "Name" FROM "Artist";')

# Query 3 - select only 'Queen' from the 'Artist' table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = \'Queen\';')
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s;', ["Queen"])

# Query 4 - select only by 'ArtistId' #51 from the 'Artist' table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with 'ArtistId' #51 on the 'Album' table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where the composer is 'Queen'
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ['test'])

# Query 7 - select all exist composers
# cursor.execute('SELECT DISTINCT "Composer" FROM "Track";')

# Query 8 U2; Edge, The track
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ['test'])

# fetch the result of the query (all)
results = cursor.fetchall()

# fetch the result (single) of the query
result = cursor.fetchone()

#close the connection
connection.close()

# print the result

for result in results:
    print(result)

 