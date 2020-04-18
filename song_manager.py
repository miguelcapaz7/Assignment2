from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from song import Song
from base import Base
from datetime import datetime


class SongManager:

    def __init__(self, song_db):
        """ Creates a Song object and map to the Database """

        if song_db is None or song_db == "":
            raise ValueError(f"Song database [{song_db}] not found")

        engine = create_engine('sqlite:///' + song_db)
        Base.metadata.bind = engine
        self._db_session = sessionmaker(bind=engine)

    def add_song(self, new_song: Song):
        """ Adds a new song to the song database """

        if new_song is None or not isinstance(new_song, Song):
            raise ValueError("Invalid Song Object")

        for song in self.get_all_songs():
            if new_song.title == song.title and new_song.artist == song.artist:
                raise ValueError("Song already exists")

        session = self._db_session()
        session.add(new_song)

        session.commit()

        song_id = new_song.title + " has been added"
        session.close()

        return song_id

    def delete_song(self, filename):
        """ Delete a song from the database """
        if filename is None or type(filename) != str:
            raise ValueError("Invalid Filename")

        session = self._db_session()

        for song in self.get_all_songs():
            if song is None:
                session.close()
                raise ValueError("Song does not exist")

            if filename == song.filename:
                session.delete(song)
                session.commit()

                session.close()

    def update_song(self, song):
        """ Updates the rating of the song """

        if song is None or not isinstance(song, Song):
            raise ValueError("Invalid Song Object")

        session = self._db_session()

        existing_song = session.query(Song).filter(
            Song.id == song.id).first()
        if existing_song is None:
            raise ValueError("Song does not exist")
        existing_song.update_rating(song)
        session.commit()
        session.close()

    def update_stats(self, song):
        """ Updates the play_count and last_played song """

        if song is None or not isinstance(song, Song):
            raise ValueError("Invalid Song Object")

        session = self._db_session()

        existing_song = session.query(Song).filter(
            Song.id == song.id).first()
        if existing_song is None:
            raise ValueError("Song does not exist")
        existing_song.play_count += 1
        existing_song.last_played = datetime.now().strftime(existing_song._DATE_FORMAT)
        session.commit()
        session.close()

    def get_song(self, filename):
        """ Return song object matching ID"""
        if filename is None or type(filename) != str:
            raise ValueError("Invalid Filename")

        session = self._db_session()

        for song in self.get_all_songs():
            if filename == song.filename:
                session.close()
                return song

    def get_all_songs(self):
        """ Return a list of all songs in the DB """
        session = self._db_session()

        all_songs = session.query(Song).all()

        session.close()

        return all_songs


