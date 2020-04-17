from song import Song
import vlc
import os
import eyed3
import requests
from tkinter import *
from tkinter import filedialog
from main_window import MainWindow


class MainController(Frame):
    """
    Controller for our views
    """

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self._root_win = Toplevel()
        self._main_window = MainWindow(self._root_win, self)
        self._vlc_instance = vlc.Instance()
        self._player = self._vlc_instance.media_player_new()
        self.list_songs_callback()

    def list_songs_callback(self):
        """ Lists song titles in listbox. """
        response = requests.get("http://localhost:5000/songs/all")
        song_list = response.json()
        song_title_list = []
        for song in song_list:
            song_title_list.append(song['title'])
        self._main_window.add_titles_to_listbox(song_title_list)

    def play_callback(self):
        """Play a song specified by number. """
        index = self._main_window.get_index()
        response = requests.get("http://localhost:5000/songs/all")
        song_list = response.json()
        song = song_list[index]
        media_file = song['pathname'] + song['filename']
        if self._player.get_state() == vlc.State.Playing:
            self._player.stop()
        media = self._vlc_instance.media_new_path(media_file)
        self._player.set_media(media)
        self._player.play()

    def pause_callback(self):
        """ Pause the player """
        if self._player.get_state() == vlc.State.Playing:
            self._player.pause()

    def resume_callback(self):
        """ Resume playing """
        if self._player.get_state() == vlc.State.Paused:
            self._player.pause()

    def stop_callback(self):
        """ Stop the player """
        self._player.stop()

    def quit_callback(self):
        """ Exit the application. """
        self.master.quit()

    def open_mp3_file(self):
        """ Load the file name selected"""
        abs_path = filedialog.askopenfilename(initialdir='.\\Music\\')
        path = os.getcwd() + "\\Music\\"
        file = os.path.basename(abs_path)
        if file.endswith('.mp3'):
            mp3_file = eyed3.load(os.path.join(path, file))
            runtime = mp3_file.info.time_secs
            mins = int(runtime // 60)
            secs = int(runtime % 60)
            song = Song(str(getattr(mp3_file.tag, 'title')), str(getattr(mp3_file.tag, 'artist')),
                        '{}:{}'.format(mins, secs), '{}'.format(path),
                        '\\{}'.format(file), str(getattr(mp3_file.tag, 'album')),
                        str(getattr(mp3_file.tag, 'genre')))
            self.add_callback(song)

    def add_callback(self, song):
        """ Add audio file. """
        data = {'title': song.title,
                'artist': song.artist,
                'runtime': song.runtime,
                'pathname': song.pathname,
                'filename': song.filename,
                'album': song.album,
                'genre': song.genre
                }

        response = requests.post("http://localhost:5000/songs", json=data)
        if response.status_code == 200:
            # msg_str = f"{form_data.get('title')} added to the database"
            # messagebox.showinfo(title='Add Song', message=msg_str)
            self.list_songs_callback()

    def delete_callback(self):
        """ Deletes selected song. """
        index = self._main_window.get_index()
        get_response = requests.get("http://localhost:5000/songs/all")
        song_list = get_response.json()
        song = song_list[index]
        filename = song['filename']
        del_response = requests.delete("http://localhost:5000/songs/" + str(filename))

        if del_response.status_code == 200:
            # msg_str = f'{selected_title} has been deleted'
            # messagebox.showinfo(title='Delete Song', message=msg_str)
            self.list_songs_callback()


if __name__ == "__main__":
    """ Create Tk window manager and a main window. Start the main loop """
    root = Tk()
    MainController(root).pack()
    mainloop()