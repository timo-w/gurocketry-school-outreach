# GU Rocketry - Coding with Rockets
# Rocket class and definitions used in part 3

class Rocket:

    def __init__(self, name, hasEngine, hasParachute, ratsInCockpit, fuelLevel, crewMembers):
        self.name = name
        self.has_engine = hasEngine
        self.has_parachute = hasParachute
        self.has_rats_in_cockpit = ratsInCockpit
        self.fuel_level = fuelLevel
        self.crew_members = crewMembers

    def __str__(self):
        return f"--------------------------------\n\n| STATUS OF {self.name.upper()} |\n\nEngine installed:\t\t{self.has_engine}\nHas a parachute:\t\t{self.has_parachute}\nHas rats in the cockpit:\t{self.has_rats_in_cockpit}\nFuel level:\t\t\t{self.fuel_level}%\nNumber of astronauts:\t\t{self.crew_members}\n\n--------------------------------\n"


rocket_1 = Rocket("Saturn V", True, True, False, 100, 3)
rocket_2 = Rocket("Falcon 9", False, True, False, 50, 4)
rocket_3 = Rocket("Saltire-3", True, False, False, 95, 0)
rocket_4 = Rocket("Space Shuttle Columbia", True, True, True, 15, 7)


rocket_5 = Rocket(
    # Name of the rocket
    # rocket.name
    "Delta IV",
    # Does the rocket have an engine?
    # rocket.has_engine
    True,
    # Does the rocket have a parachute?
    # rocket.has_parachute
    True,
    # Are there any rats in the cockpit?
    # rocket.rats_in_cockpit
    False,
    # How much fuel is in the rocket?
    # rocket.fuel_level
    100,
    # How many crew members are onboard?
    # rocket.crew_members
    5
)