from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from lib.album import Album

def test_all_return_all_artists(db_connection):
    db_connection.seed('seeds/music_directory.sql')
    repository = ArtistRepository(db_connection)
    result = repository.all()
    assert result == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz')
    ]


def test_add_artist_add_artist_into_database(db_connection):
    db_connection.seed('seeds/music_directory.sql')
    repository = ArtistRepository(db_connection)
    repository.add_artist("Wild nothing", "Indie")
    result = repository.all()
    assert result == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, 'Wild nothing', 'Indie')
    ]


def test_get_artist_with_albums(db_connection):
    db_connection.seed('seeds/music_directory.sql')
    repository = ArtistRepository(db_connection)
    result = repository.get_artist_with_albums(1)
    assert result == {"artist": Artist(1, 'Pixies', 'Rock'), "albums": [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(5, 'Bossanova', 1990, 1)
    ]}


def test_artist_exists(db_connection):
    db_connection.seed('seeds/music_directory.sql')
    repository = ArtistRepository(db_connection)
    result = repository.artist_exists("Pixies")
    assert result == 1


def test_artist_exists_return_none_if_doesnt_exist(db_connection):
    db_connection.seed('seeds/music_directory.sql')
    repository = ArtistRepository(db_connection)
    result = repository.artist_exists("Some band")
    assert result == None
