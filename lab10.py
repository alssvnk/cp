from tkinter import *

class Config:
    def __init__(self, color=None, figure=None, draw=None):
        self.color = color # 1=Red, 2=Blue, 3=Green;
        self.figure = figure # 1=Rhombus, 2=Square, 3=Сircle, 4=Star;
        self.draw = draw # 1=ON, 0=OFF;

program = Config()

def update_config():
    program.color = color_value.get()
    program.figure = figure_value.get()
    program.draw = draw_value.get()

def draw_smth(event):
    canvas.delete("all")
    colors = ["red", "blue", "green"]

    if program.draw == 1:
        if program.figure == 1:
            rhombus = canvas.create_polygon((500, 200), (550, 250), (500, 300), (450, 250), fill=colors[program.color - 1])
        elif program.figure == 2:
            square = canvas.create_polygon((450, 200), (550, 200), (550, 300), (450, 300), fill=colors[program.color - 1])
        elif program.figure == 3:
            circle = canvas.create_oval(450, 200, 550, 300, fill=colors[program.color - 1])
        elif program.figure == 4:
            star = canvas.create_polygon((500, 100), (440, 288), (590, 168), (410, 168), (560, 288), fill=colors[program.color - 1])



# main window properties;
root = Tk()
root.geometry("500x300")
root.resizable(0, 0)

# main window frames;
colors_frame = Frame()
colors_frame.pack()
figures_frame = Frame()
figures_frame.pack()

# radiobuttons properties;
color_value = IntVar()
figure_value = IntVar()
colors_label = Label(colors_frame, text="Select a color:")
colors_label.pack()
radiobutton_color_red = Radiobutton(colors_frame, text="Red", value=1, variable=color_value, command=update_config)
radiobutton_color_red.pack(side=LEFT)
radiobutton_color_blue = Radiobutton(colors_frame, text="Blue", value=2, variable=color_value, command=update_config)
radiobutton_color_blue.pack(side=LEFT)
radiobutton_color_green = Radiobutton(colors_frame, text="Green", value=3, variable=color_value, command=update_config)
radiobutton_color_green.pack(side=LEFT)
extra_label = Label(figures_frame, text="", height=2)
extra_label.pack()
figures_label = Label(figures_frame, text="Select a figure:")
figures_label.pack()
radiobutton_figure_rhombus = Radiobutton(figures_frame, text="Rhombus", value=1, variable=figure_value, command=update_config)
radiobutton_figure_rhombus.pack(side=LEFT)
radiobutton_figure_square = Radiobutton(figures_frame, text="Square", value=2, variable=figure_value, command=update_config)
radiobutton_figure_square.pack(side=LEFT)
radiobutton_figure_circle = Radiobutton(figures_frame, text="Сircle", value=3, variable=figure_value, command=update_config)
radiobutton_figure_circle.pack(side=LEFT)
radiobutton_figure_star = Radiobutton(figures_frame, text="Star", value=4, variable=figure_value, command=update_config)
radiobutton_figure_star.pack(side=LEFT)
draw_value = IntVar()
checkbox_draw = Checkbutton(text="Draw", variable=draw_value, onvalue = 1, offvalue = 0, height=5, width = 20, command=update_config)
checkbox_draw.pack()

# second window properties;
second_window = Toplevel(root)
second_window.geometry("1000x500")
second_window.resizable(0, 0)
second_window.bind("<Button-1>", draw_smth)

# second window canvas properties;
canvas = Canvas(second_window, width=1000, height=500, bg="white")

canvas.pack()

# start window;
root.mainloop()