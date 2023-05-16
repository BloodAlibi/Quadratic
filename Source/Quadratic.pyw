# BloodAlibi // 2022

import tkinter
from tkinter import messagebox
from math import sqrt
from fractions import Fraction

#---------

Window = tkinter.Tk()

#---------

def Clearer():
    AValueEntry.delete(0, "end")
    BValueEntry.delete(0, "end")
    CValueEntry.delete(0, "end")

def Delta(a,b,c):
    return ((b)**2)-(4*(a)*(c))
    
def Solutions(a,b,c):
    delta = Delta(a,b,c)
    if delta > 0:
        x1 = ((-b)-sqrt(delta))/(2*a)
        x2 = ((-b)+sqrt(delta))/(2*a)
    elif delta == 0:
        x1 = (-b)/(2*a)
        x2 = None
    elif delta < 0:
        x1 = None
        x2 = None
    else:
        print("Error finding the solutions. Delta is nil!")
    return x1, x2, delta
    
def Solver():
    a = AValueEntry.get()
    b = BValueEntry.get()
    c = CValueEntry.get()
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError:
        messagebox.showerror("Values Error","Please enter valid numbers.")
        return
    if a == 0:
        messagebox.showerror("Values Error","The value of \"a\" can't be equal to 0.")
        return
    x1, x2, d = Solutions(a,b,c)
    DeltaValueEntry.delete(0, "end")
    DeltaValueEntry.insert(0, str(d))
    x1ValueEntry.delete(0, "end")
    x2ValueEntry.delete(0, "end")
    if d > 0 and x1 != None and x2 != None:
        if type(x1) != "int":
            x1 = Fraction(x1).limit_denominator()
        if type(x2) != "int":
            x2 = Fraction(x2).limit_denominator()
        x1ValueEntry.insert(0, str(x1))
        x2ValueEntry.insert(0, str(x2))
        print("d is > to 0, 2 solutions.")
    elif d == 0 and x1 != None and x2 == None:
        if type(x1) != "int":
            x1 = Fraction(x1).limit_denominator()
        x1ValueEntry.insert(0, str(x1))
        print("d is = to 0, 1 solution.")
    elif d < 0 and x1 == None and x2 == None:
        print("d is < to 0, no solution.")
    else:
        x1ValueEntry.insert("Error.")
        x2ValueEntry.insert("Error.")
        print("Error with the solutions. No solution but delta is not infierior to 0, or solutions with delta inferior to 0.")

#---------

CreditLabel = tkinter.Label(Window, text="Made by BloodAlibi", font=("Helvetica", 6), fg = "grey")
CreditLabel.place(x=0, y=0)

#---------

SolveButton = tkinter.Button(Window, text="Solve", command=Solver)
SolveButton.place(x=160, y=170)
ClearButton = tkinter.Button(Window, text="Clear", command=Clearer)
ClearButton.place(x=220, y=170)

#---------

IndicationLabel = tkinter.Label(Window, text="A quadratic equation uses this format :", font=("Helvetica", 10))
IndicationLabel2 = tkinter.Label(Window, text="ax² + bx + c = 0", font=("Helvetica", 10))
IndicationLabel3 = tkinter.Label(Window, text="Please indicate below the values of a, b and c.", font=("Helvetica", 10))
IndicationLabel.place(x=95, y=20)
IndicationLabel2.place(x=160, y=40)
IndicationLabel3.place(x=73, y=60)

#---------

AValueEntry = tkinter.Entry(Window, text="", bd=2)
AValueEntry.place(x=162, y=88)
AValueEntry_title = tkinter.Label(Window, text="a = ", font=("Helvetica", 10))
AValueEntry_title.place(x=132, y=87)

BValueEntry = tkinter.Entry(Window, text="", bd=2)
BValueEntry.place(x=162, y=113)
AValueEntry_title = tkinter.Label(Window, text="b = ", font=("Helvetica", 10))
AValueEntry_title.place(x=132, y=112)

CValueEntry = tkinter.Entry(Window, text="", bd=2)
CValueEntry.place(x=162, y=138)
AValueEntry_title = tkinter.Label(Window, text="c = ", font=("Helvetica", 10))
AValueEntry_title.place(x=132, y=137)

#---------

DeltaValueEntry = tkinter.Entry(Window, text="", bd=2)
DeltaValueEntry.place(x=45, y=219)
DeltaValueEntry_title = tkinter.Label(Window, text="Δ = ", font=("Helvetica", 10))
DeltaValueEntry_title.place(x=12, y=218)
x1ValueEntry = tkinter.Entry(Window, text="", bd=2, width=10)
x1ValueEntry.place(x=223, y=219)
x1ValueEntry_title = tkinter.Label(Window, text="x1 = ", font=("Helvetica", 10))
x1ValueEntry_title.place(x=180, y=218)
x2ValueEntry = tkinter.Entry(Window, text="", bd=2, width=10)
x2ValueEntry.place(x=350, y=219)
x2ValueEntry_title = tkinter.Label(Window, text="x2 = ", font=("Helvetica", 10))
x2ValueEntry_title.place(x=310, y=218)

Window.title('Quadratic | Quadratic Equations Solver')
Window.iconbitmap("icon.ico")
Window.geometry("435x270")

Window.mainloop()
