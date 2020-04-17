from tkinter import *
import os


class MainWindow(Frame):
    """ Layout for the Player Window """

    def __init__(self, parent, controller):
        """ Initialize Main Application """
        Frame.__init__(self, parent)

        # 1: create any instances of other support classes that are needed

        # Window attributes
        parent.title('Audio Player')

        # Menus
        menu = Menu(master=parent)
        parent.config(menu=menu)
        file_menu = Menu(menu)
        menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Quit', command=controller.quit_callback)

        # Defining frames
        top_frame = Frame(master=parent)
        top_frame.grid(row=0, padx=30, pady=10)
        mid_frame = Frame(master=parent)
        mid_frame.grid(row=1, padx=30, pady=10)
        bot_frame = Frame(master=parent)
        bot_frame.grid(row=2, padx=30, pady=10)
        right_frame = Frame(master=parent)
        right_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10)
        bot_right_frame = Frame(master=parent)
        bot_right_frame.grid(row=2, column=1, padx=10, pady=10)

        # Labels
        Label(mid_frame, text='Song:').grid(row=0, column=0, sticky=E, padx=5, pady=5)
        self.song_playing = Label(mid_frame, text='')
        self.song_playing.grid(row=0, column=1, sticky=W, padx=5, pady=5)

        Label(mid_frame, text='State:').grid(row=1, column=0, sticky=E, padx=5, pady=5)
        self.state_value = Label(mid_frame, text='Not Playing')
        self.state_value.grid(row=1, column=1, sticky=W, padx=5, pady=5)

        # Listbox
        self.list_box = Listbox(right_frame, width=30, height=10)
        self.list_box.grid(row=0, column=0)
        # Might want to call listbox here

        # Scrollbar
        scrollbar = Scrollbar(right_frame, orient="vertical", width=20)
        scrollbar.config(command=self.list_box.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        self.list_box.config(yscrollcommand=scrollbar.set)

        # Main buttons

        Button(top_frame, text='Add a Song', width=10, command=controller.open_mp3_file) \
            .grid(row=2, column=1, sticky=E, padx=20, pady=5)

        Button(bot_frame, text='Play', width=10, command=controller.play_callback) \
            .grid(row=0, column=0, sticky=E, padx=10, pady=5)
        #
        Button(bot_frame, text='Stop', width=10, command=controller.stop_callback) \
            .grid(row=0, column=1, sticky=E, padx=10, pady=5)
        #
        Button(bot_frame, text='Pause', width=10, command=controller.pause_callback) \
            .grid(row=0, column=2, sticky=E, padx=10, pady=5)

        Button(bot_frame, text='Resume', width=10, command=controller.resume_callback) \
            .grid(row=0, column=3, sticky=E, padx=10, pady=5)

        # Buttons under listbox
        Button(bot_right_frame, text='Rate Song', width=10, command=controller.rate_song_popup) \
            .grid(row=3, column=1, sticky=E, padx=20, pady=5)

        Button(bot_right_frame, text='Delete', width=10, command=controller.delete_callback) \
            .grid(row=4, column=1, sticky=E, padx=20, pady=5)

    def add_titles_to_listbox(self, titles):
        """ Update the listbox to display all titles """
        self.list_box.delete(0, END)
        for title in titles:
            self.list_box.insert(END, title)

    def get_index(self):
        """ returns selected song from the listbox """
        return self.list_box.index(ANCHOR)
