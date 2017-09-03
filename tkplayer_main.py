#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import subprocess
import os

class TkMplayer:
    proc = None
    wid = 0
    fifoName = None

    def start(self):
        self.proc = subprocess.Popen('mplayer -quiet -wid %d -slave -input file=%s video.mp4' %
                                     (self.wid, self.fifoName),
                                     shell=True)
        print "start"
        
    def pause(self):
        fw = open(self.fifoName, "w")
        fw.write('pause\n')
        print "toggle pause"
        fw.close()

    def quitPlayer(self):
        fw = open(self.fifoName, "w")
        fw.write('quit\n')
        print "stop playing"
        fw.close()

    def __init__(self):
        self.fifoName = "tmp_mplayer_command" 
        os.mkfifo(self.fifoName)
        root = Tk()
        termf = Frame(root, height=400, width=500)
        buttons = Frame(root, height=50, width=500)
        b1 =Button(buttons, text="pause", command=self.pause)
        b1.pack(fill=BOTH, expand=YES)
        b2 = Button(buttons, text="quit", command=self.quitPlayer)
        b2.pack(fill=BOTH, expand=YES)
        termf.pack(fill=BOTH, expand=YES)
        buttons.pack(fill=BOTH, expand=YES)
        self.wid = termf.winfo_id()
        print "wid : %d" % self.wid
        self.start()
        root.mainloop()
        os.unlink(self.fifoName)

if __name__ == "__main__":
    TkMplayer()

    
