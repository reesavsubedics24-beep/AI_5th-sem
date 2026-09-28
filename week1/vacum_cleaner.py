# Vacuum Cleaner Problem
# Goal-Based Agent

def vacuum_cleaner(room_A, room_B, position):

    print("Initial State:")
    print("Room A:", room_A)
    print("Room B:", room_B)
    print("Vacuum Position:", position)
    print()

    # Continue until both rooms are clean
    while room_A == "Dirty" or room_B == "Dirty":

        # If vacuum is in Room A
        if position == "A":

            if room_A == "Dirty":
                print("Vacuum is in Room A")
                print("Action: SUCK")
                room_A = "Clean"

            else:
                print("Room A is already clean")
                print("Action: MOVE RIGHT")
                position = "B"

        # If vacuum is in Room B
        elif position == "B":

            if room_B == "Dirty":
                print("Vacuum is in Room B")
                print("Action: SUCK")
                room_B = "Clean"

            else:
                print("Room B is already clean")
                print("Action: MOVE LEFT")
                position = "A"

    print()
    print("Final State:")
    print("Room A:", room_A)
    print("Room B:", room_B)
    print("Vacuum Position:", position)
    print("Goal Achieved: Both rooms are clean!")


# Initial state
room_A = input("Enter status of Room A (Clean/Dirty): ").capitalize()
room_B = input("Enter status of Room B (Clean/Dirty): ").capitalize()
position = input("Enter vacuum position (A/B): ").upper()

vacuum_cleaner(room_A, room_B, position)