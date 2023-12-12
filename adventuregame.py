#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time

class Player:
    def __init__(self):
        self.inventory = []
        self.progress = 0

def introduction():
    print("Welcome to the Magical Forest Adventure!")
    print("You are on a quest to find the lost artifact hidden deep in the enchanted forest.")
    print("Your choices will shape your destiny. Good luck!\n")

def make_choice(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Choose an option: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def forest_path(player):
    print("You enter the magical forest. The path splits into two.")
    choice = make_choice("Which path will you take?", ["Follow the left path", "Take the right path"])

    if choice == 1:
        print("You chose to follow the left path.")
        player.progress += 1
        encounter_enemy(player)
    else:
        print("You chose to take the right path.")
        player.progress += 2
        discover_cave(player)

def encounter_enemy(player):
    print("As you walk deeper into the forest, you encounter a fierce mythical creature!")
    choice = make_choice("What will you do?", ["Fight", "Run away"])

    if choice == 1:
        print("You decide to fight the creature.")
        print("After a tough battle, you emerge victorious.")
        player.inventory.append("Magical Sword")
        find_artifact(player)
    else:
        print("You choose to run away, but the creature catches up.")
        print("Unfortunately, you are caught, and your adventure ends here.")

def discover_cave(player):
    print("You discover a mysterious cave with a glowing entrance.")
    choice = make_choice("Will you enter the cave?", ["Enter the cave", "Continue exploring the forest"])

    if choice == 1:
        print("You enter the cave and find a hidden passage.")
        player.progress += 1
        find_artifact(player)
    else:
        print("You continue exploring the forest.")
        player.progress += 1
        encounter_enemy(player)

def find_artifact(player):
    print("Congratulations! You have found the lost artifact.")
    print("You successfully completed your quest!")

    if "Magical Sword" in player.inventory:
        print("With the power of the Magical Sword, you are hailed as a hero!")
        print("You have achieved the best ending!")
    else:
        print("Without the proper equipment, your journey is more challenging.")
        print("You have achieved an average ending.")

    print(f"Your inventory: {player.inventory}")
    print(f"Your progress: {player.progress}")

def main():
    player = Player()
    introduction()
    forest_path(player)

if __name__ == "__main__":
    main()

