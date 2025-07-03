import os
from flask import Flask, redirect, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album
from lib.artist import Artist


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/', methods=['GET'])
def reroute():
    return redirect('/artists')

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums/albums.html', albums=albums)


@app.route('/albums/<int:album_id>', methods=['GET'])
def get_album_by_id(album_id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.get_album_with_artist(album_id)
    return render_template('albums/albums.html', albums=albums)


@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template('artists/artists.html', artists=artists)


@app.route('/artists/<int:artist_id>', methods=['GET'])
def get_artist_by_id(artist_id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist, albums = repository.get_artist_with_albums(artist_id).values()
    return render_template('artists/[slug]/artist.html', artist=artist, albums=albums)


@app.route('/albums/new', methods=['GET'])
def get_create_album():
    return render_template('albums/new.html', props=None)


@app.route('/albums', methods=['POST'])
def post_new_album():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)
    title = request.form['title']
    release_year = request.form['release-year']
    artist_name = request.form['artist']
    artist_id = artist_repository.artist_exists(artist_name)
    album = Album(None, title, release_year, artist_id)
    if not album.is_valid():
        props = {"album": album, "errors": album.generate_album_errors()}
        if not artist_id:
            props.update({"artist_error": artist_repository.generate_artist_error()})
        return render_template('albums/new.html', props=props)
    new_album = album_repository.add_album(album)
    return redirect(f"/albums/{new_album.id}")

@app.route('/artists/new', methods=['GET'])
def get_create_artist():
    return render_template('artists/new.html', props=None)


@app.route('/artists', methods=['POST'])
def post_new_artist():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artist_name = request.form['name']
    artist_genre = request.form['genre']
    artist_exists = artist_repository.artist_exists(artist_name)
    if artist_exists:
        return render_template('artists/new.html', error=artist_repository.generate_artist_exists_error())
    artist = Artist(None, artist_name, artist_genre)
    new_artist = artist_repository.add_artist(artist)
    return redirect(f"/artists/{new_artist.id}")

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
