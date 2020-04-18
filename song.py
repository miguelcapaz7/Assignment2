from audio_file import AudioFile
from sqlalchemy import Column, Text


class Song(AudioFile):
    """Represents a song track that is a subclass of AudioFile

    Author: Miguel Capaz
    ID: A01167207"""

    """ ORM: map db columns to instance variables in this class """

    album = Column(Text)
    genre = Column(Text)

    def __init__(self, title: str, artist: str, runtime: str, pathname: str, filename: str,
                 album: str, genre: str = None):
        """This is the constructor that creates a song subclass instance"""
        super().__init__(title, artist, runtime, pathname, filename)
        if not isinstance(album, str):
            raise ValueError("Album must be entered as a string.")
        else:
            self.album = album
        if genre is not None:
            if not isinstance(genre, str):
                raise ValueError("Genre must be entered as a string.")

        self.genre = genre

    def get_description(self) -> str:
        """Returns the description of the song as a string. """
        song_details = "{} by {} from the album {} added on {}. Runtime is {}." \
            .format(self.title, self.artist, self.album, self.date_added, self.runtime)
        if self.last_played is not None and self.rating is not None:
            song_details += " Last played on {}. User rating is {}/5." \
                .format(self.last_played, self.rating)
        if self.last_played is not None and self.rating is None:
            song_details += " Last played on {}." \
                .format(self.last_played)
        if self.genre is not None:
            song_details += f" Genre of Song: {self.genre}"
        return song_details

    def update_rating(self, song):
        """Sets the updated values of the song"""
        self.user_rating = song.rating
        if self.user_rating == ValueError:
            raise ValueError("Error rating the song. Must be a number between 0 and 5.")

    def meta_data(self) -> dict:
        """Returns a dictionary of the song details"""
        song_dict = {
            "title": self.title,
            "artist": self.artist,
            "album": self.album,
            "date_added": self.date_added,
            "runtime": self.runtime,
            "pathname": self.pathname,
            "filename": self.filename,
            "play_count": self.play_count,
            "last_played": self.last_played,
            "rating": self.rating,
            "genre": self.genre
        }
        return song_dict

