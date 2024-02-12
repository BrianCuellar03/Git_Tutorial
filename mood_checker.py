# Ask the user to input their mood
user_mood = input("How are you feeling today? (happy, sad, excited, tired): ")

# Respond based on the user's input
if user_mood == "happy":
    print("It's great to see you happy!")
elif user_mood == "sad":
    print("I'm sorry to hear that. Hope you feel better soon!")
elif user_mood == "excited":
    print("Wow, that's exciting! Tell me more!")
elif user_mood == "tired":
    print("You should rest. Everyone deserves a break.")
else:
    print("Hmm, I don't know that mood.")

