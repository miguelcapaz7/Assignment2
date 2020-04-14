from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from song import Song
from sqlalchemy.ext.declarative import declarative_base


class SongManager:

    def __init__(self, song_db):
        """ Creates a Song object and map to the Database """

        if song_db is None or song_db == "":
            raise ValueError(f"Song database [{song_db}] not found")

        engine = create_engine('sqlite:///' + song_db)
        Base = declarative_base()
        Base.metadata.bind = engine
        self._db_session = sessionmaker(bind=engine)

    def add_song(self, new_song: Song):
        """ Adds a new song to the song database """

        if new_song is None or not isinstance(new_song, Song):
            raise ValueError("Invalid Student Object")

        session = self._db_session()
        session.add(new_song)

        session.commit()

        song_id = new_song.song_id
        session.close()

        return song_id

    def delete_song(self, song_id):
        """ Delete a song from the database """
        if song_id is None or type(song_id) != str:
            raise ValueError("Invalid Song ID")

        session = self._db_session()

        song = session.query(Song).filter(
                Song.song_id == song_id).first()
        if song is None:
            session.close()
            raise ValueError("Song does not exist")

        session.delete(song)
        session.commit()

        session.close()

    def update_song(self, song):
        """ Updates an existing point """

        if song is None or not isinstance(song, Song):
            raise ValueError("Invalid Song Object")

        session = self._db_session()

        existing_point = session.query(Song).filter(
            Song.id == song.id).first()
        if existing_point is None:
            raise ValueError("Point does not exist")
        existing_point.copy(song)
        session.commit()
        session.close()

    def get_song(self, song_id):
        """ Return student object matching ID"""
        if song_id is None or type(song_id) != str:
            raise ValueError("Invalid Song ID")

        session = self._db_session()

        student = session.query(Song).filter(
                Song.song_id == song_id).first()

        session.close()

        return student

    def get_all_songs(self):
        """ Return a list of all songs in the DB """
        session = self._db_session()

        all_songs = session.query(Song).all()

        session.close()

        return all_songs
