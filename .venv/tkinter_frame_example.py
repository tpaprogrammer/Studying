import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Tkinter Frame Example")

# Create a frame to group widgets
frame = tk.Frame(root, bg="lightblue", padx=10, pady=10)
frame.pack(padx=20, pady=20)

# Add widgets to the frame
label = tk.Label(frame, text="Enter your name:")
label.pack(pady=5)

entry = tk.Entry(frame)
entry.pack(pady=5)

button = tk.Button(frame, text="Submit")
button.pack(pady=5)

# Add another widget outside the frame
outside_label = tk.Label(root, text="This is outside the frame.")
outside_label.pack(pady=10)

# Run the application
root.mainloop()
