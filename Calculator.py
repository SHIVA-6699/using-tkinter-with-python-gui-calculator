from tkinter import *
a=Tk()
def btn(num):
    cur=e.get()
    clear()
    fin=cur+num
    e.insert(0,fin)
    
def clear():
    e.delete(0,END)
def add(values):
    global first,math
    math=values
    first=e.get()
    clear()
def equal():
    second=e.get()
    clear()
    if math == 'add':
        result=int(first)+int(second)
    elif math=="min":
        result=int(first)-int(second)
    elif math=="mul":
        result=int(first)*int(second)
    elif math=="div":
        result=int(first)/ int(second)
    
    e.insert(0,str(result))
a.config(background='black')
a.title("*****SIMPLE CALCULATOR*******")
e=Entry(a,justify=RIGHT,width=14,font=('times to roman',24))
e.grid(row=0,column=0,padx=10,pady=10,columnspan=4)
but0=Button(a,text='0',padx=36,pady=10,command= lambda: btn('0'),fg='orange',bg='black')
but1=Button(a,text='1',padx=36,pady=10,command= lambda: btn('1'),fg='orange',bg='black')
but2=Button(a,text='2',padx=36,pady=10,command= lambda: btn('2'),fg='orange',bg='black')
but3=Button(a,text='3',padx=36,pady=10,command= lambda: btn('3'),fg='orange',bg='black')
but4=Button(a,text='4',padx=36,pady=10,command= lambda: btn('4'),fg='orange',bg='black')
but5=Button(a,text='5',padx=36,pady=10,command= lambda: btn('5'),fg='orange',bg='black')
but6=Butto n(a,text='6',padx=36,pady=10,command= lambda: btn('6'),fg='orange',bg='black')
but7=Button(a,text='7',padx=36,pady=10,command= lambda: btn('7'),fg='orange',bg='black')
but8=Button(a,text='8',padx=36,pady=10,command= lambda: btn('8'),fg='orange',bg='black')
but9=Button(a,text='9',padx=36,pady=10,command= lambda: btn('9'),fg='orange',bg='black')




but0.grid(row=4,column=0,padx=1,pady=1)
but1.grid(row=3,column=0,padx=1,pady=1)
but2.grid(row=3,column=1,padx=1,pady=1)
but3.grid(row=3,column=2,padx=1,pady=1)
but4.grid(row=2,column=0,padx=1,pady=1)
but5.grid(row=2,column=1,padx=1,pady=1)
but6.grid(row=2,column=2,padx=1,pady=1)
but7.grid(row=1,column=0,padx=1,pady=1)
but8.grid(row=1,column=1,padx=1,pady=1)
but9.grid(row=1,column=2,padx=1,pady=1)


clearbut=Button(a,text='clear',padx=74,pady=10,font=("impact",12),fg="red",command=clear,activebackground="yellow")
buta=Button(a,text='+',padx=36,pady=10,command=lambda:add('add'),fg='orange',bg='black')
butb=Button(a,text='-',padx=36,pady=10,command=lambda:add('min'),fg='orange',bg='black')
butc=Button(a,text='*',padx=36,pady=10,command=lambda:add('mul'),fg='orange',bg='black')
butd=Button(a,text='/',padx=36,pady=10,command=lambda :add('div'),fg='orange',bg='black')
bute=Button(a,text='=',padx=36,pady=40,command=equal,fg="green",activebackground="blue")

clearbut.grid(row=4,column=1,padx=2,pady=2,columnspan=2)
buta.grid(row=5,column=0,padx=1,pady=1)
butb.grid(row=5,column=1,padx=1,pady=1)
butc.grid(row=6,column=0,padx=1,pady=1)
butd.grid(row=6,column=1,padx=1,pady=1)
bute.grid(row=5,column=2,padx=1,pady=1,rowspan=2)

a.mainloop()
