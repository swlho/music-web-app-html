from lib.album import Album


class AlbumRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM albums')
        albums = [Album(album["id"], album["title"], album["release_year"], album["artist_id"]) for album in rows]
        return albums

    def add_album(self, album):
        [row] = self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s) RETURNING id', [album.title, album.release_year, album.artist_id])
        album.id = row["id"]
        return album

    def get_album_with_artist(self, album_id):
        [row] = self._connection.execute('SELECT albums.id, albums.title, albums.release_year, albums.artist_id, artists.id AS artist_id, artists.name, artists.genre FROM albums JOIN artists ON albums.artist_id = artists.id WHERE albums.id = %s', [album_id])
        album = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
        return [{'album': album, 'artist': row["name"]}]
