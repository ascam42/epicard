
"""
" GTK
"""
from    gi.repository   import  Gtk

class EpiCardWin(Gtk.Window):

    __WIN_HEIGHT = 720
    __WIN_WIDTH = 1280

    BASE_TITLE = "EpiCard"


    def __init__(self):
        Gtk.Window.__init__(self, title=self.BASE_TITLE)

        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.connect("delete-event", Gtk.main_quit)


    def full_size(self):
        self.set_default_size(self.__WIN_WIDTH, self.__WIN_HEIGHT)


    def clear(self):
        self.forall(self.remove)
