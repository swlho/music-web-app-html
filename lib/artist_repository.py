from lib.artist import Artist
from lib.album import Album

class ArtistRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM artists')
        artists = [Artist(artist["id"], artist["name"], artist["genre"]) for artist in rows]
        return artists
    
    def add_artist(self, name, genre):
        self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s)', [name, genre])

    def get_artist_with_albums(self, artist_id):
        rows = self._connection.execute('SELECT albums.id AS album_id, albums.title, albums.release_year, artists.id AS artist_id, artists.name, artists.genre FROM albums JOIN artists ON albums.artist_id = artists.id WHERE artists.id = %s', [artist_id])
        artist = Artist(rows[0]["artist_id"], rows[0]["name"], rows[0]["genre"])
        albums = [Album(row["album_id"], row["title"], row["release_year"], row["artist_id"]) for row in rows]
        return {"artist": artist, "albums": albums}

    def artist_exists(self, artist_name):
        artist = self._connection.execute('SELECT id FROM artists WHERE name = %s', [artist_name])
        if artist:
            return artist[0]["id"]
        else:
            return None

    def generate_artist_error(self):
        return "Artist not in database! Please add the artist first before adding albums for them."
