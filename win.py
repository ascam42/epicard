
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

        # self.set_default_size(self.__WIN_WIDTH, self.__WIN_HEIGHT)
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.connect("delete-event", Gtk.main_quit)




    # def fill(self):
        # outbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        # listbox = Gtk.ListBox()
        # row = Gtk.ListBoxRow()
        # hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        # vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        # label1 = Gtk.Label("Automatic date and Time", xalign=0)
        # label2 = Gtk.Label("Requires internet access", xalign=0)
        # switch = Gtk.Switch()

        # listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        # outbox.pack_start(listbox, True, True, 0)

        # vbox.pack_start(label1, True, True, 0)
        # vbox.pack_start(label2)
        # hbox.pack_start(vbox, True, True, 0)
        # switch.props.valign = Gtk.Align.CENTER
        # hbox.pack_start(switch, False, True, 0)
        # row.add(hbox)

        # listbox.add(row)

        # self.add(outbox)



