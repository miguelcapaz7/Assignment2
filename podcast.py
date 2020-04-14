from audio_file import AudioFile
from datetime import datetime, time


class Podcast(AudioFile):
    """Represents a Podcast

    Author: Miguel Capaz
    ID: A01167207"""

    def __init__(self, title: str, artist: str, runtime: str, pathname: str, filename: str, series: str,
                 episode_date: datetime, season: str = None, episode_number: int = None):
        """Constructor that creates podcast instance"""
        super().__init__(title, artist, runtime, pathname, filename)
        if not isinstance(series, str):
            raise ValueError("Series must be entered as a string.")
        else:
            self._series = series
        if not isinstance(episode_date, datetime):
            raise ValueError("Episode Date must be entered as a datetime object.")
        else:
            self._episode_date = episode_date.strftime("%B" " %d")
        if not isinstance(episode_number, int) and episode_number is not None:
            raise ValueError("Episode number must be entered as a number.")
        else:
            self._episode_number = episode_number
        if not isinstance(season, str) and season is not None:
            raise ValueError("Season must be entered as a string.")
        else:
            self._season = season

        self._progress = time(0, 0, 0)

    @property
    def get_series(self) -> str:
        """Returns series value"""
        return self._series

    @get_series.setter
    def get_series(self, series) -> None:
        """Sets series value"""
        self._series = series

    @property
    def get_season(self) -> str:
        """Returns season value"""
        return self._season

    @get_season.setter
    def get_season(self, season) -> None:
        """Sets season value"""
        if type(season) is not str:
            raise ValueError("Season must be a string.")
        self._season = season

    @property
    def get_episode_number(self) -> int:
        """Returns episode_number value"""
        return self._episode_number

    @get_episode_number.setter
    def get_episode_number(self, episode_number) -> None:
        """Sets episode_number value"""
        self._episode_number = episode_number

    def get_description(self) -> str:
        """Returns the description of the podcast as a string. """
        minutes, seconds = self._runtime.split(":")
        rounded_minutes = int(minutes) + round(float(seconds) / 60) # Rounds runtime to nearest minute
        if self._season is not None and self._episode_number is not None:
            podcast_details = "{}: {}, {}, {} Episode {} ({} mins)".format(
                self._series, self._title, self._episode_date, self._season,
                self._episode_number, rounded_minutes)
        elif self._episode_number is None and self._season is not None:
            podcast_details = "{}: {}, {}, {} ({} mins)".format(
                self._series, self._title, self._episode_date, self._season,
                rounded_minutes)
        else:
            podcast_details = "{}: {}, {} ({} mins)".format(
                self._series, self._title, self._episode_date, rounded_minutes)
        return podcast_details

    @property
    def get_progress(self):
        """Returns progress value"""
        return self._progress

    @get_progress.setter
    def get_progress(self, progress):
        """Sets progress value"""
        if type(progress) is time:
            self._progress = progress
        else:
            raise ValueError

    def meta_data(self) -> dict:
        """Returns a dictionary of the song details"""
        podcast_dict = {
            "title": self._title,
            "artist": self._artist,
            "runtime": self._runtime,
            "pathname": self._pathname,
            "filename": self._filename,
            "series": self._series,
            "episode_date": self._episode_date,
            "episode_number": self._episode_number,
            "season": self._season,
            "progress": self._progress,
            "date_added": self._usage.date_added,
            "play_count": self._usage.play_count,
            "last_played": self._usage.last_played,
            "rating": self._rating
        }
        return podcast_dict

