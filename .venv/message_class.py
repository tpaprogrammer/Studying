import tkinter as tk

class CustomMessageBox:
    def __init__(self, title, message):
        self.window = tk.Toplevel()
        self.window.title(title)
        self.window.geometry("415x175")
        self.window.resizable(False, False)

        self.message_label = tk.Label(
            self.window,
            text=message,
            font=("Arial", 14),
            justify="left",
            anchor="nw",
            wraplength=380
        )
        self.message_label.place(x=10, y=8)

        self.close_button = tk.Button(
            self.window,
            text="Close",
            font=("Arial", 14),
            command=self.window.destroy
        )
        self.close_button.place(x=205, y=135, anchor="center")

