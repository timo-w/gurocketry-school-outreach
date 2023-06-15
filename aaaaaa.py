# GU Rocketry - Coding with Rockets
# Part 4 - Putting it All Together
from time import sleep


# Current altitude of the rocket
speed = 0
state = ""


def calculate_state():

    if altitude == 0:
        state = "Sitting on the launchpad..."

    if altitude == 20:
        state = "Entering the stratosphere!"

    if altitude == 100:
        state = "We're now in space!"









# Simulate the rocket launch
for i in range(0, 200, 10):
    altitude = i
    print("Rocket altitude: " + str(altitude) + "km")
    calculate_state()
    sleep(1)

