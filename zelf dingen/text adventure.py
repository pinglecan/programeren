# Define the story
story = "You are a brave knight on a quest to defeat a fierce dragon. You enter the dragon's lair and see the beast sleeping in front of you. What do you do?"

# Print the story and prompt the user for their next move
print(story)
print("Do you [a]ttack the dragon, [r]un away, or [w]ait for it to wake up?")

# Get the user's next move
move = input("Enter your move: ")

# Handle the user's move
if move == "a":
    print("You attack the dragon with your sword and slay it!")
    print("You are victorious!")
elif move == "r":
    print("You run away from the dragon. It wakes up and chases after you.")
    print("You are unable to outrun the dragon and it catches you. You have been defeated.")
else:
    print("You wait for the dragon to wake up.")
    print("The dragon wakes up and attacks you. You are unable to defend yourself and are defeated.")
