from tkinter import  *

def click_me():
    print(i.get())
    print("dupa")

root = Tk()

i = StringVar()
c = Checkbutton(root, text="item 1", variable=i, offvalue=None, onvalue="checked")
c.pack()

button = Button(root, text="click me", command=click_me)
button.pack()
root.geometry("300x300+120+120")
root.mainloop()


