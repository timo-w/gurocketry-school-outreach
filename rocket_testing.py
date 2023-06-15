# GU Rocketry
# Part 3 - Making Decisions using the "If" Statement
from rocket_class import *


# A function to test if the rocket is fit to fly
def test_rocket(rocket):
    has_engine = rocket.has_engine
    has_parachute = rocket.has_parachute
    rats_in_cockpit = rocket.rats_in_cockpit
    crew_members = rocket.crew_members
    fuel_level = rocket.fuel_level

    print(f"--------------------------------\n\n| TESTING {rocket.name} |\n")


    # Check if the rocket's engine is installed
    if has_engine == False:
        print("The rocket doesn't have an engine, we can't launch!")
    

    # Check if the rocket does not have a parachute
    # YOUR ANSWER HERE!

    
    # Check if there are rats in the cockpit
    # YOUR ANSWER HERE!


    # Check the number of crewmates
    if crew_members < 3:
        print("We don't have enough astronauts onboard!")


    # Check if there is more than 90% fuel in the tank
    # YOUR ANSWER HERE!



    print(f"\n--------------------------------\n\n")
    



# Test all the rockets
test_rocket(rocket_1)
test_rocket(rocket_2)
test_rocket(rocket_3)
test_rocket(rocket_4)
test_rocket(rocket_5)

