coding = 1251

from tkinter import *
from math import *

root = Tk()
root.title("Лабораторна робота №4")

xx_max, yy_max = 650, 650 # Розміри віджета Canvas
xx0, yy0 = xx_max/2, yy_max/2

c1 = Canvas(root, width=xx_max, height=yy_max, bg="white")

c1.create_text(500, 630, text="Виконала Степанюк О.С.\n"
                              "гр. КНІТ-Б18-Б")
c1.create_text(635, 295, text="X", font="Arial 18 italic")
c1.create_text(350, 15, text="Y", font="Arial 18 italic")
c1.create_text(160, 630, text="x = t*sin(t*3)\n"+
                              "y = t*sin(t)*cos(t*3)")


def draw_graph():
    c1.create_line(0, yy0, xx_max, yy0, width=1, arrow=LAST, arrowshape=(20, 25, 10))
    c1.create_line(xx0, yy_max, xx0, 0, width=1, arrow=LAST, arrowshape=(20, 25, 10))

    t1, t2 = 0, xx0
    i1, i2 = -10, 10
    dt = xx0 / 10
    di = 1
    t = t1
    i = i1

    while(t < t2):
        if t > 30:
            c1.create_text(xx0 + 15, t, text=-1 * i, font="Verdana 9")
            c1.create_line(yy0 - 10, t, yy0 + 5, t)
            c1.create_text(t - 1, xx0 - 22, text=i, font="Verdana 9")
            c1.create_line(t, yy0 - 10, t, yy0 + 10)
        i += di
        t += dt

    t1, t2 = xx0, xx_max
    i1, i2 = 0, 10
    dt = xx0 / 10
    di = 1
    t = t1
    i = i1
    while t < t2:
        if i != 0:
            c1.create_text(xx0 - 30, t, text=i, font="Verdana 9")
            c1.create_line(xx0 - 10, t, yy0 + 10, t)
            c1.create_text(t - 1, xx0 - 22, text=-1 * i, font="Verdana 9")
            c1.create_line(t, yy0 - 10, t, yy0 + 10)
        i -= di
        t += dt

def draw_function():

    t1, t2 = -10, 10
    dt = 0.001
    kx, ky = 100, 250
    t = t1

    while (t < t2):
        x = t * sin(3 * t)  # Функція x(t)
        y = t * sin(t) * cos(t * 3)  # Функція y(t)
        xx = kx * x + xx0
        yy = ky * y * (-1) + yy0
        c1.create_oval(xx, yy, xx, yy, fill="black")
        t = t + dt

draw_graph()
draw_function()


c1.pack(side=TOP, fill=BOTH)
root.mainloop()