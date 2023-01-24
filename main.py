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

def close():
    pins.cleanup()
    print("Exiting")
    exit()

print("Press 'E' to exit!\nRunning...")

def connect_to_mobile():
    app = flask.Flask(__name__)
    @app.route('/home')
    def home():
        return """<h1>Welcome to rovo 1.0 control panel</h1>
        <h2>Use the buttons below to control the robot</h2>
        <form action="/handle_forward" method="post">
        <input type="submit" value="Forward">
        </form>
        <form action="/handle_backward" method="post">
        <input type="submit" value="Backward">
        </form>
        <form action="/handle_left" method="post">
        <input type="submit" value="Left">
        </form>
        <form action="/handle_right" method="post">
        <input type="submit" value="Right">
        </form>
        <form action="/handle_stop" method="post">
        <input type="submit" value="Stop">
        </form>
        <form action="/handle_exit" method="post">
        <input type="submit" value="Exit">
        </form>
        """
    @app.route('/handle_forward', methods=['POST'])
    def handle_forward():
        forward()
        return """<h1>Welcome to rovo 1.0 control panel</h1>
        <h2>Use the buttons below to control the robot</h2>
        <h2>Robot Forward</h2>
        <form action="/handle_forward" method="post">
        <input type="submit" value="Forward">
        </form>
        <form action="/handle_backward" method="post">
        <input type="submit" value="Backward">
        </form>
        <form action="/handle_left" method="post">
        <input type="submit" value="Left">
        </form>
        <form action="/handle_right" method="post">
        <input type="submit" value="Right">
        </form>
        <form action="/handle_stop" method="post">
        <input type="submit" value="Stop">
        </form>
        </form>
        <form action="/handle_exit" method="post">
        <input type="submit" value="Exit">
        </form>
        """
    @app.route('/handle_backward', methods=['POST'])
    def handle_backward():
        backward()
        return """<h1>Welcome to rovo 1.0 control panel</h1>
        <h2>Use the buttons below to control the robot</h2>
        <h2>Robot Backward</h2>
        <form action="/handle_forward" method="post">
        <input type="submit" value="Forward">
        </form>
        <form action="/handle_backward" method="post">
        <input type="submit" value="Backward">
        </form>
        <form action="/handle_left" method="post">
        <input type="submit" value="Left">
        </form>
        <form action="/handle_right" method="post">
        <input type="submit" value="Right">
        </form>
        <form action="/handle_stop" method="post">
        <input type="submit" value="Stop">
        </form>
        </form>
        <form action="/handle_exit" method="post">
        <input type="submit" value="Exit">
        </form>
        """
    @app.route('/handle_left', methods=['POST'])
    def handle_left():
        left()
        return """<h1>Welcome to rovo 1.0 control panel</h1>
        <h2>Use the buttons below to control the robot</h2>
        <h2>Robot Left</h2>
        <form action="/handle_forward" method="post">
        <input type="submit" value="Forward">
        </form>
        <form action="/handle_backward" method="post">
        <input type="submit" value="Backward">
        </form>
        <form action="/handle_left" method="post">
        <input type="submit" value="Left">
        </form>
        <form action="/handle_right" method="post">
        <input type="submit" value="Right">
        </form>
        <form action="/handle_stop" method="post">
        <input type="submit" value="Stop">
        </form>
        </form>
        <form action="/handle_exit" method="post">
        <input type="submit" value="Exit">
        </form>
        """
    @app.route('/handle_right', methods=['POST'])
    def handle_right():
        right()
        return """<h1>Welcome to rovo 1.0 control panel</h1>
        <h2>Use the buttons below to control the robot</h2>
        <h2>Robot Right</h2>
        <form action="/handle_forward" method="post">
        <input type="submit" value="Forward">
        </form>
        <form action="/handle_backward" method="post">
        <input type="submit" value="Backward">
        </form>
        <form action="/handle_left" method="post">
        <input type="submit" value="Left">
        </form>
        <form action="/handle_right" method="post">
        <input type="submit" value="Right">
        </form>
        <form action="/handle_stop" method="post">
        <input type="submit" value="Stop">
        </form>
        </form>
        <form action="/handle_exit" method="post">
        <input type="submit" value="Exit">
        </form>
        """
    @app.route('/handle_stop', methods=['POST'])
    def handle_stop():
        pins.output(2, pins.LOW)
        pins.output(3, pins.LOW)
        return """<h1>Welcome to rovo 1.0 control panel</h1>
        <h2>Use the buttons below to control the robot</h2>
        <h2>Robot stopped</h2>
        <form action="/handle_forward" method="post">
        <input type="submit" value="Forward">
        </form>
        <form action="/handle_backward" method="post">
        <input type="submit" value="Backward">
        </form>
        <form action="/handle_left" method="post">
        <input type="submit" value="Left">
        </form>
        <form action="/handle_right" method="post">
        <input type="submit" value="Right">
        </form>
        <form action="/handle_stop" method="post">
        <input type="submit" value="Stop">
        </form>
        </form>
        <form action="/handle_exit" method="post">
        <input type="submit" value="Exit">
        </form>
        """
    @app.route('/handle_exit', methods=['POST'])
    def handle_exit():
        close()

    host = '192.168.0.240'

    app.run(host = host, port = 7045)

connect_to_mobile()

pins.cleanup()