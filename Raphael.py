#!/usr/bin/env python
import gtk, webkit

#Raphael
class Doge():

    def __init__(self):
        #Create window
        self.much_window = gtk.Window()
        self.much_window.connect('destroy', lambda w: gtk.main_quit())
        self.much_window.fullscreen()

        self.much_window.set_title('Raphael')

        # Create view for webpage
        self.very_view = gtk.ScrolledWindow()
        self.such_webview = webkit.WebView()
        self.such_webview.open('http://192.168.43.212/3.html')
        self.very_view.add(self.such_webview)

        # Add everything and initialize
        self.raphael_container = gtk.VBox()
        self.raphael_container.pack_start(self.very_view)
        self.much_window.add(self.raphael_container)

        self.much_window.show_all()
        gtk.main()

wow = Doge()