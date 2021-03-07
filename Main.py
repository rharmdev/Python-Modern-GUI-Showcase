import tkinter as tk
from tkinter import *
import winsound
import time
from tkinter.font import Font


def ScoresWindow():
    def onleave3(event):
        But3.config(bg='grey', fg='white')

    def OnPressed3(event):
        winsound.PlaySound('clic.wav', winsound.SND_ASYNC)
        root.title("Modern")
        label.destroy()
        But3.destroy()
        But1.place(x=0, y=0)
        But2.place(x=200, y=0)

    def OnHover3(event):
        But3.config(bg='grey', fg='black')
        winsound.PlaySound('MenuMove.wav', winsound.SND_ASYNC)

    root.title("Game")

    label = Label(text="G A M E S", background="grey", font=myFont)
    label.pack()
    But3 = Button(text='B A C K', bg='grey', fg='white', relief='groove', border=0, font=myFont2)
    But3.place(x=00, y=620)
    But3.bind('<Button-1>', OnPressed3)
    But3.bind('<Enter>', OnHover3)
    But3.bind('<Leave>', onleave3)


def OnPressed1(event):
    ScoresWindow()
    winsound.PlaySound('clic.wav', winsound.SND_ASYNC)
    But1.place_forget()
    But2.place_forget()


def OnPressed2(event):
    print("Helo")
    winsound.PlaySound('clic.wav', winsound.SND_ASYNC)


def OnHover1(event):
    But1.config(bg='grey', fg='white')
    winsound.PlaySound('MenuMove.wav', winsound.SND_ASYNC)


def OnHover2(event):
    But2.config(bg='grey', fg='white')
    winsound.PlaySound('MenuMove.wav', winsound.SND_ASYNC)


def onleave1(event):
    But1.config(bg='grey', fg='black')


def onleave2(event):
    But2.config(bg='grey', fg='black')


def digitalclock():
    text_input = time.strftime("%H : %M : %S")
    label.config(text=text_input)
    label.after(200, digitalclock)


root = tk.Tk()
root.resizable(0, 0)
myFont = Font(family="Calibri", size=30, weight="normal", underline=1)
myFont2 = Font(family="Arial Black", size=20, weight="normal")
text = tk.Text(root)
text.configure(font=myFont)

root.title("Modern")
root.geometry("1280x720")
root.iconbitmap('Assets/icon.ico')
root.configure(background='grey')
But1 = Button(root, text='S C O R E S', bg='grey', relief='groove', border=0, font=myFont)
But1.place(x=0, y=0)
But1.bind('<Button-1>', OnPressed1)
But1.bind('<Enter>', OnHover1)
But1.bind('<Leave>', onleave1)
But2 = Button(root, text='G A M E', bg='grey', relief='groove', border=0, font=myFont)
But2.place(x=200, y=0)
But2.bind('<Button-1>', OnPressed2)
But2.bind('<Enter>', OnHover2)
But2.bind('<Leave>', onleave2)
label = Label(root, font=("Helvetica", 30), bg="grey", fg="white", bd=30)
label.place(x=1020, y=620)
footer = tk.Frame(root, bg='#D0CBCB', height=10)
footer.pack(fill='both', side='bottom')
panel = tk.Frame(root, bg='#D0CBCB', height=40)
panel.pack(fill='both', side='right')
panel2 = tk.Frame(root, bg='#D0CBCB', height=40)
panel2.pack(fill='both', side='left')

digitalclock()
root.mainloop()
