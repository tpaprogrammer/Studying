def custom_messagebox():
    custom_box = tk.Toplevel()
    custom_box.title("Custom Message Box")
    custom_box.geometry("415x175")
    custom_box.resizable(False, False)
    custom_message = tk.Label(
        custom_box,
        text="This is a custom message box using the Toplevel widget. "
        "The widget is used so that the geometry can be set and "
        "resizability can be turned off.",
        font=("Arial", 14),
        justify="left",
        anchor="nw",
        wraplength=380)
    custom_message.place(x=10, y=8)
    custom_close_button = tk.Button(custom_box, text="Close",
                                    font=("Arial", 14),
                                    command=custom_box.destroy)
    custom_close_button.place(x=205, y=135, anchor="center")

def infobox(event=None):
    custom_box = tk.Toplevel()
    custom_box.title("You Clicked the Frame!")
    custom_box.geometry("415x175")
    custom_box.resizable(False, False)
    custom_message = tk.Label(
        custom_box,
        text="The box appeared because the frame widget was left "
        "clicked. To understand, look for 'frame.bind' below.",
        font=("Arial", 14),
        justify="left",
        anchor="nw",
        wraplength=380)
    custom_message.place(x=10, y=8)
    custom_close_button = tk.Button(custom_box, text="Close",
                                    font=("Arial", 14),
                                    command=custom_box.destroy)
    custom_close_button.place(x=205, y=135, anchor="center")
