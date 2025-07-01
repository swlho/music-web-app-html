from lib.artist import Artist

class ArtistRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM artists')
        artists = [Artist(artist["id"], artist["name"], artist["genre"]) for artist in rows]
        return artists
    
    def add_artist(self, name, genre):
        self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s)', [name, genre])