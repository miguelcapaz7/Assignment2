from usage_stats import UsageStats
from datetime import datetime
import os
from abc import abstractmethod


class AudioFile:
    """Represents an AudioFile super class

    Author: Miguel Capaz
    ID: A01167207"""

    def __init__(self, title: str, artist: str, runtime: str, pathname: str, filename: str):
        """This is the constructor which creates an AudioFile superclass"""
        if not isinstance(title, str):
            raise ValueError("Title must be entered as a string.")
        else:
            self._title = title
        if not isinstance(artist, str):
            raise ValueError("Artist must be entered as a string.")
        else:
            self._artist = artist
        if not AudioFile.__validate_runtime(runtime):
            raise TypeError("Runtime must be formatted as 'MM:SS'")
        else:
            self._runtime = runtime
        if not AudioFile.__validate_filepath(pathname, filename):
            raise FileNotFoundError("Pathname not found.")
        else:
            self._pathname = pathname
            self._filename = filename

        self.__validate_AudioFile(self)
        self._rating = ""
        self._usage = UsageStats(datetime.now())

    @abstractmethod
    def get_description(self) -> str:
        pass

    def get_location(self) -> str:
        """Returns the path of the song and the name of the audio file"""
        file_details = "File Path of Song: {} \nFile Name of Song: {}" \
            .format(self._pathname, self._filename)
        return file_details

    @property
    def user_rating(self) -> str:
        """Gets and returns the rating of the song"""
        return self._rating

    @user_rating.setter
    def user_rating(self, rating: int) -> None:
        """Checks if the rating is a number between 0 and 5 and returns it if true.
        Otherwise, an error message is printed"""
        if type(rating) is int and 0 <= rating <= 5:
            self._rating = rating
        else:
            print("Error rating the song. Must be a number between 0 and 5.")

    def get_play_count(self) -> int:
        """Gets the amount of times the song is played and returns the amount"""
        return self._usage.play_count

    def update_usage_stats(self):
        """Play count is incremented by 1"""
        self._usage.increment_usage_stats()

    def get_usage_stats(self) -> UsageStats:
        """Returns the UsageStats class"""
        return self._usage

    @abstractmethod
    def meta_data(self) -> dict:
        pass

    @property
    def get_title(self) -> str:
        """Returns title of audio file"""
        return self._title

    @property
    def get_artist(self) -> str:
        """Returns artist of audio file"""
        return self._artist

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





