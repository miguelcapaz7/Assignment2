from flask import Flask, request
from song import Song
from song_manager import SongManager
import json

app = Flask(__name__)

SONGS_DB = 'songs.sqlite'

song_mgr = SongManager(SONGS_DB)


@app.route('/songs', methods=['POST'])
def add_song():
    """ Adds a point to the Grid """
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


# @app.route('/songs/<int:song_id>', methods=['PUT'])
# def update_song(song_id):
#     """ Updates an existing point in the Point Manager """
#     content = request.json
#
#     if song_id <= 0:
#         response = app.response_class(
#             status=400
#         )
#         return response
#
#     try:
#         song = Song(content['x'], content['y'])
#         song.id = song_id
#         song_mgr.update_song(song)
#
#         response = app.response_class(
#             status=200
#         )
#     except ValueError as e:
#         status_code = 400
#         if str(e) == "Point does not exist":
#             status_code = 404
#
#         response = app.response_class(
#             response=str(e),
#             status=status_code
#         )
#
#     return response
#
#
# @app.route('/points/<int:point_id>', methods=['GET'])
# def get_song(song_id):
#     """ Gets an existing point from the Point Manager """
#
#     if song_id <= 0:
#         response = app.response_class(
#             status=400
#         )
#         return response
#
#     try:
#         song = song_mgr.get_song(song_id)
#
#         response = app.response_class(
#             status=200,
#             response=json.dumps(song.to_dict()),
#             mimetype='application/json'
#         )
#
#         return response
#     except ValueError as e:
#         response = app.response_class(
#             response=str(e),
#             status=400
#         )
#
#         return response
#
#
# @app.route('/points/<int:point_id>', methods=['DELETE'])
# def delete_song(song_id):
#     """ Delete an existing point from the Point Manager """
#
#     if song_id <= 0:
#         response = app.response_class(
#             status=400
#         )
#         return response
#
#     try:
#         song_mgr.delete_song(song_id)
#
#         response = app.response_class(
#             status=200
#         )
#     except ValueError as e:
#         status_code = 400
#         if str(e) == "Point does not exist":
#             status_code = 404
#
#         response = app.response_class(
#             response=str(e),
#             status=status_code
#         )
#
#     return response
#
#
# @app.route('/points/all', methods=['GET'])
# def get_all_songs():
#     """ Gets all points in the Point Manager """
#     songs = song_mgr.get_all_songs()
#
#     song_list = []
#
#     for song in songs:
#         song_list.append(song.to_dict())
#
#     response = app.response_class(
#         status=200,
#         response=json.dumps(song_list),
#         mimetype='application/json'
#     )
#
#     return response


if __name__ == "__main__":
    app.run()