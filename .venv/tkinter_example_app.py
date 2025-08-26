import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox
from message_class import CustomMessageBox


window = tk.Tk()
window.geometry("800x600")
window.configure(bg="gray20")
window.title("My Awesome App")
window.resizable(False, False)


def open_new_window():
    new_window = Toplevel(window)
    new_window.title("New Window")
    new_window.geometry("300x200")
    tk.Label(new_window, text="This is a new window").pack(pady=20)

def clicked():
    messagebox.showinfo("Messagebox",
                        "This is a standard messagebox widget.\n\n"
                        "You cannot set the geometry parameters " +
                        "or turn off \nresizability.")

def frame_clicked(event=None):
    CustomMessageBox(
        "You Clicked the Frame!",
        ("The box appeared because the frame widget was "
         "left clicked.")
    )

def button_two_clicked(event=None):
    CustomMessageBox(
        "You clicked 'Button Two'!",
        ("This is a custom message box using the Toplevel widget. "
         "The widget is used instead of the MessageBox widget to be "
         "able to set the size of the window and prohibit "
         "resizability.")
    )
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", font="Arial", menu=file_menu)
file_menu.add_command(label="Open New Window", font="Arial",
                      command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

label = tk.Label(window, text="This is the BEST label ever.",
                 font=("Arial", 20), padx=20, bg="gray90",
                 highlightbackground="gray50", highlightthickness=3)
label.place(x=400, y=50, anchor="center")

frame = tk.Frame(window, height="300", width="600", bg="gray90",
                 highlightbackground="gray50", highlightthickness=3)
frame.place(x=400, y=250, anchor="center")
frame.bind("<Button-1>", frame_clicked)

button_one = tk.Button(window, text="An amazing button",
                       font=("Arial", 18), command=clicked)
button_one.place(x=100, y=425, anchor="nw")
button_two = tk.Button(window, text="Another amazing button",
                       font=("Arial", 18), command=button_two_clicked)
button_two.place(x=420, y=425, anchor="nw")

switch1 = tk.IntVar().set(0)
switch2 = tk.IntVar().set(0)
switch3= tk.IntVar().set(0)

tk.Checkbutton(window, text="Check me!", variable=switch1).place(x=125, y=124)
tk.Checkbutton(window,
               text="Maybe don't check me?",
               variable=switch2).place(x=125, y=150)

entry = tk.Entry(window, width=30).place(x=125, y=350)

radiobutton1 = tk.Radiobutton(window, text="Radio Option 1",
                              variable=switch3, value=0)
radiobutton1.place(x=375, y=324)

radiobutton2 = tk.Radiobutton(window, text="Radio Option 2",
                              variable=switch3, value=1)
radiobutton2.place(x=375, y=350)

window.mainloop()
