from usage_stats import UsageStats
from datetime import datetime
from song import Song


class Playlist:
    """Represents a song playlist that can allow songs to be added,
    removed, or moved into a different position in the playlist"""

    def __init__(self, name: str, description: str):
        """This is the constructor which creates a new playlist instance"""
        if not isinstance(name, str):
            raise ValueError("Playlist name must be a string.")
        else:
            self._name = name
        if not isinstance(description, str):
            raise ValueError("Playlist description must be a string.")
        else:
            self._description = description

        self._playlist = []
        self._usage = UsageStats(datetime.now())

    def add_song(self, song: Song, posn: int = None) -> None:
        """Adds a song to the playlist if it does not already exist in the playlist"""
        if song not in self._playlist:
            if posn is not None:
                if posn <= len(self._playlist):
                    self._playlist.insert(posn - 1, song)
                else:
                    print("Invalid position. Must be a number that is in the range "
                          "of the number of songs in the playlist.")
            else:
                self._playlist.append(song)
        else:
            print("The song already exists in the playlist.")

    def remove_song(self, song: Song) -> None:
        """Removes a song from the playlist if it already exists in the playlist"""
        try:
            self._playlist.remove(song)
        except ValueError:
            print("Song not found. Failed to remove song.")

    def move_song(self, song: Song, posn: int) -> None:
        """Moves the song to a different position in the playlist"""
        if song in self._playlist:
            if posn <= len(self._playlist):
                self._playlist.remove(song)
                self._playlist.insert(posn - 1, song)
            else:
                print("Invalid position. Must be a number that is in the range "
                      "of the number of songs in the playlist")
        else:
            print("Song not found. Failed to move song")

    def list_songs(self) -> list:
        """Returns a list of the song details that exist in the playlist"""
        list_of_songs = []
        for index, value in enumerate(self._playlist):
            song_str = "{}{}{}{}{}".format(str(index + 1) + '. ', value._title.ljust(20),
                                           value._artist.ljust(20), value._album.ljust(20), value._runtime)
            list_of_songs.append(song_str)
        return list_of_songs

    def get_song_by_position(self, posn) -> Song:
        """Returns the song based on the position passeed in"""
        try:
            if type(posn) is int:
                return self._playlist[posn - 1]
            else:
                raise ValueError("The position of the song must be a number.")
        except IndexError:
            print("The position is out of range.")

    def find_song(self, title: str = None, artist: str = None, album: str = None) -> int or None:
        """Returns the position of the song with supplied parameters"""
        if title is not None:
            titles = set([self._playlist.index(song) + 1 for song in self._playlist if song._title == title])
        else:
            titles = set([self._playlist.index(song) + 1 for song in self._playlist])
        if artist is not None:
            artists = set([self._playlist.index(song) + 1 for song in self._playlist if song._artist == artist])
        else:
            artists = set([self._playlist.index(song) + 1 for song in self._playlist])
        if album is not None:
            albums = set([self._playlist.index(song) + 1 for song in self._playlist if song._album == album])
        else:
            albums = set([self._playlist.index(song) + 1 for song in self._playlist])
        intersected_list = list(titles.intersection(artists, albums))
        if len(intersected_list) > 0:
            return intersected_list[0]
        else:
            return None

    def number_of_songs(self) -> int:
        """Returns the number of songs found in the playlist"""
        num_songs = len(self._playlist)
        return num_songs

    def update_usage_stats(self) -> None:
        """Increments play count and last_played"""
        self._usage.increment_usage_stats()

    def get_usage_stats(self) -> UsageStats:
        """Returns usage stats"""
        return self._usage

    @property
    def playlist_name(self) -> str:
        """Gets the playlist name"""
        return self._name

    @playlist_name.setter
    def playlist_name(self, name) -> None:
        """Sets the playlist name"""
        self._name = name

    @property
    def playlist_description(self) -> str:
        """Gets the playlist description"""
        return self._description

    @playlist_description.setter
    def playlist_description(self, description) -> None:
        """Sets the playlist description"""
        self._description = description
