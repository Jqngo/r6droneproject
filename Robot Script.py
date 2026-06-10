# Bash these in order to install all modules
# sudo apt update
# sudo apt upgrade
# sudo apt install python3-picamera
# sudo python3 robot.py
# pip3 install keyboard

import gpiozero as gpio 
import keyboard as kb
import picamera

cam = picamera()


motor1 = gpio.Motor(forward=4, backward =5)
motor2 = gpio.Motor(forward=2, backward=3)


#main loop
try:
    while True:
     #ask for input

        if kb.is_pressed("w"):
            motor1.forward()
            motor2.forward()
            print("Move forward")

        elif kb.is_pressed("s"):
            motor1.backward()
            motor2.backward()
            print("Move backward")

        elif kb.is_pressed("a"):
            motor1.forward()
            motor2.backward()
            print("Move left")

        elif kb.is_pressed("d"):
            motor1.backward()
            motor2.forward()
            print("Move right")

        elif kb.is_pressed("e"):
            motor1.stop()
            motor2.stop()
            cam.stop_preview()
            print("Ending script")
            break

        elif kb.is_pressed("c"):
            cam.start_preview()
            print("Starting preview")
        else:
            motor1.stop()
            motor2.stop()
            print("Stop")
    


finally:
    motor1.stop()
    motor2.stop()
