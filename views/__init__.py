
"""
" EpiCard views
"""
from views.login import *
from views.menu import *

def make(threading_local):
    login(threading_local.window, threading_local)
    # menu(win)
