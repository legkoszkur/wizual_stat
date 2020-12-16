import tkinter as tk

window = tk.Tk()

window.geometry('700x700')
window.title("Welcome to LikeGeeks app")
window.state('disabled')

buttons_frame = tk.LabelFrame(window, bg="white", text="Data setings")
buttons_frame.place(relx=0.005, rely=0.76, relwidth=0.99, relheight=0.18)

Load_data = tk.Button(window, text="Load")
Load_data.place(relx=0.3, rely=0.1, relheight=0.6, relwidth=0.1)



window.mainloop()