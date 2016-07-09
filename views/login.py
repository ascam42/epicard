
"""
" GTK
"""
from    gi.repository   import  Gtk

"""
" Threading
"""
from    threading       import  Thread

"""
" EpiCard
"""
from net.intra import IntraRetriever

def login(win, threading_local):
    win.set_title(win.BASE_TITLE + " - Connexion")
    __populate_login(win, threading_local)
    win.show_all()


def __submit_login(field, login, passwd, local):
    connecting_label = Gtk.Label("Connecting...")

    local.window.clear()
    local.window.add(connecting_label)
    local.window.show_all()

    # on thread it !!
    connect_thread = Thread(target=local.intra.ping,
                            args=('/user/', login.get_text(), passwd.get_text()))
    local.processes.append(connect_thread)
    connect_thread.start()
    #
    # TODO
    # Any pythonic way to raise an event ON THREAD JOIN ??? 
    # YA KNO, LIKE TO HANDLE EXIT !
    # + how to retieve return data ?
    # or does it needs to be in local data ?


def __populate_login(win, threading_local):
    contain_grid = Gtk.Grid()
    contain_grid.set_row_spacing(10)
    contain_grid.set_column_spacing(10)

    """
        Login input
    """
    login_label = Gtk.Label("Login intranet", xalign=0)
    login_field = Gtk.Entry()
    # login_field.set_text("logi_n")
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
    # passwd_field.set_text("password")
    passwd_field.props.caps_lock_warning = True
    passwd_field.props.visibility = False
    contain_grid.attach(passwd_label, 0, 1, 1, 1)
    contain_grid.attach(passwd_field, 1, 1, 2, 1)

    """
        Submit - Callbacks
    """
    submit_button = Gtk.Button("Connexion")
    submit_button.connect("clicked", __submit_login,
                        login_field, passwd_field, threading_local)
    contain_grid.attach(submit_button, 0, 2, 3, 1)
    passwd_field.connect("activate", __submit_login,
                        login_field, passwd_field, threading_local)

    """
        Packing
    """
    win.add(contain_grid)
    return (contain_grid)

