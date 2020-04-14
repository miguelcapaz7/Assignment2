from audio_file import AudioFile
from usage_stats import UsageStats
from datetime import datetime


class Song(AudioFile):
    """Represents a song track that is a subclass of AudioFile

    Author: Miguel Capaz
    ID: A01167207"""

    def __init__(self, title: str, artist: str, runtime: str, pathname: str, filename: str,
                 album: str, genre: str = None):
        """This is the constructor that creates a song subclass instance"""
        super().__init__(title, artist, runtime, pathname, filename)
        if not isinstance(album, str):
            raise ValueError("Album must be entered as a string.")
        else:
            self._album = album
        if genre is not None:
            if not isinstance(genre, str):
                raise ValueError("Genre must be entered as a string.")

        self._genre = []
        self._usage = UsageStats(datetime.now())
        if genre is not None:
            self._genre.append(genre)

    def add_genre(self, genre):
        """Adds a genre to a song"""
        if genre not in self._genre:
            self._genre.append(genre)
        else:
            print(genre, "is already included.")

    def get_description(self) -> str:
        """Returns the description of the song as a string. """
        song_details = "{} by {} from the album {} added on {}. Runtime is {}." \
            .format(self._title, self._artist, self._album, self._usage.date_added, self._runtime)
        if self._usage.last_played is not None and self._rating != "":
            song_details += " Last played on {}. User rating is {}/5." \
                .format(self._usage.last_played, self._rating)
        if self._usage.last_played is not None and self._rating == "":
            song_details += " Last played on {}." \
                .format(self._usage.last_played)
        if len(self._genre) > 0:
            song_details += f" Genres of Song: {', '.join(self._genre)}"
        return song_details

    def meta_data(self) -> dict:
        """Returns a dictionary of the song details"""
        song_dict = {
            "title": self._title,
            "artist": self._artist,
            "album": self._album,
            "date_added": self._usage.date_added,
            "runtime": self._runtime,
            "pathname": self._pathname,
            "filename": self._filename,
            "play_count": self._usage.play_count,
            "last_played": self._usage.last_played,
            "rating": self._rating,
            "genre": self._genre
        }
        return song_dict

