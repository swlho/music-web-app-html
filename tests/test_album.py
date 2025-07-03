from lib.album import Album

def test_initialisation():
    album = Album(1, 'Some Title', 2024, 1)
    assert album.id == 1
    assert album.title == 'Some Title'
    assert album.release_year == 2024
    assert album.artist_id == 1

def test_is_valid():
    album = Album(1, 'Some Title', 2024, 1)
    result = album.is_valid()
    assert result == True

def test_is_valid_not_valid_album():
    album = Album(1, "", None, None)
    result = album.is_valid()
    assert result == False
