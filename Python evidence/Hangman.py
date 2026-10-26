import random

# Word categories
word_categories = {
    "Fruits": ["apple", "banana", "mango", "orange", "grapes", "papaya", "kiwi", "pineapple", "strawberry", "watermelon", "blueberry", "raspberry", "peach", "cherry", "pear", "plum", "apricot", "coconut", "fig", "guava"],
    "Animals": ["tiger", "elephant", "giraffe", "monkey", "rabbit", "zebra", "kangaroo", "panda", "dolphin", "penguin", "lion", "bear", "wolf", "fox", "deer", "horse", "sheep", "goat", "camel", "otter"],
    "Countries": ["england", "france", "brazil", "canada", "japan", "australia", "ireland", "germany", "italy", "spain", "portugal", "sweden", "norway", "finland", "denmark", "netherlands", "belgium", "switzerland", "austria", "poland"],
    "Cars": ["toyota", "honda", "ford", "bmw", "audi", "mercedes", "chevrolet", "nissan", "volkswagen", "hyundai", "vauxhall", "mini", "jaguar", "porsche", "ferrari", "lamborghini", "tesla", "mazda", "subaru", "volvo"],
    "Colors": ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white", "gray", "cyan", "magenta", "teal", "indigo", "violet", "maroon", "beige", "turquoise", "lavender"],
    "Sports": ["soccer", "basketball", "tennis", "cricket", "baseball", "golf", "swimming", "cycling", "volleyball", "rugby", "hockey", "skiing", "snowboarding", "boxing", "wrestling", "badminton", "tabletennis", "karate", "judo", "archery"],
    "Professions": ["doctor", "engineer", "teacher", "nurse", "lawyer", "artist", "chef", "pilot", "scientist", "writer", "musician", "actor", "dancer", "photographer", "architect", "farmer", "mechanic", "plumber", "electrician", "firefighter"],
    "Musical Instruments": ["guitar", "piano", "violin", "drums", "flute", "trumpet", "saxophone", "cello", "clarinet", "harp", "accordion", "banjo", "trombone", "oboe", "bass", "keyboard", "marimba", "xylophone", "ukulele", "bagpipes"],
    "Planets": ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto", "ceres", "eris", "haumea", "makemake", "ganymede", "callisto", "io", "europa", "titan", "triton", "charon"],
    "Food": ["pizza", "burger", "pasta", "sushi", "salad", "sandwich", "taco", "steak", "noodles", "curry",],
    "School Subjects": ["math", "science", "history", "geography", "art", "music", "pe", "computerscience", "drama", "economics", "psychology"],
    "Languages": ["english", "spanish", "french", "german", "italian", "chinese", "japanese", "korean", "arabic", "russian"],
    "Elements": ["hydrogen", "helium", "oxygen", "carbon", "nitrogen", "sodium", "potassium", "calcium", "iron", "gold"],
    "Mythical Creatures": ["dragon", "unicorn", "phoenix", "mermaid", "centaur", "griffin", "werewolf", "vampire", "goblin", "troll"],
    "Social Media Platforms": ["facebook", "twitter", "instagram", "linkedin", "snapchat", "tiktok", "youtube", "whatsapp"],
    "Video Games": ["minecraft", "fortnite", "roblox", "overwatch", "leagueoflegends", "callofduty", "amongus", "apexlegends"]
}

# Hangman drawings
hangman = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

print("Welcome to Hangman!")

# Main replay loop
while True:

    # Randomly choose a category and word
    category = random.choice(list(word_categories.keys()))
    word = random.choice(word_categories[category])

    guessed = []
    wrong_guesses = 0
    max_attempts = 6

    print("\nNew game!")
    print("You have", max_attempts, "wrong guesses available.")
    print("Category:", category)

    # Main game loop
    while wrong_guesses < max_attempts:

        # Display the word with blanks for unguessed letters
        display = ""

        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "

        print(hangman[wrong_guesses])
        print("Word:", display)

        # Check if the player has won
        if all(letter in guessed for letter in word):
            print("Congratulations! You won!")
            print("The word was:", word)
            break

        # Get the player's guess
        guess = input("Guess a letter: ").lower().strip()

        # Validate the guess
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.append(guess)

        # Check the guess
        if guess in word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    else:
        # Runs when the player runs out of attempts
        print(hangman[wrong_guesses])
        print("Game Over!")
        print("The word was:", word)

    # Ask whether the player wants to replay
    play_again = input(
        "\nWould you like to play again? (yes/no): "
    ).lower().strip()

    if play_again not in ["yes", "y"]:
        print("Thanks for playing Hangman!")
        break
