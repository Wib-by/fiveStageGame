print("Welcome to Tartaria!")
name = input("Input your name: ")
health = 5
start = (input(f"""Are you ready to proceed, {name}?
Press 1 + Enter to continue, press another otherwise >>> """))

if start == "1":
    pass
else:
    print(f"See you later, adventurer {name}")
    quit()
print("Let us begin \n\n\n")

#STAGE 1!!!

print("""STAGE 1 – The Blackout

The power grid collapses at 2:17 AM. Your apartment goes silent. Your phone shows one notification:

“Signal detected. Rooftop.”

You hear something move in the hallway.""")

choice_1 = str(input("""Choice A: Grab a flashlight and check the hallway

Choice B: Lock the door and head to the rooftop
""")).upper()

if choice_1 == "A":
    print("""Damage: -2 HP
You step into the dark. Something darts past you.
You fall against the wall and scrape your arm.
Nothing's there when you look again.""")
    health -= 2
    
elif choice_1 == "B":
    print("""You ignore the noise. The stairwell door creaks open as you push through.""")
    
print(f"""Health: {health}
Story continues: You reach the rooftop. The city is dark.""")

#STAGE 2!!!

print("""STAGE 2 – The Signal Tower

On the rooftop stands a portable transmitter, blinking red. It wasn’t here before.

The screen reads: “Manual calibration required.”""")

choice_2 = str(input("""Choice A: Touch the transmitter screen.

Choice B: Search the rooftop first.""")).upper()

if choice_2 == "A":
    print("""Damage: -3 HP
The screen sparks. Electricity shoots through your fingers.
The signal stabilizes slightly.""")
    health -= 3
elif choice_2 == "B":
    print("""You find a tool kit behind the water tank.
The signal flickers stronger.""")
    
    print(f"""Health: {health}""")
else:
    print("Invalid choice. You hesitate and lose time.")
    quit()
if health <= 0:
    print(f"""You collapse before completion. The city remains dark.
The signal waits for someone else, health reached {health}.""")
    quit()
else:
    print("""Story continues: The transmitter activates.
A direction appears: NORTH DISTRICT.""")
    
# STAGE 3!!!

print("""STAGE 3 – The Street Below

The streets are empty. Wind pushes debris across the road. A shadow moves between cars.""")

choice_3 = str(input("""Choice A: Run across the open road.

Choice B: Move slowly between buildings.""")).upper()

if choice_3 == "A":
    print("""Damage: -2 HP
Something lunges from under a vehicle.
It claws your leg before retreating.""")
    health -= 2
elif choice_3 == "B":
    print("""You stay close to walls.
The shadow follows but never strikes..""")
    
    print(f"""Health: {health}""")
else:
    print("Invalid choice. You hesitate and lose time.")
    quit()
if health <= 0:
    print(f"""You collapse before completion. The city remains dark.
The signal waits for someone else, health reached {health}.""")
    quit()
else:
    print("""Story continues: You reach the entrance to an underground subway station.""")
    
# STAGE 4!!!

