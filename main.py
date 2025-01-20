class AdventureGame:
    def __init__(self):
        self.inventory = []

    def add_to_inventory(self, item):
        print(f"You have obtained: {item}.")
        self.inventory.append(item)

    def show_inventory(self):
        if self.inventory:
            print("\nYour Inventory:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("\nYour inventory is empty.")

    def start_game(self):
        print("""
****************************************************
*                                                  *
*          WELCOME TO THE ADVENTURE GAME!          *
*                                                  *
****************************************************

You wake up in a dense, dark forest. The air is damp, 
and you can hear the distant howl of wolves. In front of you, 
a narrow path splits into two directions.

What will you do?
1. Take the path to the left, which seems well-trodden.
2. Take the path to the right, which disappears into thick bushes.

Choose 1 or 2:
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            self.path_left()
        elif choice == "2":
            self.path_right()
        else:
            print("Invalid choice! The forest seems to grow darker as you hesitate...")

    def path_left(self):
        print("\nYou take the path to the left, hoping it leads to safety...")
        print("After walking for a while, you find an abandoned campsite. There is a lantern on the ground.")
        
        pick_item = input("Will you take the lantern? (yes/no): ").lower()
        if pick_item == "yes":
            self.add_to_inventory("Lantern")
        else:
            print("You leave the lantern behind and continue walking.")

        print("You see a dark cave ahead. Do you want to explore it?")
        explore_cave = input("Enter your choice (yes/no): ").lower()

        if explore_cave == "yes":
            if "Lantern" in self.inventory:
                print("\nYou use the lantern to light your way and safely explore the cave. Inside, you find a treasure chest filled with gold!")
                self.add_to_inventory("Gold Treasure")
            else:
                print("\nIt's too dark to see anything in the cave. You stumble and fall, ending your adventure.")
        else:
            print("\nYou decide to avoid the cave and continue on the path, leaving the mystery behind.")

    def path_right(self):
        print("\nYou push through the thick bushes, not knowing what lies ahead...")
        print("""
        After pushing through the thick underbrush, you stumble into a clearing.
        In the center of the clearing, you see a glowing, ancient-looking artifact 
        resting on a stone pedestal. A voice echoes in your mind:

        "Adventurer, do you wish to claim this artifact? It holds immense power, 
        but great risk comes with it. Choose wisely."
        """)

        sub_choice = input("Will you take the artifact? (yes/no): ").lower()

        if sub_choice == "yes":
            print("""
            As you touch the artifact, a surge of energy courses through your body. 
            You feel invincible, but the power is overwhelming. The forest fades 
            away, and you are transported to another realm, forever bound to the 
            artifact’s will. Your adventure ends here... or does it?
            """)
        elif sub_choice == "no":
            print("""
            You step away from the artifact, deciding it’s not worth the risk. 
            The ground beneath you trembles as the artifact crumbles to dust. 
            The clearing collapses, and you fall into a deep chasm. Your story 
            ends here, swallowed by the unknown.
            """)
        else:
            print("Invalid choice! The artifact glows brighter as the clearing fades into darkness...")

# Start the game
game = AdventureGame()
game.start_game()
