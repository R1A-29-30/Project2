#!/usr/bin/env -S python3 -B
from tk_drawer_kanatovo1 import TkDrawer
from points1 import Point
import time
import math

class Competition:
    def __init__(self, px, py, qx, qy, radius):
        self.p = Point(px, py)
        self.q = Point(qx, qy)
        self.radius = radius
        self.o = Point(0,0)
        
        self.tk = TkDrawer()
        self.tk.clean()
        self.tk.draw_circle(self.o, radius, "grey80")
        self.tk.draw_point(self.p, "red")
        self.tk.draw_point(self.q, "green")
 
    def draw_path(self):
        
        self.tk.draw_line(self.p, self.q, "red")
        self.tk.draw_arc(self.p, self.q, math.radians(10), math.radians(90), "red")

for _ in range(int(input())):
    ls = map(int, input().split())
    c = Competition(*ls)


    
    c.draw_path()
    time.sleep(10)
   
    #c.tk.root.mainloop()
