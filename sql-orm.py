from sqlalchemy import (
    create_engine, Column, Integer, String, ForeignKey, Float
)

#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

# Create a connection to the database
db = create_engine("postgresql:///chinook")  #/// indicate the default database hosted locally
base = declarative_base()

# create a class for the "Artist" table
class Artist(base):
    __tablename__ = 'Artist'
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# create a class for the "Album" table
class Album(base):
    __tablename__ = 'Album'
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey('Artist.ArtistId'))

# create a class for the "Track" table
class Track(base):
    __tablename__ = 'Track'
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey('Album.AlbumId'))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)

# instead of connecting to the databse we are creating a session
# create a new instance of sessionmaker, then point it to the engine (the db)
Session = sessionmaker(bind=db)
#opens an actual session by calling the Session() subclass defined above
session = Session()

# create the database using declarative_base subclass
base.metadata.create_all(db)

# query 1 - select all records from the 'Artist' table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" |") 

# query 2 - select only the "Name" column from the 'Artist' table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# query 3 - select only 'Queen' from the 'Artist' table
# artist = session.query(Artist).filter_by(Name='Queen').first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# query 4 - select only by 'ArtistId' #51 from the 'Artist' table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# query 5 - select only the albums with 'ArtistId' #51 on the 'Album' table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# query 6 - select all tracks where the composer is 'Queen'
tracks = session.query(Track).filter_by(Composer='Queen')
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId, 
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice, 
        sep=" | "
    )