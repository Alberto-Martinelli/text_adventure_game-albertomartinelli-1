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
    print("\nYou take the path to the left, hoping it leads to safety...")
    print("""
    After a long walk, you find yourself at the edge of a misty lake. 
    A ferryman waits silently, offering to take you across. 
    He holds out his hand, demanding payment. 
    You have two choices:

    1. Pay the ferryman with a gold coin you found earlier in the forest.
    2. Refuse to pay and attempt to swim across.
    """)
    sub_choice = input("Enter your choice: ")

    if sub_choice == "1":
        print("""
        The ferryman silently takes the coin and rows you across the lake. 
        As you reach the far shore, he whispers, 
        "Beware the shadow in the castle ahead." 
        You walk toward the castle, where you must now confront an ancient curse.
        
        Inside the castle, you meet a mysterious figure who offers to lift the curse 
        in exchange for a piece of your soul. What will you do?
        1. Agree to give up part of your soul.
        2. Refuse and attempt to destroy the curse yourself.
        """)
        castle_choice = input("Enter your choice: ")
        if castle_choice == "1":
            print("""
            You agree to the deal. The curse is lifted, and the castle crumbles. 
            However, you feel a deep emptiness inside, as part of your soul 
            has been lost forever. Your journey continues, but you are now 
            forever changed.
            """)
        elif castle_choice == "2":
            print("""
            You refuse the deal and confront the curse head-on. 
            The battle is grueling, and though you destroy the curse, 
            you are mortally wounded. You collapse as the castle fades 
            into the mist. Your adventure ends here.
            """)
        else:
            print("Invalid choice! The curse consumes you as the figure disappears.")

    elif sub_choice == "2":
        print("""
        You attempt to swim across the lake, but the water is freezing, 
        and strange creatures lurk beneath the surface. You are dragged underwater, 
        and your adventure ends here.
        """)

    else:
        print("Invalid choice! The ferryman vanishes, and you are left stranded by the lake.")

elif choice == "2":
    print("\nYou push through the thick bushes, not knowing what lies ahead...")
    print("""
    After emerging from the bushes, you find a hidden shrine guarded by a spectral figure. 
    The figure speaks: 
    "This shrine holds the power to alter destiny. To claim it, you must pass a trial."

    Will you:
    1. Accept the trial.
    2. Refuse and continue on your way.
    """)
    shrine_choice = input("Enter your choice: ")

    if shrine_choice == "1":
        print("""
        You accept the trial, and the spectral figure explains the rules. 
        You must solve three riddles or face eternal imprisonment. 
        The first riddle is: 
        "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?"
        """)
        answer = input("Enter your answer: ").lower()
        if answer == "echo":
            print("""
            Correct! The spectral figure nods and presents the second riddle: 
            "The more of this there is, the less you see. What is it?"
            """)
            answer2 = input("Enter your answer: ").lower()
            if answer2 == "darkness":
                print("""
                Correct again! The spectral figure presents the final riddle: 
                "I’m always in front of you but can’t be seen. What am I?"
                """)
                answer3 = input("Enter your answer: ").lower()
                if answer3 == "future":
                    print("""
                    You have passed the trial! The shrine grants you the power to alter one event in your past. 
                    You choose to undo a past mistake, changing your fate forever. 
                    The forest disappears, and you awaken in a new reality.
                    """)
                else:
                    print("Wrong! The spectral figure banishes you to the void. Your adventure ends here.")
            else:
                print("Wrong! The spectral figure banishes you to the void. Your adventure ends here.")
        else:
            print("Wrong! The spectral figure banishes you to the void. Your adventure ends here.")

    elif shrine_choice == "2":
        print("""
        You refuse the trial and walk deeper into the forest. 
        You find an abandoned campsite with supplies, but night falls quickly. 
        Wolves begin to circle the area, and you must decide:

        1. Climb a tree to stay safe.
        2. Light a fire to scare the wolves away.
        """)
        wolf_choice = input("Enter your choice: ")

        if wolf_choice == "1":
            print("""
            You climb a tree and wait for the wolves to leave. 
            As dawn breaks, you find a map carved into the tree trunk, 
            leading to a hidden treasure. Your journey continues.
            """)
        elif wolf_choice == "2":
            print("""
            You light a fire, scaring off the wolves, but the smoke attracts 
            a group of hostile bandits. Outnumbered and unarmed, your adventure ends here.
            """)
        else:
            print("Invalid choice! The wolves close in as you hesitate...")

    else:
        print("Invalid choice! The shrine disappears, and you are left wandering aimlessly.")

else:
    print("Invalid choice! The forest seems to grow darker as you hesitate...")
