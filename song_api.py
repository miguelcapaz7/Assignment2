from flask import Flask, request
from song import Song
from song_manager import SongManager
from datetime import datetime
import json

app = Flask(__name__)

SONGS_DB = 'songs.sqlite'

song_mgr = SongManager(SONGS_DB)


@app.route('/songs', methods=['POST'])
def add_song():
    """ Adds a song to the db """
    content = request.json

    try:
        song = Song(content['title'], content['artist'], content['runtime'],
                    content['pathname'], content['filename'], content['album'],
                    content['genre'])
        song_id = song_mgr.add_song(song)

        response = app.response_class(
            response=str(song_id),
            status=200
        )
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )

    return response


@app.route('/songs/rating/<string:filename>', methods=['PUT'])
def update_rating(filename):
    """ Updates an the rating of a song in Song Manager """
    content = request.json

    try:
        song = song_mgr.get_song(filename)
        if 'rating' in content.keys():
            song.rating = content['rating']
        song_mgr.update_song(song)

        response = app.response_class(
            status=200
        )
    except ValueError as e:
        status_code = 400
        if str(e) == "Song does not exist":
            status_code = 404

        response = app.response_class(
            response=str(e),
            status=status_code
        )

    return response


@app.route('/songs/play_count/<string:filename>', methods=['PUT'])
def update_play_count(filename):
    """ Updates an the rating of a song in Song Manager """

    content = request.json
    try:
        song = song_mgr.get_song(filename)
        if 'play_count' in content.keys():
            song.play_count += 1
        if 'last_played' in content.keys():
            song.last_played = datetime.now()
        song_mgr.update_song(song)

        response = app.response_class(
            status=200
        )
    except ValueError as e:
        status_code = 400
        if str(e) == "Song does not exist":
            status_code = 404

        response = app.response_class(
            response=str(e),
            status=status_code
        )

    return response


@app.route('/songs/<string:filename>', methods=['GET'])
def get_song(filename):
    """ Gets an existing point from the Point Manager """

    try:
        song = song_mgr.get_song(filename)

        response = app.response_class(
            status=200,
            response=json.dumps(song.meta_data()),
            mimetype='application/json'
        )

        return response
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )

        return response


@app.route('/songs/<string:filename>', methods=['DELETE'])
def delete_song(filename):
    """ Delete an existing song from the Song Manager """

    try:
        song_mgr.delete_song(filename)

        response = app.response_class(
            status=200
        )
    except ValueError as e:
        status_code = 400
        if str(e) == "Song does not exist":
            status_code = 404

        response = app.response_class(
            response=str(e),
            status=status_code
        )

    return response


@app.route('/songs/all', methods=['GET'])
def get_all_songs():
    """ Gets all points in the Point Manager """
    songs = song_mgr.get_all_songs()

    song_list = []

    for song in songs:
        song_list.append(song.meta_data())

    response = app.response_class(
        status=200,
        response=json.dumps(song_list),
        mimetype='application/json'
    )

    return response


if __name__ == "__main__":
    app.run()