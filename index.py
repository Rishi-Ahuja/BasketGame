import time
import random
from tkinter import *
tk=Tk()
canvas=Canvas(tk,width=800,height=800,bg='blue')
canvas.pack()
g=canvas.create_rectangle(0,500,1000,1000,fill='light green')
e=canvas.create_oval(200,10,230,60,fill='white',outline='black',width=5)
b=canvas.create_arc(100,500,200,600,start=180,extent=180,style='arc',outline='black',width=9)
z=0
def r(event):
    canvas.move(b,10,0)
def l(event):
    canvas.move(b,-10,0)
canvas.bind('<Right>',r)
canvas.bind('<Left>',l)
canvas.focus_set()
l=3
s=0
while True:
     a=random.randint(0,700)
     b1,b2,b3,b4=canvas.coords(b)
     e1,e2,e3,e4=canvas.coords(e)
     canvas.move(e,0,10)
     time.sleep(0.03)
     tk.update()
     if b4==e4 and b1<e1 and b3>e3:
         a=random.randint(0,1000)
         canvas.delete(e)
         e=canvas.create_oval(a,10,a+30,60,fill='white',outline='black',width=5)
         s=s+1
     elif b4<e4:
         for t in range(0,15):
           canvas.move(e,0,10)
         a=random.randint(0,800)
         e=canvas.create_oval(a,10,a+30,60,fill='white',outline='black',width=5)
         l=l-1
         print('lives=',l)
         if l==0:
             print('sorry but you lost')
             print ('score is',s)
             exit()
