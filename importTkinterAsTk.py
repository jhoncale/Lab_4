import rospy
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import tkinter as tk
from roboticstoolbox import DHRobot, RevoluteDH
import math
import numpy as np
from roboticstoolbox import SerialLink
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from math import cos, sin

    
def joint_publisher():
    global pub
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)

    while not rospy.is_shutdown():
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
        point = JointTrajectoryPoint()
        point.positions = np.radians([-25,-15, -90-20, 20, 0])
        point.time_from_start = rospy.Duration(0.1)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(2)
        return state

def set_positions(positions):
    global pub
    point = JointTrajectoryPoint()
    point.positions = np.radians(positions)
    point.time_from_start = rospy.Duration(0.1)
    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    state.points.append(point)
    pub.publish(state)

def start_publisher():
    rospy.loginfo("Starting publisher")
    state = joint_publisher()
    return state




root = tk.Tk()
root.title("Controlador robot")


image_fondo = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/pngegg.png")
fondo = tk.Label(root, image=image_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)



def change_image(event, button, new_image):
    button.config(image=new_image)

frame_buttons = tk.Frame(root)
frame_buttons.pack(side=tk.TOP, padx=10, pady=10)

image_1 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/home.png")
image_2 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/pos1.png")
image_3 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/pos2.png")
image_4 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/pos3.png")
image_5 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/pos4.png")

image_11 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/home1.png")
image_22 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/pos11.png")
image_33 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/pos22.png")
image_44 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/pos33.png")
image_55 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/pos44.png")


button_1 = tk.Button(frame_buttons, image=image_1, text="Home"      ,command=lambda: set_positions( [-25, -15, -90-20, 20, 0]), bd=0, highlightthickness=0,compound="top")
button_2 = tk.Button(frame_buttons, image=image_2, text="Posición 1",command=lambda: set_positions( [-2, -1, -9-2, 2, 0]), bd=0, highlightthickness=0,compound="top")
button_3 = tk.Button(frame_buttons, image=image_3, text="Posición 2",command=lambda: set_positions( [-250, -150, -900-20,200, 0]), bd=0, highlightthickness=0,compound="top")
button_4 = tk.Button(frame_buttons, image=image_4, text="Posición 3",command=lambda: set_positions( [-265, -175, -980-230, 20, 0]), bd=0, highlightthickness=0,compound="top")
button_5 = tk.Button(frame_buttons, image=image_5, text="Posición 4",command=lambda: set_positions( [-0, -0, -0-20, 20, 0]), bd=0, highlightthickness=0,compound="top")
start_button = tk.Button(frame_buttons, text="Start", command=start_publisher)


button_1.bind("<Enter>", lambda event: change_image(event, button_1, new_image=image_11))
button_1.bind("<Leave>", lambda event: change_image(event, button_1, new_image=image_1))

button_2.bind("<Enter>", lambda event: change_image(event, button_2, new_image=image_22))
button_2.bind("<Leave>", lambda event: change_image(event, button_2, new_image=image_2))

button_3.bind("<Enter>", lambda event: change_image(event, button_3, new_image=image_33))
button_3.bind("<Leave>", lambda event: change_image(event, button_3, new_image=image_3))

button_4.bind("<Enter>", lambda event: change_image(event, button_4, new_image=image_44))
button_4.bind("<Leave>", lambda event: change_image(event, button_4, new_image=image_4))

button_5.bind("<Enter>", lambda event: change_image(event, button_5, new_image=image_55))
button_5.bind("<Leave>", lambda event: change_image(event, button_5, new_image=image_5))


button_1.config(width=300, height=400)
button_2.config(width=300, height=400)
button_3.config(width=300, height=400)
button_4.config(width=300, height=400)
button_5.config(width=300, height=400)
start_button.config(width=root.winfo_width(), height=5)  


start_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
button_1.pack(side=tk.LEFT, padx=10, pady=10)
button_2.pack(side=tk.LEFT, padx=10, pady=10)
button_3.pack(side=tk.LEFT, padx=10, pady=10)
button_4.pack(side=tk.LEFT, padx=10, pady=10)
button_5.pack(side=tk.LEFT, padx=10, pady=10)
start_button.pack()
start_button.lift() 



frame_container = tk.Frame(root)
frame_container.pack(side=tk.BOTTOM, padx=10, pady=10)


frame_extra = tk.LabelFrame(frame_container, text="Integrantes del grupo", highlightbackground=root.cget('bg'), highlightcolor=root.cget('bg'), highlightthickness=0)
frame_extra.pack(side=tk.LEFT, padx=10, pady=10)

image = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/unal.png")
label_imagen = tk.Label(frame_extra, image=image)
label_imagen.grid(row=0, column=0, padx=10, pady=10, rowspan=3)

label_texto1 = tk.Label(frame_extra, text="Valentina Cruz De Paula")
label_texto1.grid(row=0, column=1, padx=10, pady=10)

label_texto2 = tk.Label(frame_extra, text="Oscar Sergio Urrego Riaño")
label_texto2.grid(row=1, column=1, padx=10, pady=10)

label_texto3 = tk.Label(frame_extra, text="Jhon Nelson Cáceres Leal")
label_texto3.grid(row=2, column=1, padx=10, pady=10)



frame_data = tk.LabelFrame(frame_container, text="Datos de los motores")
frame_data.pack(side=tk.LEFT, padx=100, pady=10)

label_motor1 = tk.Label(frame_data, text="Motor 1: ")
label_motor1.pack(padx=10, pady=10)

label_motor2 = tk.Label(frame_data, text="Motor 2: ")
label_motor2.pack(padx=10, pady=10)

label_motor3 = tk.Label(frame_data, text="Motor 3: ")
label_motor3.pack(padx=10, pady=10)

label_motor4 = tk.Label(frame_data, text="Motor 4: ")
label_motor4.pack(padx=10, pady=10)

label_motor5 = tk.Label(frame_data, text="Motor 5: ")
label_motor5.pack(padx=10, pady=10)


motor1 = 0
motor2 = 0
motor3 = 0
motor4 = 0
motor5 = 0

def callback(data):
    
    rospy.loginfo(data.position)
    motor1 = data.position[0]
    motor2 = data.position[1]
    motor3 = data.position[2]
    motor4 = data.position[3]
    motor5 = data.position[4]
    
        
def listener():
    
    rospy.init_node('joint_listener', anonymous=True)
    rospy.Subscriber("/dynamixel_workbench/joint_states", JointState, callback)
    rospy.spin()
    

    try:
        while not rospy.is_shutdown():
            listener()
    except rospy.ROSInterruptException:
        pass

def update_labels():
    label_motor1.config(text="Motor 1: {}".format(motor1))
    label_motor2.config(text="Motor 2: {}".format(motor2))
    label_motor3.config(text="Motor 3: {}".format(motor3))
    label_motor4.config(text="Motor 4: {}".format(motor4))
    label_motor5.config(text="Motor 5: {}".format(motor5))


update_labels()

root.mainloop()