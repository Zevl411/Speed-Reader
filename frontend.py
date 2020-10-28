import tkinter as tk
from tkinter import *
import time


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.count = 0
        self.txt_speed = 200
        self.textLabel.after(1000, self.say_hi)

    def create_widgets(self):
        global var
        var = StringVar()
        self.textLabel = tk.Label(self, textvariable = var)
        self.textLabel.pack(side="top")
        # Button to Play/Pause
        self.pause = tk.Button(self, text="PLAY/PAUSE", fg="black",
                              command=self.pause_txt)
        self.pause.pack(side="bottom")
        # Button to terminate program
        self.quit = tk.Button(self, text="QUIT", fg="black",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        list = ["hi", "my", "name", "is", "pablo", "mf"]
        if self.count < len(list):
            if self.txt_speed > 0:
                var.set(list[self.count])
                self.textLabel.after(self.txt_speed, self.say_hi) # call this method again in 1,000 milliseconds
                self.count += 1
            else:
                self.textLabel.after(self.txt_speed, self.say_hi) # call this method again in 1,000 milliseconds

    def pause_txt(self):
        if self.txt_speed > 0:
            self.txt_speed = 0
        else:
            self.txt_speed = 200

root = tk.Tk()
root.geometry("500x500")
app = Application(master=root)
app.mainloop()
