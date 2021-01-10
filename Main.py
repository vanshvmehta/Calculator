from tkinter import *

root = Tk()
root.title('Simple Calculator')

e = Entry(root, width=60, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=7)

op = []


def button_number(num):
    global op
    temp = e.get()
    if temp in ('+', '-', '*', '/', '%'):
        if temp == '%':
            e.delete(0, END)
        else:
            op += temp
            e.delete(0, END)
    e.insert(END, num)


def button_char(char):
    global op
    temp = e.get()
    e.delete(0, END)
    e.insert(0, char)

    if temp not in ('+', '-', '*', '/', '%'):
        op += temp


def main():
    answer = op[0]
    for i in range(1, len(op)):
        answer += op[i]
    try:
        e.insert(0, eval(answer))
    except ZeroDivisionError:
        e.insert(0, 'Invalid operation (Division by Zero)')
    except SyntaxError:
        e.insert(0, 'Please enter a valid operation')


def button_per():
    global op
    op += e.get()
    e.delete(0, END)
    e.insert(0, '%')
    op += ['/100*']


def button_equal():
    global op
    op += e.get()
    e.delete(0, END)
    main()


def button_clear():
    global op
    e.delete(0, END)
    op = []


x = 40
y = 20

# Defining Buttons
b_clear = Button(root, text='C', padx=39, pady=y, command=lambda: button_clear())
b_minus = Button(root, text='-', padx=41, pady=y, command=lambda: button_char('-'))
b_multiply = Button(root, text='*', padx=41, pady=y, command=lambda: button_char('*'))
b_divide = Button(root, text='/', padx=x, pady=y, command=lambda: button_char('/'))

b_7 = Button(root, text='7', padx=x, pady=y, command=lambda: button_number('7'))
b_8 = Button(root, text='8', padx=x, pady=y, command=lambda: button_number('8'))
b_9 = Button(root, text='9', padx=x, pady=y, command=lambda: button_number('9'))

b_4 = Button(root, text='4', padx=x, pady=y, command=lambda: button_number('4'))
b_5 = Button(root, text='5', padx=x, pady=y, command=lambda: button_number('5'))
b_6 = Button(root, text='6', padx=x, pady=y, command=lambda: button_number('6'))

b_1 = Button(root, text='1', padx=x, pady=y, command=lambda: button_number('1'))
b_2 = Button(root, text='2', padx=x, pady=y, command=lambda: button_number('2'))
b_3 = Button(root, text='3', padx=x, pady=y, command=lambda: button_number('3'))

b_0 = Button(root, text='0', padx=x, pady=y, command=lambda: button_number('0'))
b_del = Button(root, text='.', padx=42, pady=y, command=lambda: button_number('.'))
b_percent = Button(root, text='%', padx=x, pady=y, command=button_per)

b_plus = Button(root, text='+', padx=x, pady=52, command=lambda: button_char('+'))
b_enter = Button(root, text='=', padx=x, pady=52, command=lambda: button_equal())

# Griding the buttons
b_clear.grid(row=1, column=0)
b_divide.grid(row=1, column=1)
b_multiply.grid(row=1, column=2)
b_minus.grid(row=1, column=3)

b_7.grid(row=2, column=0)
b_8.grid(row=2, column=1)
b_9.grid(row=2, column=2)

b_4.grid(row=3, column=0)
b_5.grid(row=3, column=1)
b_6.grid(row=3, column=2)

b_1.grid(row=4, column=0)
b_2.grid(row=4, column=1)
b_3.grid(row=4, column=2)

b_0.grid(row=5, column=0)
b_percent.grid(row=5, column=1)
b_del.grid(row=5, column=2)

b_plus.grid(row=2, column=3, rowspan=2)
b_enter.grid(row=4, column=3, rowspan=2)

root.mainloop()
