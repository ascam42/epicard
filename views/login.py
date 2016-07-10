
"""
" GTK
"""
from    gi.repository   import  Gtk
from    gi.repository   import  GLib

"""
" EpiCard
"""
from net.intra import IntraRetriever

def login(win, threading_local, addit=None):
    win.clear()
    win.set_title(win.BASE_TITLE + " - Connexion")
    __populate_login(win, threading_local, addit)
    win.center()
    win.show_all()


def __submit_login(field, login, passwd, local):
    connecting_label = Gtk.Label("Connexion en cours...")

    local.window.clear()
    local.window.add(connecting_label)
    local.window.show_all()

    # on thread it !!
    print(login)
    print(login.get_text())
    print(login.get_text())
    print(login.get_text() + passwd.get_text())
    connect_thread = local.pool.apply_async(local.intra.ping,
                                            ('/user/', login.get_text(), passwd.get_text()))
    local.processes.append(connect_thread)
    GLib.timeout_add(100, __check_ping_done, (local))
    # connect_thread.start()


def __check_ping_done(local):
    if local.processes[0].ready():
        result = local.processes[0].get()
        if result == True:
            print('ok')
        else:
            print('fail')
            print(result)
            login(local.window, local, addit="Erreur de connexion" +
                    (": " + result if result != False else " zouf"))
        return False
    return True



def __populate_login(win, threading_local, addit=None):
    contain_grid = Gtk.Grid()
    contain_grid.set_row_spacing(10)
    contain_grid.set_column_spacing(10)

    if addit is not None:
        addit_label = Gtk.Label("<b>" + addit + "</b>")
        addit_label.set_use_markup(True)
        contain_grid.attach(addit_label, 0, 0, 3, 1)
    """
        Login input
    """
    login_label = Gtk.Label("Login intranet", xalign=0)
    login_label.set_justify(Gtk.Justification.LEFT)
    login_field = Gtk.Entry()
    # login_field.set_text("logi_n")
    login_field.props.caps_lock_warning = True
    contain_grid.attach(login_label, 0, 1, 1, 1)
    contain_grid.attach(login_field, 1, 1, 2, 1)

    """
        Password input
    """
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

