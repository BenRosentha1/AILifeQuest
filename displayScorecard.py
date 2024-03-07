"""
This function displays the characters scorecard.
"""
# Display scorecard
def displayScorecard(character):
    # Print the characters name and age
    print("Thanks for playing, heres how you did:")
    print(f"Name:  {list(character.qualities.values())[0]}")
    print(f"Age:  {character.age}", end="\n\n")
    
    # For each of the characteristics of the character
    for k, v in character.characteristics.items():

        # Print the characteristic and the corresponding score/weight
        print(f"{k}:  {v}")