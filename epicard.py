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
import views
from net.intra import IntraRetriever

if __name__ == '__main__':
    intra = IntraRetriever()
    window = EpiCardWin()

    views.make(window, intra)
    Gtk.main()
