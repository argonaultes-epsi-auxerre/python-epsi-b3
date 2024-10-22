from tkinter import StringVar, Tk
from tkinter import ttk

class Disk:
    def __init__(self, total, used):
        self.__total = total
        self.__used = used

    def used_perc(self):
        return 0

# command

def calculate_used_perc():
    total = totalVar.get()
    used = usedVar.get()
    disk = Disk(total, used)
    usedPercVar.set(disk.used_perc())


root = Tk()

# utiliser dans les widget Entry
totalVar = StringVar()
usedVar = StringVar()
usedPercVar = StringVar()

# déclarer les widget
totalEntry = ttk.Entry(root, textvariable=totalVar)