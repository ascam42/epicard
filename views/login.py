
"""
" GTK
"""
from    gi.repository   import  Gtk

"""
" EpiCard
"""
from net.intra import IntraRetriever

def login(win, intra):
    win.set_title(win.BASE_TITLE + " - Connexion")
    __populate_login(win, intra)
    win.show_all()


def __submit_login(field, win, login, passwd, intra):
    win.clear()
    win.show_all()
    intra.auth(login.get_text(), passwd.get_text())
    if intra.ping('/user/') is True:
        print('owi')
    else:
        print('oignon')
    # pass


def __populate_login(win, intra):
    contain_grid = Gtk.Grid()
    contain_grid.set_row_spacing(10)
    contain_grid.set_column_spacing(10)

    """
        Login input
    """
    login_label = Gtk.Label("Login intranet", xalign=0)
    login_field = Gtk.Entry()
    login_field.set_text("logi_n")
    login_field.props.caps_lock_warning = True
    contain_grid.attach(login_label, 0, 0, 1, 1)
    contain_grid.attach(login_field, 1, 0, 2, 1)

    """
        Password input
    """
    passwd_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    passwd_label = Gtk.Label("Pass UNIX", xalign=0)
    passwd_label.set_justify(Gtk.Justification.LEFT)
    passwd_field = Gtk.Entry()
    passwd_field.set_text("password")
    passwd_field.props.caps_lock_warning = True
    passwd_field.props.visibility = False
    contain_grid.attach(passwd_label, 0, 1, 1, 1)
    contain_grid.attach(passwd_field, 1, 1, 2, 1)

    """
        Submit - Callbacks
    """
    submit_button = Gtk.Button("Connexion")
    submit_button.connect("clicked", __submit_login,
                        win, login_field, passwd_field, intra)
    contain_grid.attach(submit_button, 0, 2, 3, 1)
    passwd_field.connect("activate", __submit_login,
                        win, login_field, passwd_field, intra)

    """
        Packing
    """
    win.add(contain_grid)
    return (contain_grid)

