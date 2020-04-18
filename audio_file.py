import os
from abc import abstractmethod
from base import Base
from sqlalchemy import Column, Text, Integer
from datetime import datetime


class AudioFile(Base):
    """Represents an AudioFile super class

    Author: Miguel Capaz
    ID: A01167207"""

    __tablename__ = "Song"
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    artist = Column(Text, nullable=False)
    runtime = Column(Text)
    pathname = Column(Text, nullable=False)
    filename = Column(Text, nullable=False)
    date_added = Column(Text, nullable=False)
    last_played = Column(Text)
    play_count = Column(Integer, nullable=False)
    rating = Column(Integer)

    _DATE_FORMAT = "%Y-%m-%d"

    def __init__(self, title: str, artist: str, runtime: str, pathname: str, filename: str):
        """This is the constructor which creates an AudioFile superclass"""
        if not isinstance(title, str):
            raise ValueError("Title must be entered as a string.")
        else:
            self.title = title
        if not isinstance(artist, str):
            raise ValueError("Artist must be entered as a string.")
        else:
            self.artist = artist
        if not AudioFile.__validate_runtime(runtime):
            raise TypeError("Runtime must be formatted as 'MM:SS'")
        else:
            self.runtime = runtime
        if not AudioFile.__validate_filepath(pathname, filename):
            raise FileNotFoundError("Pathname not found.")
        else:
            self.pathname = pathname
            self.filename = filename
        if AudioFile.__valid_datetime(datetime.now()):
            self.date_added = datetime.now().strftime(AudioFile._DATE_FORMAT)
        else:
            raise ValueError("date_added must be a datetime object")

        self.__validate_AudioFile(self)
        self.rating = None
        self.play_count = 0
        self.last_played = None

    @abstractmethod
    def get_description(self) -> str:
        pass

    def get_location(self) -> str:
        """Returns the path of the song and the name of the audio file"""
        file_path = "{}{}".format(self.pathname, self.filename)
        return file_path

    @property
    def user_rating(self) -> str:
        """Gets and returns the rating of the song"""
        return self.rating

    @user_rating.setter
    def user_rating(self, rating: int) -> None:
        """Checks if the rating is a number between 0 and 5 and returns it if true.
        Otherwise, an error message is printed"""
        if type(rating) is int and 0 <= rating <= 5:
            self.rating = rating
        else:
            raise ValueError("Error rating the song. Must be a number between 0 and 5.")

    def get_play_count(self) -> int:
        """Gets the amount of times the song is played and returns the amount"""
        return self.play_count

    def update_play_count(self):
        """ update the play count and last played time when a song is played """
        self.play_count += 1
        self.last_played = datetime.now()

    @property
    def get_last_played(self):
        """ return the date the song or playlist was last played """
        if self.last_played is None:
            return None
        else:
            return self.last_played.strftime(AudioFile._DATE_FORMAT)

    @abstractmethod
    def meta_data(self) -> dict:
        pass

    @property
    def get_title(self) -> str:
        """Returns title of audio file"""
        return self.title

    @property
    def get_artist(self) -> str:
        """Returns artist of audio file"""
        return self.artist

    @classmethod
    def __validate_runtime(cls, runtime):
        """Checks is runtime can be formatted into datetime"""
        try:
            datetime.strptime(runtime, "%M:%S")
            return True
        except ValueError:
            return False

    @classmethod
    def __validate_filepath(cls, pathname, filename) -> bool:
        """Validates that the path exists"""
        if os.path.exists(pathname + filename):
            return True
        else:
            return False

    @staticmethod
    def __validate_AudioFile(self):
        if type(self) == AudioFile:
            raise TypeError("Error: Cannot create super class objects.")

    @classmethod
    def __valid_datetime(cls, date):
        """ private method to validate the date is datetime object """
        if type(date) is not datetime:
            return False
        else:
            return True






