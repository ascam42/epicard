
"""
" GTK
"""
from    gi.repository   import  Gtk

def login(win):
    win.set_title(win.BASE_TITLE + " - Connexion")
    __populate_login(win)
    win.show_all()

def __submit_login(field, login, passwd, autologin):
    pass

def __populate_login(win):
    contain_grid = Gtk.Grid()
    contain_grid.set_row_spacing(10)
    contain_grid.set_column_spacing(10)

    """
        Login input
    """
    login_label = Gtk.Label("Login intranet")
    login_field = Gtk.Entry()
    login_field.set_text("logi_n")
    login_field.props.caps_lock_warning = True
    contain_grid.attach(login_label, 0, 0, 1, 1)
    contain_grid.attach(login_field, 1, 0, 2, 1)

    """
        Password input
    """
    passwd_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    passwd_label = Gtk.Label("Pass UNIX")
    passwd_field = Gtk.Entry()
    passwd_field.set_text("password")
    passwd_field.props.caps_lock_warning = True
    passwd_field.props.visibility = False
    contain_grid.attach(passwd_label, 0, 1, 1, 1)
    contain_grid.attach(passwd_field, 1, 1, 2, 1)

    or_label = Gtk.Label("Ou")
    contain_grid.attach(or_label, 0, 2, 3, 1)

    """
        Autologin link input
    """
    autologin_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    autologin_label = Gtk.Label("Lien autologin")
    autologin_field = Gtk.Entry()
    autologin_field.set_text("http://intra.epitech.eu/logi_n-autologin")
    contain_grid.attach(autologin_label, 0, 3, 1, 1)
    contain_grid.attach(autologin_field, 1, 3, 2, 1)

    """
        Submit - Callbacks
    """
    submit_button = Gtk.Button("Connexion")
    submit_button.connect("clicked", __submit_login,
                        login_field, passwd_field, autologin_field)
    contain_grid.attach(submit_button, 0, 4, 3, 1)
    login_field.connect("activate", __submit_login,
                        login_field, passwd_field, autologin_field)
    passwd_field.connect("activate", __submit_login,
                         login_field, passwd_field, autologin_field)
    autologin_field.connect("activate", __submit_login,
                            login_field, passwd_field, autologin_field)

    """
        Packing
    """
    win.add(contain_grid)

