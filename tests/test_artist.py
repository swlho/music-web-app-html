from lib.artist import Artist

def test_initialisation():
    artist = Artist(1, 'Test artist', 'Rock')
    assert artist.id == 1
    assert artist.name == 'Test artist'
    assert artist.genre == 'Rock'