import RPi.GPIO as pins
import pygame

pins.setmode(pins.BCM)

# set up pins 2 and 3 as outputs
pins.setup(2, pins.OUT)
pins.setup(3, pins.OUT)

pygame.init()

run = True

def forward():
    pins.output(2, pins.HIGH)
    pins.output(3, pins.HIGH)

def backward():
    pins.output(2, pins.LOW)
    pins.output(3, pins.LOW)

def left():
    pins.output(2, pins.HIGH)
    pins.output(3, pins.LOW)

def right():
    pins.output(2, pins.LOW)
    pins.output(3, pins.HIGH)

print("Press 'E' to exit!\nRunning...")

while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        forward()
    elif keys[pygame.K_s]:
        backward()
    elif keys[pygame.K_a]:
        left()
    elif keys[pygame.K_d]:
        right()

    pygame.time.Clock().tick(60)