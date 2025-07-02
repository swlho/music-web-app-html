import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums/index.html', albums=albums)

@app.route('/albums/<int:album_id>', methods=['GET'])
def get_album_by_id(album_id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.get_album_with_artist(album_id)
    return render_template('albums/index.html', albums=albums)

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template('artists/index.html', artists=artists)

@app.route('/artists/<int:artist_id>', methods=['GET'])
def get_artist_by_id(artist_id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist, albums = repository.get_artist_with_albums(artist_id).values()
    return render_template('artists/[slug]/index.html', artist=artist, albums=albums)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
