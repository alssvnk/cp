from tkinter import *
import random
import time
import threading

class Config:
    def __init__(self, stopped=True):
        self.stopped = stopped

config = Config()

def start_threads():
    if config.stopped:
        config.stopped = False
        thread_1 = threading.Thread(target=move_text, args=(1,)).start()
        thread_2 = threading.Thread(target=move_text, args=(2,)).start()
        thread_3 = threading.Thread(target=move_text, args=(3,)).start()

def stop_threads():
    config.stopped = True

def move_text(index):
    if index == 1:
        speed = 0.1
        label = label1
    if index == 2:
        speed = 0.2
        label = label2
    if index == 3:
        speed = 0.3
        label = label3

    x = label.winfo_x()
    y = label.winfo_y()

    shift = 10
    while True:
        if config.stopped:
            break

        if y > 400 or y < 30:
            shift *= -1

        y += shift
        label.place(x=x, y=y)
        time.sleep(speed)

# main window properties;
root = Tk()
root.geometry("1000x500")
root.resizable(0, 0)

# canvas properties;
canvas = Canvas(root, width=1000, height=450)
canvas.pack()
label1 = Label(root, text="Thread 1")
label1.pack()
label1.place(x = 200, y = 100)

label2 = Label(root, text="Thread 2")
label2.pack()
label2.place(x = 500, y = 200)

label3 = Label(root, text="Thread 3")
label3.pack()
label3.place(x = 800, y = 300)

# buttons properties;
button_add = Button(text="START", command=start_threads, width=10)
button_add.pack(side=BOTTOM)
button_add.place(y=20)
button_clear = Button(text="STOP", command=stop_threads, width=10)
button_clear.pack(side=BOTTOM)
button_clear.place(y=60)

# start window;
root.mainloop()