# Adventure Game: Castle Blackthorn
# A simple text-based adventure game where the player explores a castle
import time
import random


def print_pause(message, delay=2):
    print(message)
    time.sleep(delay)


def valid_input(prompt, options):
    response = input(prompt).lower()
    while response not in options:
        options_str = ', '.join(options)
        response = input(f"Please enter {options_str}: ").lower()
    return response


def intro():
    print_pause("You stand before the towering gates of Castle Blackthorn.")
    print_pause("Legends say a fierce guardian lurks within its halls.")
    print_pause("To your left is an ancient forest, rumored to hide a magical"
                " shield.")
    print_pause("Armed only with a simple torch, you feel both anxious and "
                "excited.")


def choose_guardian():
    return random.choice(["dragon", "undead knight", "cunning warlock"])


def explore_forest(inventory):
    print_pause("You slip into the shadowy forest.")
    if "shield" in inventory:
        print_pause("You've already retrieved the magical shield here; it "
                    "glints at your side.")
    else:
        print_pause("You push vines aside and find a rune-etched shield on a "
                    "stone!")
        inventory.append("shield")
        print_pause("You strap the shield to your arm. It feels sturdy and "
                    "light.")
    print_pause("You make your way back to the castle gates.")
    return inventory


def storm_gate(guardian, inventory):
    print_pause(f"You stride up to the castle gate and the {guardian} "
                "emerges!")
    print_pause("It roars a challenge and prepares to strike.")
    if "shield" in inventory:
        print_pause("You raise your magical shield—its runes glow and the "
                    "attack harmlessly deflects!")
        print_pause("Seizing your chance, you dash past and conquer the "
                    "guardian!")
        return True

    print_pause("You swing your torch, but it’s no weapon…")
    print_pause("The guardian laughs, then readies its attack.")
    if random.choice([True, False]):
        print_pause("By fortune’s favor, you land a lucky blow!")
        return True

    print_pause("The guardian overwhelms you with a powerful strike.")
    return False


def field(guardian, inventory):
    print_pause("\nEnter 1 to approach the castle gate.")
    print_pause("Enter 2 to explore the nearby forest.")
    choice = valid_input("What will you do? (1 or 2)\n", ["1", "2"])

    if choice == "1":
        win = storm_gate(guardian, inventory)
        if win:
            print_pause("You’ve defeated the guardian and claimed the castle! "
                        "YOU WIN!")
        else:
            print_pause("You have fallen in battle. GAME OVER.")
    else:
        inventory = explore_forest(inventory)
        field(guardian, inventory)


def play_game():
    guardian = choose_guardian()
    inventory = []
    intro()
    field(guardian, inventory)


def main():
    print(" Welcome to Castle Blackthorn! ")
    while True:
        play_game()
        again = valid_input("\nPlay again? (y/n)\n", ["y", "n"])
        if again == "n":
            print_pause("Farewell, brave adventurer!", delay=1)
            break


if __name__ == "__main__":
    main()
