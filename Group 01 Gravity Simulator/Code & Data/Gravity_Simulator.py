from cgi import test
import functools
from json.tool import main
from pydoc import TextRepr
import tkinter
from tkinter import CURRENT, HORIZONTAL, PhotoImage
from tkinter import BOTH, END
from turtle import width
from matplotlib.pyplot import text
from matplotlib import pyplot
from requests import delete

# Define Window
win = tkinter.Tk()
win.title("Gravity Simulator")
p1 = PhotoImage(file='E:/MTE 19/2-1 Semester (2nd Year Odd)/CSE 2128 Sessional/Group 01 Gravity Simulator/Code & Data/gravity.png')
win.iconphoto(False, p1)
win.geometry("500x650")
win.resizable(0,0)

# Define global variables
time = 0
data = {}
for i in range(1,5):
    data['data_%d' % i] = []

# Functions

# To make the ball move
def move(event):

    if "BALL" in main_canvas_frame.gettags(CURRENT):
        x1 = main_canvas_frame.coords(CURRENT)[0]
        x2 = main_canvas_frame.coords(CURRENT)[2]

        main_canvas_frame.coords(CURRENT, x1, event.y, x2, event.y+10)

        if main_canvas_frame.coords(CURRENT)[3] < 15:
            main_canvas_frame.coords(CURRENT, x1, 5, x2, 15)
        elif main_canvas_frame.coords(CURRENT)[3] > 415:
            main_canvas_frame.coords(CURRENT, x1, 405, x2, 415)

    # Then it will update the height accordingly 
    update_height()

# Changing the heights as per the movement of the balls
def update_height():
    for i in range(1,5):
        height['h_%d' % i].config(text="Height: " + str(round(415 - main_canvas_frame.coords(balls['ball_%d' % i])[3],2)))


# Function for step button
def step_button_func(t):
    global time
    for i in range(1,5):
        a = -1*float(acceleration['a_%d' % i].get())
        u = -1*float(velocity['u_%d' % i].get())

        d = u*t + 0.5*a*t**2

        x1 = main_canvas_frame.coords(balls['ball_%d' % i])[0]
        x2 = main_canvas_frame.coords(balls['ball_%d' % i])[2]

        if main_canvas_frame.coords(balls['ball_%d' % i ])[3] + d <= 415:
            main_canvas_frame.move(balls['ball_%d' % i], 0, d)
            y2 = main_canvas_frame.coords(balls['ball_%d' % i])[3]
            main_canvas_frame.create_line(x1, y2, x2, y2, tag="DASH")
        else:
            main_canvas_frame.coords(balls['ball_%d' % i], x1, 405, x2, 415)
        
        v = u + a*t

        velocity['u_%d' % i].delete(0, END)
        velocity['u_%d' % i].insert(0, str(round(-1*v, 2)))

        data['data_%d' % i].append((time, 415 - main_canvas_frame.coords(balls['ball_%d' %i])[3]))

        update_height()

        time += t

# Function for run button
def run_button_func():
    step_button_func(time_scale.get())

    while 15 < main_canvas_frame.coords(balls['ball_1'])[3] < 415 or 15 < main_canvas_frame.coords(balls['ball_2'])[3] < 415 or 15 < main_canvas_frame.coords(balls['ball_3'])[3] < 415 or 15 < main_canvas_frame.coords(balls['ball_4'])[3] < 415:
        step_button_func(time_scale.get())

# Function for generating graph button
def graph_button_func():
    colors = ['blue', 'green', 'red', 'orange']

    for i in range(1,5):
        x = []
        y = []

        for data_list in data['data_%d' % i]:
            x.append(data_list[0])
            y.append(data_list[1])

        pyplot.plot(x,y, color = colors[i-1])

    pyplot.title('Displacement Vs. Time')
    pyplot.xlabel('Time')
    pyplot.ylabel('Displacement')
    pyplot.show()

