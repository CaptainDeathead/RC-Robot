import PiRelay
import flask

r1 = PiRelay.Relay("RELAY1")
r2 = PiRelay.Relay("RELAY2")
r3 = PiRelay.Relay("RELAY3")
r4 = PiRelay.Relay("RELAY4")

def forward():
    r1.on()
    r2.on()
    print("Forward")

def backward():
    r1.off()
    r2.off()
    print("Backward")

def left():
    r1.on()
    r2.off()
    print("Left")

def right():
    r1.off()
    r2.on()
    print("Right")

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
        """
    @app.route('/handle_stop', methods=['POST'])
    def handle_stop():
        backward()
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
        """

    host = '192.168.0.240'

    app.run(host = host, port = 7045)

connect_to_mobile()