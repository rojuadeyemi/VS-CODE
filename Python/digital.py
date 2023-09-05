from time import strftime
from tkinter import Label, Tk

#======= Configuring window =========
window = Tk()
window.title("Aderoju Calc")
window.geometry("2x3")
window.configure(bg="green")
window.resizable(True, True)
clock_label = Label(window, bg="green", fg="white", font = ("Times", 30, 'bold'), relief='flat')
clock_label.place(x = 2, y = 2)

def update_label():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_label)

update_label()
window.mainloop()