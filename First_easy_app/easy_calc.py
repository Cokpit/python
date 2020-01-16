from tkinter import *

root = Tk()
root.title("Kalkulator by Arek")
root.geometry("400x400")
root.maxsize(width=350, height=400)
root.minsize(width=350, height=400)

exp = ""
def press(num):
    global exp
    exp = str(num)
    dzialanie.insert(END, exp)

def clean_pole():
    global exp
    exp = ""
    dzialanie.delete(0,END)
    dzialanie.insert(0,exp)
    wynik.delete(0, END)
    wynik.insert(0,exp)

def press_equal():
    total = str(eval(dzialanie.get()))
    wynik.delete(0, END)
    wynik.insert(0, total)


appTop = Frame(root)
appBottom = Frame(root)
appTop.grid(row = 0, column = 0, padx = 10, pady = 10)
appBottom.grid(row = 1, column = 0, padx = 10, pady = 10)

wynik = Entry(appTop, bg = "white", width = 20, justify = "right", font = ("", 20))
wynik.grid(row = 1, column = 0)

dzialanie = Entry(appTop, bg = "grey", width = 50, justify = "right")
dzialanie.grid(row=0, column=0)

button1 = Button(appBottom, text = "1", height = 2, width = 6, pady = 10, command = lambda : press(1))
button2 = Button(appBottom, text = "2", height = 2, width = 6, pady = 10, command = lambda : press(2))
button3 = Button(appBottom, text = "3", height = 2, width = 6, pady = 10, command = lambda : press(3))
button4 = Button(appBottom, text = "4", height = 2, width = 6, pady = 10, command = lambda : press(4))
button5 = Button(appBottom, text = "5", height = 2, width = 6, pady = 10, command = lambda : press(5))
button6 = Button(appBottom, text = "6", height = 2, width = 6, pady = 10, command = lambda : press(6))
button7 = Button(appBottom, text = "7", height = 2, width = 6, pady = 10, command = lambda : press(7))
button8 = Button(appBottom, text = "8", height = 2, width = 6, pady = 10, command = lambda : press(8))
button9 = Button(appBottom, text = "9", height = 2, width = 6, pady = 10, command = lambda : press(9))
button0 = Button(appBottom, text = "0", height = 2, width = 6, pady = 10, command = lambda : press(0))
button_equal = Button(appBottom, text = "=", height = 2, width = 6, pady = 10, command = press_equal)
button_clean = Button(appBottom, text = "R", height = 2, width = 6, pady = 10, command = clean_pole)
button_plus = Button(appBottom, text = "+", height = 2, width = 6, pady = 10, command = lambda : press("+"))
button_minus = Button(appBottom, text = "-", height = 2, width = 6, pady = 10, command = lambda : press("-"))
button_mnoz = Button(appBottom, text = "*", height = 2, width = 6, pady = 10, command = lambda : press("*"))
button_dziel = Button(appBottom, text = "/", height = 2, width = 6, pady = 10, command = lambda : press("/"))

button7.grid(row = 0, column = 0, pady = 5)
button8.grid(row = 0, column = 1, pady = 5)
button9.grid(row = 0, column = 2, pady = 5)
button_plus.grid(row = 0, column = 3, pady = 5, padx = 20)
button4.grid(row = 1, column = 0, pady = 5)
button5.grid(row = 1, column = 1, pady = 5)
button6.grid(row = 1, column = 2, pady = 5)
button_minus.grid(row = 1, column = 3, pady = 5, padx = 20)
button1.grid(row = 2, column = 0, pady = 5)
button2.grid(row = 2, column = 1, pady = 5)
button3.grid(row = 2, column = 2, pady = 5)
button_mnoz.grid(row = 2, column = 3, pady = 5, padx = 20)
button0.grid(row = 3, column = 0, pady = 5)
button_equal.grid(row = 3, column = 1, pady = 5)
button_clean.grid(row = 3, column = 2, pady = 5)
button_dziel.grid(row = 3, column = 3, pady = 5, padx = 20)

root.mainloop()
