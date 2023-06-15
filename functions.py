# GU Rocketry
# Part 2 - Using Functions
from time import sleep


# A function to prepare the rocket
def prepare():
    print("\n--------------------------------\n\n| PREPARE |\n")
    print("Preparing all systems...")
    sleep(0.5)
    print("Turning on the engine...")
    sleep(0.5)
    print("Calibrating flight sensors...")
    sleep(0.5)
    print("Testing flight computers...")
    sleep(0.5)
    print("Rocket is ready to launch!")
    sleep(2)


# A function to launch the rocket
def launch():
    print("\n--------------------------------\n\n| LAUNCH |\n")
    print("Initiating launch countdown...")
    sleep(0.5)
    for number in range(10, 0, -1):
        print("-", number)
        sleep(1)
    print("Liftoff!")
    sleep(2)


# A function to navigate the rocket to a provided destination
def navigate_to(destination):
    print("\n--------------------------------\n\n| NAVIGATE |\n")
    print("Engaging flight computers...")
    sleep(1)
    print("COMPUTER: NAVIGATING TO " + destination.upper())
    sleep(5)
    print("COMPUTER: ARRIVED AT " + destination.upper() + "")
    sleep(2)


# A function to land the rocket
def land_on(destination):
    print("\n--------------------------------\n\n| LAND |\n")
    print("Deploying parachute...")
    sleep(1)
    print("Extending landing legs...")
    sleep(2)
    print("Rocket has landed on " + destination + "!")


def survey_planet():
    # YOUR CODE HERE
    pass # <- delete me first!



# Where we want the rocket to go
planet = "Mars"


# Call each of the functions
prepare()
launch()
navigate_to(planet)
land_on(planet)