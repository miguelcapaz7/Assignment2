from tkinter import *


class AddQueueWindow(Frame):

    def __init__(self, parent, controller, titles):
        """ Initialize the Add Queue window """
        Frame.__init__(self, parent)
        parent.title('Add to Queue')

        self.titles = titles

        self.top_frame = Frame(self.master)
        self.bot_frame = Frame(self.master)
        self.top_frame.grid(row=0, padx=30, pady=10)
        self.bot_frame.grid(row=1, padx=30, pady=10)

        Label(self.top_frame, text='Select a song to add to your queue').grid(row=0, column=0)
        self.listbox = Listbox(self.top_frame, width=30, height=10)
        self.listbox.grid(row=1, column=0)

        self.add_songs_to_listbox()

        self.add_button = Button(self.bot_frame, text='Add', width=10, command=controller.add_to_queue_callback) \
            .grid(row=2, column=1, sticky=E, padx=20, pady=5)
        self.back_button = Button(self.bot_frame, text='Back', width=10, command=controller._close_add_queue_popup)
        self.back_button.grid(row=3, column=1)

    def add_songs_to_listbox(self):
        """ Update the listbox to display all titles """
        self.listbox.delete(0, END)
        for title in self.titles:
            self.listbox.insert(END, title)

    def get_index(self):
        """ returns selected song from the listbox """
        return self.listbox.index(ANCHOR)
