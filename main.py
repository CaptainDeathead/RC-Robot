import RPi.GPIO as pins
import threading as tk
import flask

pins.setmode(pins.BCM)

# set up pins 2 and 3 as outputs
pins.setup(2, pins.OUT)
pins.setup(3, pins.OUT)

def forward():
    pins.output(2, pins.HIGH)
    pins.output(3, pins.HIGH)
    print("Forward")
    pins.output(2, pins.LOW)
    pins.output(3, pins.LOW)

def backward():
    pins.output(2, pins.LOW)
    pins.output(3, pins.LOW)
    print("Backward")
    pins.output(2, pins.LOW)
    pins.output(3, pins.LOW)

def left():
    pins.output(2, pins.HIGH)
    pins.output(3, pins.LOW)
    print("Left")
    pins.output(2, pins.LOW)
    pins.output(3, pins.LOW)

def right():
    pins.output(2, pins.LOW)
    pins.output(3, pins.HIGH)
    print("Right")
    pins.output(2, pins.LOW)
    pins.output(3, pins.LOW)

print("Press 'E' to exit!\nRunning...")

def connect_to_mobile():
    app = flask.Flask(__name__)
    @app.route('/home')
    def home():
        return """<h1>Welcome to rovo 1.0 control panel</h1>
        <h2>Use the buttons below to control the robot</h2>
        <form action="/forward" method="post">
        <input type="submit" value="Forward">
        </form>
        <form action="/backward" method="post">
        <input type="submit" value="Backward">
        </form>
        <form action="/left" method="post">
        <input type="submit" value="Left">
        </form>
        <form action="/right" method="post">
        <input type="submit" value="Right">
        </form>
        <form action="/stop" method="post">
        <input type="submit" value="Stop">
        </form>
        """
    @app.route('/forward', methods=['POST'])
    def forward():
        forward()
        return "Forward"
    @app.route('/backward', methods=['POST'])
    def backward():
        backward()
        return "Backward"
    @app.route('/left', methods=['POST'])
    def left():
        left()
        return "Left"
    @app.route('/right', methods=['POST'])
    def right():
        right()
        return "Right"
    @app.route('/stop', methods=['POST'])
    def stop():
        pins.output(2, pins.LOW)
        pins.output(3, pins.LOW)
        return "Stop"

    host = '192.168.0.240'

    app.run(host = host, port = 7045)

connect_to_mobile()

pins.cleanup()