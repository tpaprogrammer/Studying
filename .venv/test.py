import tkinter as tk


def on_off():
    global switch
    if switch:
        mathz_button.configure(command=do_mathz)
        mathz_button.configure(text="Do Mathz Now =)")
    else:
        mathz_button.configure(command=lambda: None)
        mathz_button.configure(text="No Do Mathz >=(")
    switch = not switch

def do_mathz():
    mathz_window = tk.Toplevel()
    mathz_window.geometry("400x200")
    mathz_window.title("Doing the Mathz Now")
    mathz_window.resizable(False, False)
    message = tk.Label(mathz_window, text="The Mathz iz Did.",
                       font=("Arial", 14)
                       ).place(x=200, y=100, anchor="center")

switch = True


main_window = tk.Tk()
main_window.geometry("800x600")
main_window.title("Maybe Do The Mathz?")
main_window.resizable(False, False)

frame = tk.Frame(main_window,
                 width="750",
                 height="550",
                 bg="gray50"
                 ).place(x=400, y=300, anchor="center")

toggle = tk.Button(main_window, text="Mathz Toggler",
                   font=("Arial", 14),
                   command=on_off
                   )
toggle.place(x=108, y=108)

mathz_button = tk.Button(main_window, text="No Do Mathz >=(",
                         font=("Arial", 14),
                         command=lambda: None
                         )
mathz_button.place(x=108, y=150)

main_window.mainloop()