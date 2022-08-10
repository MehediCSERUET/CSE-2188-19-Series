# Gravity-Simulator Application
Gravity Simulator Application is a project developed under the course CSE 2188, Software Engineering Sessional. This app is developed by a group of students from the department of Mechatronics Engineering, Rajshahi University of Engineering & Technology (RUET). The main inspiration of the Application was from a Reddit post. This project is from Grooup-01 and the members are S. M. Khalid Bin Zahid (1908001), Najeeb Ahmed Bhuiyan (1908002), Puja Mazumdar (1908003), Hameem Julfiqar (1908004) & Tamzid-Ul-Islam (1908005). 

## Gravity Simulator
A gravity simulator application is an application which basically simulates the effect of gravity on falling objects at certain heights, much like our real word. It uses Newton’s laws of gravity in order to make the simulation. Not only the simulator can simulate gravitational force like our earth, but also it can simulate the gravitational force same as that in other celestial bodies also.

## Features of Gravity Simulator
The following are key features of the Application are:
- Keeps track of the position of the falling object at certain intervals of time. 
- Shows the path of the falling of the object.
- Users can set the parameters such as, height, initial velocity, acceleration and time interval as per their wish.
- It can simulate the falling of multiple objects at the same time.
- This application can also generate the displacement vs time graph of the falling objects after the simulation.

## Tools in Building the Application
We have used:
- Python [Main Programming Language]
- Tkinter [To create the GUI]
- Matplotlib [To generate the graph]

## Demonstration of the Application
Here's the full demonstration of the Gravity Simulator Application!

## Parameters & Meaning
- `h` denotes the *height* and it sets when the user drags the ball using the mouse in the canvas.
- `u` denotes the *initial velocity* and for each ball the user has to set the value manually. Note: Velocity in the upwards direction is (+) and downwards direction is (-).
- `a` denotes the *acceleration* and for each ball the user has to set the value manually. Note: Acceleration in the upwards direction is (+) and downwards direction is (-).
- `t` denotes the *time interval* and using the slider the user can give the required input from `0 to 1` (But do not input `0` otherwise the application might crash).

## Buttons & Usage

- `Step` Button makes step by step simulation.
- `Run` Button makes the whole simulation at once.
- `Graph` Button generates a **Displacement Vs. Time** curve of each of the balls.
- `Reset` Button resets all the parameters to its initial value.
- `Quit` Button makes the user get an exit from the Application.

## Usage of Gravity Simulator Application
There are dynamic usage of the application but it is most commonly used in:
- Astrophysics
- Understanding the Motion Equations
- Free Falling Body Experiment Simulation & Calculation
- Making Physics Interesting
And many more!

## Conclusion

As the Gravity Simulator was developed by the students of Mechatronics Engineering, it was kept in mind that whether proper synergistic integration between different fields were made. In our 2nd Year, Odd Semester, we have studied *Kinematics of Particles* under the course *ME 2155*. And the laws and equations studied there is implemented in this Application as we use the Motion equations to make the simulations. 