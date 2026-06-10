import picamera
cam = PiCamera()
import keyboard as kb

while True:
	if kb.is_pressed == "c":
		cam.start_preview()
		print("Starting preview")
		
	elif kb.is_pressed == "x":
		cam.stop_preview()
		print("Stopping preview")
		break
		
