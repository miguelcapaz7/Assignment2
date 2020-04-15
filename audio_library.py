from song import Song
import os
import eyed3


class AudioLibrary:
    """Represents an AudioLibrary

    Author: Miguel Capaz, Bryan Campos, Anthony Raymundo
    """

    def __init__(self):
        """This is the constructor which creates an AudioLibrary class"""
        self._songs = []
        self.titles = []

    def add_song(self, song: Song):
        """Adds a song to the list of songs in the library."""
        if song not in self._songs:
            self._songs.append(song)
            self.titles.append(song.title)
        else:
            raise ValueError("Error: The song already exists in the library. Failed to"
                             " add song.")

    def remove_song(self, song: Song):
        """Removes a song from the list of songs in the library"""
        if song in self._songs:
            self._songs.remove(song)
            self.titles.remove(song.title)
        else:
            raise ValueError("Error: The song does not exist in the library. Failed to"
                             " remove song.")

    def get_song(self, title) -> Song:
        """Gets a single song object from the title"""
        for song in self._songs:
            if title == song.title:
                return song

    def get_songs(self) -> list:
        """Returns the list of songs in the library"""
        return self._songs

    def load(self, path):
        """Creates a song object for each mp3 in the directory. These objects
        are appended to the songs list."""
        if os.path.exists(path):
            mp3_files = os.listdir(path)
            for file in mp3_files:
                if file.endswith('.mp3'):
                    mp3_file = eyed3.load(os.path.join(path, file))
                    runtime = mp3_file.info.time_secs
                    mins = int(runtime // 60)
                    secs = int(runtime % 60)
                    song = Song(str(getattr(mp3_file.tag, 'title')), str(getattr(mp3_file.tag, 'artist')),
                                '{}:{}'.format(mins, secs), '{}'.format(path),
                                '\\{}'.format(file), str(getattr(mp3_file.tag, 'album')),
                                str(getattr(mp3_file.tag, 'genre')))
                    self.add_song(song)  # adds song to songs list
        else:
            raise FileNotFoundError("Path not found.")




