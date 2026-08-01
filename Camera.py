#stolen from https://github.com/shillehbean
from picamera2 import Picamera2
import cv2

### You can donate at https://www.buymeacoffee.com/mmshilleh 

camera = Picamera2()
camera.configure(
    camera.create_preview_configuration(
        main={"format": 'XRGB8888', "size": (640, 480)}
            )
            )
camera.start()

def generate_frames():
    while True:
        frame = camera.capture_array()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')