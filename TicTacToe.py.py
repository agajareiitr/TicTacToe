from tkinter import *
import tkinter.messagebox

tk = Tk()
tk.title("Tic Tac Toe")

bclick = True


def ttt(buttons):
    # noinspection SpellCheckingInspection
    global bclick
    if buttons["text"] == " " and True == bclick:
        buttons["text"] = "x"
        bclick = False
    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "o"
        bclick = True
    elif button1['text'] == 'x' and button2['text'] == 'X' and button3['text'] == 'X':
        tkinter.messagebox.showinfo("player X", "winner is X !!!")
    elif button4['text'] == 'x' and button5['text'] == 'X' and button6['text'] == 'X':
        tkinter.messagebox.showinfo("player X", "winner is X !!!")
    elif button7['text'] == 'x' and button8['text'] == 'X' and button9['text'] == 'X':
        tkinter.messagebox.showinfo("player X", "winner is X !!!")
    elif button1['text'] == 'x' and button5['text'] == 'X' and button9['text'] == 'X':
        tkinter.messagebox.showinfo("player X", "winner is X !!!")
    elif button3['text'] == 'x' and button5['text'] == 'X' and button7['text'] == 'X':
        tkinter.messagebox.showinfo("player X", "winner is X !!!")
    elif button1['text'] == 'x' and button4['text'] == 'X' and button7['text'] == 'X':
        tkinter.messagebox.showinfo("player X", "winner is X !!!")
    elif button2['text'] == 'x' and button5['text'] == 'X' and button8['text'] == 'X':
        tkinter.messagebox.showinfo("player X", "winner is X !!!")
    elif button3['text'] == 'x' and button6['text'] == 'X' and button9['text'] == 'X':
        tkinter.messagebox.showinfo("player X", "winner is X !!!")

    elif button1['text'] == 'o' and button2['text'] == 'O' and button3['text'] == 'O':
        tkinter.messagebox.showinfo("player O ", "Winner is O !!!")
    elif button4['text'] == 'o' and button5['text'] == 'O' and button6['text'] == 'O':
        tkinter.messagebox.showinfo("player O ", "Winner is O !!!")
    elif button7['text'] == 'o' and button8['text'] == 'O' and button9['text'] == 'O':
        tkinter.messagebox.showinfo("player O ", "Winner is O !!!")
    elif button1['text'] == 'o' and button5['text'] == 'O' and button9['text'] == 'O':
        tkinter.messagebox.showinfo("player O ", "Winner is O !!!")
    elif button3['text'] == 'o' and button5['text'] == 'O' and button7['text'] == 'O':
        tkinter.messagebox.showinfo("player O ", "Winner is O !!!")
    elif button1['text'] == 'o' and button4['text'] == 'O' and button7['text'] == 'O':
        tkinter.messagebox.showinfo("player O ", "Winner is O !!!")
    elif button2['text'] == 'o' and button5['text'] == 'O' and button8['text'] == 'O':
        tkinter.messagebox.showinfo("player O ", "Winner is O !!!")
    elif button3['text'] == 'o' and button6['text'] == 'O' and button9['text'] == 'O':
        tkinter.messagebox.showinfo("player O ", "Winner is O !!!")


buttons = StringVar()
button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='White', height=4, width=8,
                 command=lambda: ttt(button1))
button1.grid(row=1, column=0, sticky=S + N + E + W)

button2 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='White', height=4, width=8,
                 command=lambda: ttt(button2))
button2.grid(row=1, column=1, sticky=S + N + E + W)

button3 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='White', height=4, width=8,
                 command=lambda: ttt(button3))
button3.grid(row=1, column=2, sticky=S + N + E + W)

button4 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='White', height=4, width=8,
                 command=lambda: ttt(button4))
button4.grid(row=2, column=0, sticky=S + N + E + W)

button5 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='White', height=4, width=8,
                 command=lambda: ttt(button5))
button5.grid(row=2, column=1, sticky=S + N + E + W)

button6 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='White', height=4, width=8,
                 command=lambda: ttt(button6))
button6.grid(row=2, column=2, sticky=S + N + E + W)

button7 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='White', height=4, width=8,
                 command=lambda: ttt(button7))
button7.grid(row=3, column=0, sticky=S + N + E + W)

button8 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='White', height=4, width=8,
                 command=lambda: ttt(button8))
button8.grid(row=3, column=1, sticky=S + N + E + W)

button9 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='White', height=4, width=8,
                 command=lambda: ttt(button9))
button9.grid(row=3, column=2, sticky=S + N + E + W)

tk.mainloop()
