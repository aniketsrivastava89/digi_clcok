import tkinter as tk
from tkinter import ttk
from time import strftime

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Digital Clock")
        self.root.geometry("400x200")

        self.time_format = tk.StringVar()
        self.time_format.set("12-hour")

        self.create_widgets()

        # Update the time every 1000 milliseconds (1 second)
        self.update_time()

    def create_widgets(self):
        # Time Label
        self.time_label = tk.Label(self.root, font=('calibri', 40, 'bold'), background='black', foreground='white')
        self.time_label.pack(anchor='center')

        # Date Label
        self.date_label = tk.Label(self.root, text="", font=('calibri', 16, 'bold'), background='black', foreground='white')
        self.date_label.pack(anchor='center')

        # Time Format Switch
        self.format_switch = ttk.Combobox(self.root, textvariable=self.time_format, values=["12-hour", "24-hour"])
        self.format_switch.bind("<<ComboboxSelected>>", self.update_time)
        self.format_switch.pack(anchor='center', pady=10)
        self.format_switch.set("12-hour")

    def update_time(self, event=None):
        current_time = strftime('%H:%M:%S' if self.time_format.get() == "24-hour" else '%I:%M:%S %p')
        current_date = strftime('%A, %B %d, %Y')

        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)

        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.configure(background='black')
    root.mainloop()
