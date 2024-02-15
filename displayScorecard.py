def displayScorecard(character):
    print("Thanks for playing, heres how you did:")
    print(f"Name:  {list(character.qualities.values())[0]}")
    print(f"Age:  {character.age}", end="\n\n")
    
    for k, v in character.characteristics.items():
        print(f"{k}:  {v}")