#Import Tkinter
from tkinter import *
from tkinter.ttk import Label
#from tkinter .messageboximport
import primecheck
import Palindrome
import Anagram
import ascii
import armstrong
import leapyear
import evenodd
import fibo
import facto
import leaplist
import primelist
import listevenodd
import listarm

#Create GUI Window
window = Tk()
window.geometry('720x580')
window['bg']='sky blue'
l=Label(window,text="My Calculator",font=("Arial", 25),foreground='Blue',background='sky blue')
l.pack()
l=Label(window, text="Hope this calculator is useful - AM Robert",font=("Times New Roman", 15),foreground='Blue',background='sky blue')
l.pack()

#PALINDROME
def action():
    Palindrome.action()

b = Button(window, text='Palindrome',font=("Arial",10),foreground='white',command=action,bg='red')
b.place(x=30, y=100)

#ANAGRAM
def action():
    Anagram.action()

b = Button(window, text='Anagram',font=("Arial",10),foreground='white', command=action,bg='red')
b.place(x=30, y=150)

#PRIME NUMBERS
def action():
    primecheck.action()

b = Button(window, text='Prime Numbers',font=("Arial",10),foreground='white', command=action,bg='red')
b.place(x=30, y=500)

#ASCII VALUE
def action():
    ascii.action()

b = Button(window, text='ASCII Value',font=("Arial",10),foreground='white', command=action,bg='red')
b.place(x=30, y=250)

#ARMSTRONG
def action():
    armstrong.action()

b = Button(window, text='Armstrong',font=("Arial",10),foreground='white', command=action,bg='red')
b.place(x=30, y=200)

#LEAP YEAR
def action():
    leapyear.action()

b = Button(window, text='Leap Year',font=("Arial",10),foreground='white', command=action,bg='red')
b.place(x=30, y=450)

#EVEN OR ODD
def action():
    evenodd.action()

b = Button(window, text='Even/Odd',font=("Arial",10),foreground='white', command=action,bg='red')
b.place(x=30, y=300)

#FIBONACCI
def action():
    fibo.action()

b = Button(window, text='Fibonacci',font=("Arial",10),foreground='white', command=action,bg='red')
b.place(x=30, y=400)

#FACTORIAL
def action():
    facto.action()

b = Button(window, text='Factorial',font=("Arial",10),foreground='white', command=action,bg='red')
b.place(x=30, y=350)

#LIST OF LEAP YEARS
def action():
    leaplist.action()

b = Button(window, text='List of Leap Years',font=("Arial",10),foreground='white', command=action,bg='red')
b.place(x=150, y=200)

#LIST OF PRIME NUMBERS
def action():
    primelist.action()

b = Button(window, text='List of Prime Numbers',font=("Arial",10),foreground='white', command=action,bg='red')
b.place(x=150, y=250)

#LIST OF EVEN / ODD
def action():
    listevenodd.action()

b = Button(window, text='List of Even & Odd',font=("Arial",10),foreground='white', command=action,bg='red')
b.place(x=150, y=150)

#LIST OF ARMSTRONG
def action():
    listarm.action()

b = Button(window, text='List of Armstrong',font=("Arial",10),foreground='white', command=action,bg='red')
b.place(x=150, y=100)

window.mainloop()
