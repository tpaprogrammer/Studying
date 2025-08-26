import tkinter as tk

"""Use the method '.tk()' to create the Main Window object."""
window = tk.Tk()

"""Create a Label object."""
label = tk.Label(window, text="Little label:")

"""This tutorial uses the '.pack()' method. There are three methods:
        - .place()  -> coordinate-based placement of each object
            - This method is invoked from within the widget's object,
            not the window, as the widget is always aware of the window
            it belongs to due to the constructor's first argument.
        - .grid()   -> distribution of widgets is modeled inside the
        manager
            - You are only able to view the final arrangement.
            - You do not need to declare the number of rows and columns
            in advance, the method identifies what is needed.
        - .pack()   -> packs subsequent widgets, in order, into the
        window's interior
            - Quickest, but 'sloppiest' and least intuitive.
"""
label.pack()

"""None of the example code utilizes color changing, examples follow:

button = tk.Button(window, text="Button #1",
                   bg="MediumPurple",
                   fg="LightSalmon",
                   activeforeground="LavenderBlush",
                   activebackground="HotPink")

button = tk.Button(window, text="Button #1",
                   bg="#9370DB",
                   fg="#FFA07A",
                   activeforeground="#FFF0F5",
                   activebackground="#FF69B4")
"""

"""Create a Frame object.

A Frame object is an area border in which widgets are placed. See
tkinter_frame_example.py for details on how to use.
"""

frame = tk.Frame(window, height=30, width=100, bg="#000099")
frame.pack()

"""Create a Button object."""
button = tk.Button(window, text="Button")

"""
The 'fill' argument is used in the .pack() geometry manager, not
directly in the button constructor. It specifies how a widget should
expand to fill the available space in its container (parent widget).

Here’s how the fill argument works:

fill='x': The widget will expand horizontally to fill the width of its
    container.
fill='y': The widget will expand vertically to fill the height of its
    container.
fill='both': The widget will expand both horizontally and vertically to
    fill the entire space of its container.
fill=None (default): The widget will not expand in any direction.
"""
button.pack(fill=tk.X)

"""Create a Switch object.

The switch below is designed to hold an IntVar class object, which is
designed to store inger values. A regular variable cannot be used.
IntVar objects are used by TKinter to organize internal communication
between different widgets.

Other examples of what can be used within a switch (per Bing) include
a BooleanVar for binary states, Direct State Management (No Variable)
and a custom class or function.

The switch below is referenced by both the following CheckButton and
RadioButton objects. As a result, checking/unchecking the CheckButton
also and unavoidably changes the RadioButtons' state(s) and vice versa.
To control separate widgets, additional switches would be used.
"""

switch = tk.IntVar()

"""Set the initial state of the switch."""
switch.set(1)

"""Create a CheckButton object."""
checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
checkbutton.pack()

"""Create an Entry object.

An Entry object is designed to let the user enter simple, one-line data
(i.e. single numbers, names, addresses, etc.)
"""

entry = tk.Entry(window, width=30)
entry.pack()

"""Create a RadioButton object.

While CheckButton objects are solitary, RadioButton objects always work
in groups and only one of the elements inside the group can be checked.
"""
radiobutton_1 = tk.Radiobutton(window, text="Steak", variable=switch, value=0)
radiobutton_1.pack()
radiobutton_2 = tk.Radiobutton(window, text="Salad", variable=switch, value=1)
radiobutton_2.pack()

"""Include the following line at the end of the file to initiate the
GUI.
"""

window.mainloop()
