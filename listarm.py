from tkinter import *
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
    def listarm():
        global l
        user_input = e.get()
        user1_input = f.get()
        s1 = str(user_input)
        s2 = str(user1_input)
        s1 = int(s1)
        s2 = int(s2)
        ans =  []
        window.update_idletasks()
        for i in range(min(s1,s2),max(s1,s2)+1):
            sum = 0
            temp = i
            while temp > 0:
                digit = temp % 10
                sum += digit ** 3
                temp //= 10
            if i == sum:
                ans.append(str(i))
        l = Label(window, text="Armstrong Numbers: "+ ' '.join(ans),wraplength='500')
        l.place(x=10, y=200)

    b = Button(window, text='Check',command=listarm)
    b.place(x=20, y=120)
    b = Button(window, text='Try Another', command=click)
    b.place(x=100, y=120)
    window.mainloop()