from song import Song
from playlist import Playlist
from podcast import Podcast


class AudioLibrary:
    """Represents an AudioLibrary

    Author: Miguel Capaz, Bryan Campos, Anthony Raymundo
    """

    def __init__(self, name: str):
        """This is the constructor which creates an AudioLibrary class"""
        if not isinstance(name, str):
            raise ValueError("Error: Library name must be a string.")
        else:
            self._name = name

        self._songs = []
        self._podcasts = []
        self._playlists = []

    def add_song(self, song: Song):
        """Adds a song to the list of songs in the library."""
        if song not in self._songs:
            self._songs.append(song)
        else:
            raise ValueError("Error: The song already exists in the library. Failed to"
                             " add song.")

    def remove_song(self, song: Song):
        """Removes a song from the list of songs in the library"""
        if song in self._songs:
            self._songs.remove(song)
        else:
            raise ValueError("Error: The song does not exist in the library. Failed to"
                             " remove song.")

    def add_playlist(self, playlist: Playlist):
        """Adds a playlist to the list of playlists in the library"""
        if playlist not in self._playlists:
            self._playlists.append(playlist)
        else:
            raise ValueError("Error: The playlist already exists in the library. Failed to"
                             " add playlist.")

    def remove_playlist(self, playlist: Playlist):
        """Removes a playlist from the list of playlists in the library"""
        if playlist in self._playlists:
            self._playlists.remove(playlist)
        else:
            raise ValueError("Error: The playlist does not exist in the library. Failed to"
                             " remove playlist.")

    def add_podcast(self, podcast: Podcast):
        """Adds a podcast to the list of podcasts in the library"""
        if podcast not in self._podcasts:
            self._podcasts.append(podcast)
        else:
            raise ValueError(("Error: The podcast already exists in the library. Failed to"
                             " add podcast."))

    def remove_podcast(self, podcast: Podcast):
        """Removes a podcast from the list of podcasts in the library"""
        if podcast in self._podcasts:
            self._podcasts.remove(podcast)
        else:
            raise ValueError(("Error: The podcast does not exist in the library. Failed to"
                             " remove podcast."))

    def create_playlist_from_song(self, song: Song, playlist_name: str, playlist_description: str) -> Playlist:
        """Creates a playlist with a song provided. """
        if isinstance(song, Song):
            if song not in self._songs:
                self.add_song(song)
            playlist = Playlist(playlist_name, playlist_description)
            playlist.add_song(song)
            self.add_playlist(playlist)
            return playlist
        else:
            raise ValueError(("Error: First parameter is not Song object. Failed to create playlist "
                              "from song."))

    def get_playlist(self, playlist_name: str) -> Playlist:
        """Gets the specific playlist object that is searched by playlist name."""
        if type(playlist_name) == str:
            for playlist in self._playlists:
                if playlist_name == playlist._name:
                    return playlist
                else:
                    print("Playlist does not exist.")
        else:
            raise ValueError("Wrong value type for playlist_name, please write a string!")

    def get_songs(self) -> list:
        """Returns the list of songs in the library"""
        return self._songs

    def get_playlists(self) -> list:
        """Returns the list of playlists in the library"""
        return self._playlists

    def get_podcasts(self) -> list:
        """Returns the list of podcasts in the library"""
        return self._podcasts






