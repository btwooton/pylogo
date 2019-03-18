from turtle import *
import math
import random

def setxy(x, y):
    setx(x)
    sety(y)

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def equals(a, b):
    return a == b

def lt(a, b):
    return a < b

def gt(a, b):
    return a > b

def set_color(val):

    if val == 0:
        pencolor("black")
    elif val == 1:
        pencolor("blue")
    elif val == 2:
        pencolor("green")
    elif val == 3:
        pencolor("cyan")
    elif val == 4:
        pencolor("red")
    elif val == 5:
        pencolor("magenta")
    elif val == 6:
        pencolor("yellow")
    elif val == 7:
        pencolor("white")
    elif val == 8:
        pencolor("brown")
    elif val == 9:
        pencolor("tan")
    elif val == 10:
        pencolor("dark green")
    elif val == 11:
        pencolor("aquamarine")
    elif val == 12:
        pencolor("salmon")
    elif val == 13:
        pencolor("purple")
    elif val == 14:
        pencolor("orange")
    elif val == 15:
        pencolor("gray")

def rand(val):

    return int(random.random() * val)

table = {
        'forward': forward,
        'fd': forward,
        'backward': backward,
        'bk': backward,
        'left': left,
        'lt': left,
        'right': right,
        'rt': right,
        'setpos': setpos,
        'setxy': setxy,
        'setx': setx,
        'sety': sety,
        'setheading': setheading,
        'seth': seth,
        'home': home,
        'arc': circle,
        'pendown': pendown,
        'pd': pendown,
        'penup': penup,
        'pu': penup,
        'clean': clear,
        '+': add,
        '*': mul,
        '-': sub,
        '/': div,
        'setwidth': width,
        'setcolor': set_color,
        'setpencolor': set_color,
        '=': equals,
        '<': lt,
        '>': gt,
        'sqrt': math.sqrt,
        'power': pow,
        'ln': math.log,
        'exp': math.exp,
        'log10': math.log10,
        'random': rand,
        'difference': sub,
        }

arity_table = {
        'forward': 1,
        'fd': 1,
        'backward': 1,
        'bk': 1,
        'left': 1,
        'lt': 1,
        'right': 1,
        'rt': 1,
        'setpos': 2,
        'setxy': 2,
        'setx': 1,
        'sety': 1,
        'setheading': 1,
        'seth': 1,
        'home': 0,
        'arc': 2,
        'pendown': 0,
        'pd': 0,
        'penup': 0,
        'pu': 0,
        'clean': 0,
        '+': 2,
        '*': 2,
        '-': 2,
        '/': 2,
        'setwidth': 1,
        'setcolor': 1,
        'setpencolor': 1,
        '=': 2,
        '<': 2,
        '>': 2,
        'sqrt': 1,
        'power': 2,
        'ln': 1,
        'exp': 1,
        'log10': 1,
        'random': 1,
        'difference': 2,
        }
