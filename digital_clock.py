
import time
import tkinter as tk

# Main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x250")
root.resizable(False, False)
root.configure(bg="black")


# Function to display current time and date
def current_time():
    current = time.strftime("%I:%M:%S %p")
    date = time.strftime("%d-%m-%Y")

    label.config(text=current)
    date_label.config(text=date)

    label.after(1000, current_time)


# Time display
label = tk.Label(
    root,
    font=("Calibri", 42, "bold"),
    bg="black",
    fg="cyan"
)
label.pack(pady=(40, 10))

# Date display
date_label = tk.Label(
    root,
    font=("Calibri", 18),
    bg="black",
    fg="white"
)
date_label.pack()

# Start clock
current_time()

# Keep window running
root.mainloop()
