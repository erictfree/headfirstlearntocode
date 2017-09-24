from tkinter import *

root = Tk()
count = 10

def countdown():
    global root, count


    if count > 0:
        print(count)
        count = count - 1
        root.after(1000, countdown)
    else:
        print('Blastoff')

countdown()
mainloop()
