#!/usr/bin/env python3

"""
" GTK
"""
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import  Gtk

"""
" EpiCard
"""
from win import  *
import threading
import views
from net.intra import IntraRetriever

if __name__ == '__main__':
    local = threading.local()
    local.intra = IntraRetriever()
    local.window = EpiCardWin()
    local.processes = []

    views.make(local)
    Gtk.main()

    for proc in local.processes:
        proc.join()
