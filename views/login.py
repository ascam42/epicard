
"""
" GTK
"""
from    gi.repository   import  Gtk
from    gi.repository   import  GLib

"""
" Threading
"""
from    threading       import  Thread

"""
" EpiCard
"""
from net.intra import IntraRetriever

def login(win, threading_local, addit=None):
    win.set_title(win.BASE_TITLE + " - Connexion")
    __populate_login(win, threading_local, addit)
    win.show_all()


def __submit_login(field, login, passwd, local):
    connecting_label = Gtk.Label("Connexion en cours...")

    local.window.clear()
    local.window.add(connecting_label)
    local.window.show_all()

    # on thread it !!
    connect_thread = local.pool.apply_async(local.intra.ping,
                                            ('/user/', login.get_text(), passwd.get_text()))
    local.processes.append(connect_thread)
    GLib.timeout_add(100, __check_ping_done, (local))
    # connect_thread.start()


def __check_ping_done(local):
    if local.processes[0].ready():
        if local.processes[0].get() == True:
            print('ready')
        else:
            login(local.window, local, addit="Erreur de connexioErreur de connexionn")
        return False
    print('connecting...')
    return True



def __populate_login(win, threading_local, addit=None):
    contain_grid = Gtk.Grid()
    contain_grid.set_row_spacing(10)
    contain_grid.set_column_spacing(10)

    if addit is not None:
        addit_label = Gtk.Label(addit)
        contain_grid.attach(addit_label, 0, 0, 3, 1)
    """
        Login input
    """
    login_label = Gtk.Label("Login intranet", xalign=0)
    login_field = Gtk.Entry()
    # login_field.set_text("logi_n")
    login_field.props.caps_lock_warning = True
    contain_grid.attach(login_label, 0, 1, 1, 1)
    contain_grid.attach(login_field, 1, 1, 2, 1)

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
    contain_grid.attach(passwd_label, 0, 2, 1, 1)
    contain_grid.attach(passwd_field, 1, 2, 2, 1)

    """
        Submit - Callbacks
    """
    submit_button = Gtk.Button("Connexion")
    submit_button.connect("clicked", __submit_login,
                        login_field, passwd_field, threading_local)
    contain_grid.attach(submit_button, 0, 3, 3, 1)
    passwd_field.connect("activate", __submit_login,
                        login_field, passwd_field, threading_local)

    """
        Packing
    """
    win.add(contain_grid)
    return (contain_grid)

