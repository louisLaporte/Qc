#!/usr/bin/env python3.4
import curses

from Qc.Widgets import CApplication, CMainWindow, CGridLayout, CWidget
from Qc.Extra import *

from time import sleep
import os

def main():

    app = CApplication()

    try:
        DEBUG("- ** START INIT")
        w = CWidget()
        w.setObjectName("main")
        DEBUG("{}".format(w.objectName()))
        g = CGridLayout()
        g.setObjectName("layout_{}".format(0))
        DEBUG("{}".format(g.objectName()))

        for i in range(0,1):
            for j in range(0,2):
                w1 = CWidget()
                w1.setObjectName("widget_{}_{}".format(i,j))
                DEBUG("{}".format(w1.objectName()))
                g.addWidget(w1,i,j)

        w.addLayout(g)
        DEBUG("+ ** END INIT")

    except NameError as err:
        app.exit()
        print(err)

    else:
        try:
            i = 0

            while True:
                DEBUG(">>>>>>>>> i: {}".format(i))
                w.show(border=True)
                sleep(1)
                i += 1

        except KeyboardInterrupt as err:
            app.exit()
            print("KeyboardInterrupt",err)

        except AttributeError as err:
            app.exit()
            print("Attribute Error",err)

if __name__ == '__main__':

    try:
        main()

    except KeyboardInterrupt:
        cur.end_curses()
