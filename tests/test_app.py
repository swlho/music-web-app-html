from playwright.sync_api import Page, expect

# Tests for your routes go here


def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_directory.sql')
    page.goto(f"http://{test_web_address}/albums")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        'Title: Doolittle Released: 1989',
        'Title: Surfer Rosa Released: 1988',
        'Title: Waterloo Released: 1974',
        'Title: Super Trouper Released: 1980',
        'Title: Bossanova Released: 1990',
        'Title: Lover Released: 2019',
        'Title: Folklore Released: 2020',
        'Title: I Put a Spell on You Released: 1965',
        'Title: Baltimore Released: 1978',
        'Title: Here Comes the Sun Released: 1971',
        'Title: Fodder on My Wings Released: 1982',
        'Title: Ring Ring Released: 1973'
    ])


def test_get_album_by_id_1(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_directory.sql')
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator("h1")
    p_tag = page.locator("p")
    expect(h1_tag).to_have_text(["Doolittle"])
    expect(p_tag).to_have_text(["Release year: 1989\nArtist: Pixies"])


def test_get_artist_details_by_id_1(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_directory.sql')
    page.goto(f"http://{test_web_address}/artists/1")
    h1_tag = page.locator("h1")
    p_tag = page.locator("p")
    li_tag = page.locator("li")
    expect(h1_tag).to_have_text(["Pixies"])
    expect(p_tag).to_have_text(["Rock"])
    expect(li_tag).to_have_text([
        'Doolittle, Released: 1989',
        'Surfer Rosa, Released: 1988',
        'Bossanova, Released: 1990'
        ])


def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_directory.sql')
    page.goto(f"http://{test_web_address}/artists")
    a_tag = page.locator("a")
    expect(a_tag).to_have_text([
        'Pixies, Genre: Rock',
        'ABBA, Genre: Pop',
        'Taylor Swift, Genre: Pop',
        'Nina Simone, Genre: Jazz'
    ])