# Function for reset button 
def reset_button_func():
    global time
    time = 0

    main_canvas_frame.delete('DASH')

    for i in range(1,5):
        velocity['u_%d' % i].delete(0, END)
        velocity['u_%d' % i].insert(0, '0')
        acceleration['a_%d' % i].delete(0,END)
        acceleration['a_%d' % i].insert(0, '0')

        main_canvas_frame.coords(balls['ball_%d' % i], 45+(i-1)*100, 405, 55+(i-1)*100, 415)

        data['data_%d' % i].clear()

    update_height()
    time_scale.set(0)


# Define Layouts
canvas_frame = tkinter.Frame(win)
function_frame = tkinter.Frame(win)

canvas_frame.pack(pady=10)
function_frame.pack(fill=BOTH, expand=True)

# Canvas Frame Layout 
main_canvas_frame = tkinter.Canvas(canvas_frame, width=400, height=415, bg='white')
main_canvas_frame.grid(row=0, column=0, padx=5, pady=5)

# Lines to seperate ball movement 
line1 = main_canvas_frame.create_line(2,0,2,415)
line2 = main_canvas_frame.create_line(100,0,100,415)
line3 = main_canvas_frame.create_line(200,0,200,415)
line4 = main_canvas_frame.create_line(300,0,300,415)
line5 = main_canvas_frame.create_line(400,0,400,415)
line6 = main_canvas_frame.create_line(0,2,400,2)
line7 = main_canvas_frame.create_line(0,415,415,415)

# Balls
balls = {}
balls['ball_1'] = main_canvas_frame.create_oval(45, 405, 55, 415, fill='blue', tag='BALL')
balls['ball_2'] = main_canvas_frame.create_oval(145, 405, 155, 415, fill='green', tag='BALL')
balls['ball_3'] = main_canvas_frame.create_oval(245, 405, 255, 415, fill='red', tag='BALL')
balls['ball_4'] = main_canvas_frame.create_oval(345, 405, 355, 415, fill='orange', tag='BALL')

# Binding to make balls move
win.bind('<B1-Motion>', move)

# Function Frame Layout

# Row Labels
tkinter.Label(function_frame, text='h').grid(row=0, column=0)
tkinter.Label(function_frame, text='u').grid(row=1, column=0)
tkinter.Label(function_frame, text='a').grid(row=2, column=0, ipadx=20)
tkinter.Label(function_frame, text='t').grid(row=3, column=0)

# Heigts Labeling (H)
height = {}
for i in range(1,5):
    height['h_%d' % i] = tkinter.Label(function_frame, text="Height: " + str(415 - main_canvas_frame.coords(balls['ball_%d' % i])[3]))
    height['h_%d' % i].grid(row=0, column=i)

# Initial velocity Labeling (u)
velocity = {}
for i in range(1,5):
    velocity['u_%d' % i] = tkinter.Entry(function_frame, width=15)
    velocity['u_%d' % i].grid(row=1, column=i, padx=1)
    velocity['u_%d' % i].insert(0, '0')

# Acceleration Labeling (a)
acceleration={}
for i in range(1,5):
    acceleration['a_%d' % i] = tkinter.Entry(function_frame, width=15)
    acceleration['a_%d' % i].grid(row=2, column=i, padx=1)
    acceleration['a_%d' % i].insert(0, '0')

# Time Scale
time_scale = tkinter.Scale(function_frame, from_=0, to=1, tickinterval=0.1, resolution=0.01, orient=HORIZONTAL)
time_scale.grid(row=3, column=1, columnspan=4, sticky='WE')
time_scale.set(0)

# Buttons
run_button = tkinter.Button(function_frame, text='Run', command=run_button_func)
run_button.grid(row=4, column=1, pady=(10,0), sticky='WE')

step_button = tkinter.Button(function_frame, text='Step', command=lambda:step_button_func(time_scale.get()))
step_button.grid(row=4, column=2, pady=(10,0), sticky='WE')

graph_button = tkinter.Button(function_frame, text='Graph', command=graph_button_func)
graph_button.grid(row=4, column=3, pady=(10,0), sticky='WE')

reset_button = tkinter.Button(function_frame, text='Reset', command=reset_button_func)
reset_button.grid(row=4, column=4, pady=(10,0), sticky='WE')

quit_button = tkinter.Button(function_frame, text='Quit', command=win.destroy)
quit_button.grid(row=5, column=1, columnspan=4, sticky="WE")

win.mainloop()