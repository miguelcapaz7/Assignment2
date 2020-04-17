from tkinter import *


class RatingWindow(Frame):

    def __init__(self, parent, controller, title):
        """ Initialize the Rate Song window """
        Frame.__init__(self, parent)
        parent.title('Rate Song')

        self.top_frame = Frame(self.master)
        self.mid_frame = Frame(self.master)
        self.bot_frame = Frame(self.master)
        self.top_frame.grid(row=0, padx=30, pady=10)
        self.mid_frame.grid(row=1, padx=30, pady=10)
        self.bot_frame.grid(row=2, padx=30, pady=10)

        Label(self.mid_frame, text=title).grid(row=0, column=0, sticky=E, padx=5, pady=5)
        Label(self.bot_frame, text='Rating:').grid(row=0, column=0, sticky=E, padx=5, pady=5)

        self._entry1 = Entry(self.bot_frame, width=20)
        self._entry1.grid(row=0, column=1, sticky=W, padx=5, pady=5)

        self.save_button = Button(self.bot_frame, text='Save', width=10)
        self.save_button.grid(row=1, column=1)
        self.save_button.bind("<Button-1>", controller.update_rating)

        self.cancel_button = Button(self.bot_frame, text='Cancel', width=10, command=controller._close_rate_song_popup)
        self.cancel_button.grid(row=3, column=2)

    def get_form_data(self):
        """ Return a dictionary of form field values for this form """
        return {
            "rating": self._entry1.get()
        }

    def clear_form_fields(self):
        """ Clear the name entry box """
        self._entry1.delete(0, END)
