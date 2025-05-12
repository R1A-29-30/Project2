from tkinter import *
from sympy import *
import numpy as np

root = Tk()
root.title('s')


cases = [ (1, 1, -1, 1, 1)]

def kasa(r, x1, y1):

    base_circle = Circle(Point(0, 0), 1)
    new_circle = Circle(Point(x1 / 2, y1 / 2), sqrt(x1 ** 2 + y1 ** 2) / 2)

    intersactions = intersection(base_circle, new_circle)
    return intersactions

def dlina_dugi(x1, y1, x2, y2, r):
    l = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    cosA = (2*r**2 - l**2)/(2*r)
    arc = acos(cosA)
    res = arc * 180 / 360 * 2 * r
    return res


canv = Canvas(width=1000, height=1000, bg="white", cursor='pencil')
k = 0
for i in range(int(input())):

    ls = [int(i) for i in input().split()]
    r = ls[4]
    canv.create_oval(500 - r*50, 375 - r*50, 500 + r*50, 375 + r*50, width = 5, fill = 'green')
    coor1 = kasa(r, ls[0], ls[1])
    coor2 = kasa(r, ls[2], ls[3])
    min_duga = []
    for i in coor1:
        for j in coor2:
            min_duga.append(dlina_dugi(i[0], i[1], j[0], j[1], r))

    canv.create_line(500 + 50 * ls[0], 375 - 50 * ls[1], 500 + 50 * coor1[0][0], 375 - 50* coor1[0][1], width = 5, fill = 'black')
    canv.create_line(500 + 50 * ls[2], 375 - 50 * ls[3], 500 + 50 * coor2[1][0], 375 - 50* coor2[1][1], width=5, fill='black')
    canv.create_line(500 + 50 * ls[2], 375 - 50 * ls[3], 500 + 50 * coor2[0][0], 375 - 50 * coor2[0][1], width=5,
                     fill='black')
    canv.create_line(500 + 50 * ls[0], 375 - 50 * ls[1], 500 + 50 * coor1[1][0], 375 - 50 * coor1[1][1], width=5,
                     fill='black')
    print(round(sum([sqrt((ls[0] - coor1[0][0])**2 + (ls[1] - coor1[0][1])**2), sqrt((ls[2] - coor2[0][0])**2 + (ls[3] - coor2[0][1])**2), min(min_duga)]), 3))
    k += 1

    

canv.pack()
root.mainloop()











