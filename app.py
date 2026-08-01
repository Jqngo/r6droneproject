#stolen from https://github.com/shillehbean
from flask import Flask, Response
from camera import generate_frames
from movement import movement_loop
from threading import Thread


### You can donate at https://www.buymeacoffee.com/mmshilleh 

app = Flask(__name__)
Thread(target=movement_loop, daemon=True).start()

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
