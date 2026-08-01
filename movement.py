# Bash these in order to install all modules

# sudo python3 robot.py


import gpiozero as gpio 
import keyboard as kb

motor1 = gpio.Motor(forward=4, backward =5)
motor2 = gpio.Motor(forward=2, backward=3)


#main loop for controlling movement of the robot using a keyboard
def movement_loop():
    try:
        while True:
            #move forwards
            if kb.is_pressed("w"):
                motor1.forward()
                motor2.forward()
                print("Move forward")
            #move backwards
            elif kb.is_pressed("s"):
                motor1.backward()
                motor2.backward()
                print("Move backward")
            #move left
            elif kb.is_pressed("a"):
                motor1.forward()
                motor2.backward()
                print("Move left")
            #move right
            elif kb.is_pressed("d"):
                motor1.backward()
                motor2.forward()
                print("Move right")
            #ending script
            elif kb.is_pressed("e"):
                motor1.stop()
                motor2.stop()
                print("Ending script")
                break
            
            else:
                motor1.stop()
                motor2.stop()
                print("Stop")
        


    finally:
        motor1.stop()
        motor2.stop()
