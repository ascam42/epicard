#!/usr/bin/env python3

"""
" GTK
"""
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import  Gtk

"""
" Threading
"""
import threading
from threading import Thread
from multiprocessing.pool import ThreadPool

"""
" EpiCard
"""
from win import  *
import views
from net.intra import IntraRetriever

if __name__ == '__main__':
    local = threading.local()
    local.pool = ThreadPool()
    local.intra = IntraRetriever()
    local.window = EpiCardWin()
    local.processes = []
    # intra = IntraRetriever()
    # window = EpiCardWin()
    # processes = []

    try:
        views.make(local)
        Gtk.main()
    except TypeError as err:
        print(err.__traceback__ + err.__cause__)

    # not anymore if in TreadPool (so greatm handling itself, much love)
    # for proc in local.processes:
        # proc.join()
