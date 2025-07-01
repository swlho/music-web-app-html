from lib.artist_repository import ArtistRepository
from lib.artist import Artist

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