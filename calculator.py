from tkinter import *

root=Tk()
root.title('calculator')
root.resizable(width=False, height=False)
equa=""
symboles=['+','-','*','/','C','=']
a=symboles
b=symboles
count=2
counter=0
equation=StringVar()
k=0
j=2
cun=1
label=Label(root,textvariable=equation)
equation.set("Enter Your Expression")
label.grid(columnspan=10)

def display(num):
    global equa
    equa=equa+str(num)
    equation.set(equa)

def symboldisp(num):
    global counter
    global equa
    while counter==0:
        equa=equa+str(num)
        equation.set(equa)
        counter=counter+1

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def back():
    global equa
    global counter
    equa=equa[:-1]
    equation.set(equa)
    counter=0
    
def buttons(num):
    global j
    global counter
    global k
    if(num==0):
        button=Button(root,text=num)
        button.config(width=10, height=1,bg='yellow',command=lambda:display(num))
        button.grid(row=j,column=k,columnspan=2)
        counter=0
    else:
        button=Button(root,text=num)
        button.config(width=4, height=1,bg='yellow',command=lambda:display(num))
        button.grid(row=j,column=k)
        counter=0
        
    k=k+1
    if k==3:
        k=0
        j=j+1
        
def symbols(sym):
    global cun
    global counter
    but=Button(root,text=sym,bg='cyan',command=lambda:symboldisp(sym))
    but.grid(row=cun,column=4)
    but.config(width=4, height=1)
    cun=cun+1

def bracket():
    global count
    global counter
    global equa
    if(count%2==0):
        equa=equa+'('
        equation.set(equa)
        count=count+1
        counter=0
    else:
        equa=equa+')'
        equation.set(equa)
        count=count+1
        counter=0

def clear():
    global equa
    global counter
    equa=""
    equation.set("")
    counter=0

def equal():
    global equa
    global counter
    if '/0'in equa:
            equa='cannot divide by zero'
            equation.set(equa)
            equa=''
            counter=0
    else:
            try:
                total=str(eval(equa))
                equation.set(total)
                equa=''
                counter=0
                
            except SyntaxError as syn:
                 equa='Syntax error'
                 equation.set(equa)
                 equa=''
           
def close():
    exit()
    
photo = PhotoImage(file="capture.gif")
def about():
    filewin = Toplevel(root)
    label=Label(filewin,image=photo)
    label.pack()
    
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Clear", command=clear)
filemenu.add_command(label="Calculate", command=equal)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=close)
menubar.add_cascade(label="File", menu=filemenu)



helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
clear=Button(root,text='C',command=clear,bg='red')
clear.grid(row=1,column=0,columnspan=1)
clear.config(width=4, height=1)

bracket=Button(root,text='(  )',command=bracket,bg='cyan')
bracket.grid(row=1,column=1)
bracket.config(width=4, height=1)

brack=Button(root,text='<--',command=back,bg='cyan')
brack.grid(row=1,column=2)
brack.config(width=4, height=1)

buttons(1)
buttons(2)
buttons(3)
buttons(4)
buttons(5)
buttons(6)
buttons(7)
buttons(8)
buttons(9)
buttons(0)

symbols('+')
symbols('-')
symbols('/')
symbols('*')
symbols('.')

equal=Button(root,text='=',command=equal,bg='Light green')
equal.grid(row=5,column=2)
equal.config(width=4, height=1)


root.mainloop()

    

