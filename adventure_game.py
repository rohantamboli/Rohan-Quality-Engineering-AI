# This script runs a text-based treasure-hunting adventure game.


def ask_choice(prompt, valid_choices):
    """Keep asking until the player enters one of the allowed choices."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        print(f"Please choose: {', '.join(valid_choices)}.")


def forest_path(player_name):
    """Play the forest route and return True when the player wins."""
    print("\nYou enter the dense forest. A river blocks the path ahead.")
    choice = ask_choice(
        "Do you follow the river or climb a tree? ", {"river", "tree"}
    )

    if choice == "river":
        print("You follow the river to an ancient stone bridge.")
        bridge_choice = ask_choice(
            "Do you cross the bridge or search beneath it? ", {"cross", "search"}
        )
        if bridge_choice == "search":
            print("You find a hidden chest containing the legendary treasure!")
            return True
        print("The bridge collapses. You escape, but the treasure is lost.")
        return False

    print("From the tree, you spot a safe path but disturb a nest of hornets.")
    print("You retreat safely, but must end this attempt without the treasure.")
    return False


def cave_path(player_name):
    """Play the cave route and return True when the player wins."""
    print("\nYou enter the mysterious cave. The passage becomes completely dark.")
    choice = ask_choice(
        "Do you light a torch or proceed in the dark? ", {"torch", "dark"}
    )

    if choice == "torch":
        print("The torch reveals symbols pointing toward a sealed stone door.")
        door_choice = ask_choice(
            "Do you read the symbols or force the door? ", {"read", "force"}
        )
        if door_choice == "read":
            print("The symbols unlock the door. Inside is the legendary treasure!")
            return True
        print("The cave shakes and blocks the exit. Your expedition ends.")
        return False

    print("You lose your way in the darkness and return to the entrance empty-handed.")
    return False


def start_game():
    """Introduce the quest, collect the player's name, and start a route."""
    print("\n=== THE LEGENDARY TREASURE ===")
    player_name = input("Explorer, what is your name? ").strip() or "Explorer"
    print(f"Welcome, {player_name}. Your quest is to find the ancient treasure.")

    path = ask_choice(
        "Choose your path: dark forest or mysterious cave? ", {"forest", "cave"}
    )
    if path == "forest":
        return forest_path(player_name)
    return cave_path(player_name)


def play_game():
    """Run complete adventures until the player decides to stop."""
    while True:
        won = start_game()
        if won:
            print("Congratulations! You completed the quest.")
        else:
            print("The adventure is over for now.")

        replay = ask_choice("Would you like to play again? yes or no: ", {"yes", "no"})
        if replay == "no":
            print("Thank you for playing. Farewell, explorer!")
            break


if __name__ == "__main__":
    play_game()
