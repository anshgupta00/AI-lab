#"""1) The River Crossing Problem involves a farmer who must take a wolf, a goat, and a cabbage across a river. However, there are constraints:
#The boat can carry only the farmer and one other item (wolf, goat, or cabbage) at a time.
#The wolf cannot be left alone with the goat (the wolf will eat the goat).
#The goat cannot be left alone with the cabbage (the goat will eat the cabbage)."""
#///////////////////////////////////////////////////////////////////////////////////////////////

def river_crossing():
    # Initial state: all on the west bank
    west_bank = {"farmer", "wolf", "goat", "cabbage"}
    east_bank = set()

    # Helper function to print the current state
    def print_state():
        print(f"West Bank: {west_bank}, East Bank: {east_bank}")

    # Rules to check if a state is valid
    def is_valid(bank):
        if "goat" in bank and "wolf" in bank and "farmer" not in bank:
            return False  # Wolf eats the goat
        if "goat" in bank and "cabbage" in bank and "farmer" not in bank:
            return False  # Goat eats the cabbage
        return True

    # Step-by-step solution
    steps = [
        ("goat", "east"),    # Take goat to the east bank
        ("", "west"),        # Return to the west bank alone
        ("wolf", "east"),    # Take wolf to the east bank
        ("goat", "west"),    # Bring goat back to the west bank
        ("cabbage", "east"), # Take cabbage to the east bank
        ("", "west"),        # Return to the west bank alone
        ("goat", "east")     # Take goat to the east bank
    ]

    # Execute steps
    for item, direction in steps:
        if direction == "east":
            if item:
                west_bank.remove(item)
                east_bank.add(item)
            west_bank.remove("farmer")
            east_bank.add("farmer")
        elif direction == "west":
            if item:
                east_bank.remove(item)
                west_bank.add(item)
            east_bank.remove("farmer")
            west_bank.add("farmer")
        
        # Print each step
        print(f"\nFarmer takes {item if item else 'nothing'} to the {direction} bank:")
        print_state()

        # Check validity of each bank
        if not is_valid(west_bank) or not is_valid(east_bank):
            print("Invalid state reached! Something got eaten.")
            return

    print("\nAll items successfully transported to the east bank!")

# Run the solution
river_crossing()
