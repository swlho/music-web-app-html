from lib.album import Album

def test_initialisation():
    album = Album(1, 'Some Title', 2024, 1)
    assert album.id == 1
    assert album.title == 'Some Title'
    assert album.release_year == 2024
    assert album.artist_id == 1