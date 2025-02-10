#vd1
from tkinter import *
#tao 1 cua so moi
window = Tk()
window.title("Welcome to EAUT")
window.geometry('350x200')
window.mainloop()

#vd2
from tkinter import *
window = Tk()
window.title("Welcome to Vniteach app")
lbl = Label(window, text = "Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
window.mainloop()

#vd3
from tkinter import *
window = Tk()
window.title("Welcome to EAUT")
window.geometry('350x200')
lbl = Label(window,text="Hello")
lbl.grid(column=0, row=0)
btn = Button(window, text="Click me", bg="orange",fg="red")
btn.grid(column=1, row=0)
window.mainloop()

#vd5
from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("100x100")
def helloCallBack():
    msg = messagebox.showinfo("Hello Python", "Hello World")
B = Button(top, text="Hello", command = helloCallBack)
B.place(x=50,y=50)
top.mainloop()

#vd6
from tkinter import *
window = Tk()
window.title("Welcome to EAUT")
window.geometry('350x200')
lbl = Label(window,text = "hello")
lbl.grid(column=0,row=0)
txt = Entry(window,width=10)
txt.grid(column=1,row=0)
txt.focus()
def clicked():
    res ="Welcome to" + txt.get()
    lbl.configue(text=res)
btn = Button(window,text="Click me", command=clicked)
btn.grid(column=2,row=0)
#để tắt chức năng nhập của TẽtBox bằng state
#txt = Entry(window, width=10, state='disabled')
window.mainloop()

#vd7
from tkinter import *
from tkinter.ttk import *
window =Tk()
window.title("Welcome to EAUT")
window.geometry('350x200')
combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=0,row=0)
window.mainloop()


#vd8
from tkinter import *
from tkinter.ttk import *
window =Tk()
window.title("Welcome to EAUT")
window.geometry('350x200')
chk_state = BooleanVar()
chk_state.set(True) #set check state to True
chk= Checkbutton(window,text='Choose', var=chk_state)
chk.grid(column=0,row=0)
window.mainloop()

#vd9
from tkinter import *
from tkinter.ttk import *
window =Tk()
window.title("Welcome to EAUT")
selected = IntVar()
rad1 = Radiobutton(window, text="First", variable=selected, value=1)
rad2 = Radiobutton(window, text="Second", variable=selected, value=2)
rad3 = Radiobutton(window, text="Third", variable=selected, value=3)
def clicked():
    print(selected.get())
btn = Button(window,text="click me", command=clicked)
rad1.grid(column=0,row=0)
rad2.grid(column=1,row=0)
rad3.grid(column=2,row=0)
btn.grid(column=3,row=0)
window.mainloop()


#vd10
from tkinter import *
from tkinter import  scrolledtext
window =Tk()
window.title("Welcome to EAUT")
window.geometry('350x200')
txt = scrolledtext.ScrolledText(window, width=40, height= 10)
txt.grid(column=0,row=0)
window.mainloop()


#vd11
#lam viec voi messagebox
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Welcome to EAUT")
window.geometry('350x200')
def clicked():
    # hop thoai thong bao
    messagebox.showinfo("EAUT", "Hello, world!")
    #hop thoai canh bao
    messagebox.showwarning("EAUT", "Hello, world!")
    #hop thoai thong bao loi
    messagebox.showerror("EAUT", "Hello, world!")
    #hop thoai cau hoi
    res = messagebox.askquestion('message title', 'message content')
    res = messagebox.askyesno('message title', 'message content')
    res= messagebox.askyesnocancel('message title', 'message content')
    res= messagebox.askokcancel('message title', 'message content')
    res= messagebox.askretrycancel('message title', 'message content')
btn = Button(window, text='click here', command=clicked)
btn.grid(column=0,row=0)
window.mainloop()

    