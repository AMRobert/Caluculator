from tkinter import *
from tkinter .messagebox import *
def action():
    window = Tk()
    window.geometry('300x300')
    e=Entry(window,width=56,borderwidth=5)
    e.place(x=10,y=80)
    f = Entry(window, width=56, borderwidth=5)
    f.place(x=10, y=10)
    def click():
        #l.place_forget()
        l.destroy()
    def primelist():
        global l
        user_input = e.get()
        user1_input = f.get()
        s1 = str(user_input)
        s2 = str(user1_input)
        s1 = int(s1)
        s2 = int(s2)
        window.update_idletasks()
        maxi = max(s1,s2)
        primes = [True]*(maxi+1)
        primes[0],primes[1] = False,False
        for i in range(2,maxi+1):

            if primes[i]==True:
                j = i+i
                while j<=maxi:
                    primes[j] = False
                    j+=i
        ans = []
        start = min(s1,s2)
        end = max(s1,s2)
        for i in range(start,end+1):
            if primes[i]==True:
                ans.append(str(i))
        l = Label(window, text="Prime Numbers between : "+ ' '.join(ans),wraplength='500')
        l.place(x=10, y=200)

        '''                
        for i in range(s1,s2+1):
            if i>1:
                for j in range(2,i):
                    if(i%j==0):
                        break
                    else:
                        l=Label(window, text="Prime Numbers: ")
                        l.place(x=10,y=200)
        '''


    b = Button(window, text='Check',command=primelist)
    b.place(x=20, y=120)
    b = Button(window, text='Try Another', command=click)
    b.place(x=100, y=120)
    window.mainloop()