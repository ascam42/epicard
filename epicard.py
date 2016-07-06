#!/usr/bin/env python3

"""
" GTK
"""
import                          gi
gi.require_version('Gtk', '3.0')
from    gi.repository   import  Gtk

"""
" EpiCard
"""
from    win             import  *
import                          views

if __name__ == '__main__':
    window = EpiCardWin()

    views.make(window)
    Gtk.main()
