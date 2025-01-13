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
    # Expand this branch as before

elif choice == "2":
    print("\nYou push through the thick bushes, not knowing what lies ahead...")
    print("""
    After pushing through the thick underbrush, you stumble into a clearing.
    In the center of the clearing, you see a glowing, ancient-looking artifact 
    resting on a stone pedestal. A voice echoes in your mind:

    "Adventurer, do you wish to claim this artifact? It holds immense power, 
    but great risk comes with it. Choose wisely."

    Will you take the artifact? (yes/no)
    """)
    
    sub_choice = input("Enter your choice (yes or no): ").lower()

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

else:
    print("Invalid choice! The forest seems to grow darker as you hesitate...")