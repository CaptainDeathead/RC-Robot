import RPi.GPIO as pins
import threading as tk

pins.setmode(pins.BOARD)

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

def get_input():
    while True:
        key = input()[0]
        if key == "w":
            forward()
        elif key == "s":
            backward()
        elif key == "a":
            left()
        elif key == "d":
            right()
        elif key == "e":
            break

tk.Thread(target=get_input).start()

pins.cleanup()