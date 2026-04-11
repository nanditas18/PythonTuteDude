from tkinter import *

root = Tk()
root.title("Calculator")

entry = Entry(root, width=25, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

first_num = 0
operation = ""

# Number buttons
def click_0(): entry.insert(END, "0")
def click_1(): entry.insert(END, "1")
def click_2(): entry.insert(END, "2")
def click_3(): entry.insert(END, "3")
def click_4(): entry.insert(END, "4")
def click_5(): entry.insert(END, "5")
def click_6(): entry.insert(END, "6")
def click_7(): entry.insert(END, "7")
def click_8(): entry.insert(END, "8")
def click_9(): entry.insert(END, "9")

def clear():
    entry.delete(0, END)

def set_op(op):
    global first_num, operation
    try:
        first_num = int(entry.get())
        operation = op
        entry.delete(0, END)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def add(): set_op("+")
def sub(): set_op("-")
def mul(): set_op("*")
def div(): set_op("/")

def calculate():
    global first_num, operation
    try:
        second_num = int(entry.get())
        entry.delete(0, END)

        if operation == "+":
            result = first_num + second_num
        elif operation == "-":
            result = first_num - second_num
        elif operation == "*":
            result = first_num * second_num
        elif operation == "/":
            if second_num == 0:
                entry.insert(0, "Error")
                return
            result = first_num / second_num
        else:
            entry.insert(0, "Error")
            return

        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

# Layout
Button(root, text="7", command=click_7).grid(row=1, column=0)
Button(root, text="8", command=click_8).grid(row=1, column=1)
Button(root, text="9", command=click_9).grid(row=1, column=2)
Button(root, text="/", command=div).grid(row=1, column=3)

Button(root, text="4", command=click_4).grid(row=2, column=0)
Button(root, text="5", command=click_5).grid(row=2, column=1)
Button(root, text="6", command=click_6).grid(row=2, column=2)
Button(root, text="*", command=mul).grid(row=2, column=3)

Button(root, text="1", command=click_1).grid(row=3, column=0)
Button(root, text="2", command=click_2).grid(row=3, column=1)
Button(root, text="3", command=click_3).grid(row=3, column=2)
Button(root, text="-", command=sub).grid(row=3, column=3)

Button(root, text="0", command=click_0).grid(row=4, column=0)
Button(root, text="C", command=clear).grid(row=4, column=1)
Button(root, text="=", command=calculate).grid(row=4, column=2)
Button(root, text="+", command=add).grid(row=4, column=3)

root.mainloop()