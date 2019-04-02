#coding: utf-8

import turtle
import random
import math
import mrrobot

PHI = 360 / 7
R = 50
turtle.speed(0)


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def draw_revolve(x, y):
    #основной круг
    gotoxy(x, y)
    turtle.circle(80)
    #мушка
    gotoxy(x, y+160)
    draw_circle(5, 'red')
    #барабан
    for i in range(0, 7):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(x+math.sin(phi_rad) * R, y+math.cos(phi_rad) * R + 60)
        draw_circle(22, 'brown')
        draw_circle(22, 'white')


def spin_revole(x, y, start):
    for i in range(start, random.randrange(7, 100)):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(x + math.sin(phi_rad) * R, y + math.cos(phi_rad) * R + 60)
        draw_circle(22, 'brown')
        draw_circle(22, 'white')

    gotoxy(x+math.sin(phi_rad) * R, y+math.cos(phi_rad) * R + 60)
    draw_circle(22, 'brown')
    return i % 7



draw_revolve(100, 100)

answer = ''
start = 0
while answer != 'N':
    answer = turtle.textinput('Играем?', 'Y/N').upper()
    if answer == 'Y':

        start = spin_revole(100, 100, start)

        if start == 0:
            gotoxy(-150, 250)
            turtle.write('Вы проиграли!', font=('Arial', 18, 'normal'))
            mrrobot.double_files('.')

        # turtle.penup()
        # turtle.goto(random.randrange(-300, 300), random.randrange(-200, 200))
        # turtle.pendown()
        # turtle.fillcolor(random.random(), random.random(), random.random())
        # turtle.begin_fill()
        # turtle.circle(random.randrange(1, 100))
        # turtle.end_fill()
    else:
        pass