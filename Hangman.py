import random
words_list = [
    "able", "about", "account", "acid", "across", "act", "addition", "adjustment", 
    "advertisement", "after", "again", "against", "agreement", "air", "all", 
    "almost", "among", "amount", "amusement", "and", "angle", "angry", "animal", 
    "answer", "ant", "any", "apparatus", "apple", "approval", "arch", "argument", 
    "arm", "army", "art", "as", "at", "attack", "attempt", "attention", "attraction", 
    "authority", "automatic", "awake", "baby", "back", "bad", "bag", "balance", 
    "ball", "band", "base", "basin", "basket", "bath", "be", "beautiful", "because", 
    "bed", "bee", "before", "behaviour", "belief", "bell", "bent", "berry", 
    "between", "bird", "birth", "bit", "bite", "bitter", "black", "blade", "blood", 
    "blow", "blue", "board", "boat", "body", "boiling", "bone", "book", "boot", 
    "bottle", "box", "boy", "brain", "brake", "branch", "brass", "bread", "breath", 
    "brick", "bridge", "bright", "broken", "brother", "brown", "brush", "bucket", 
    "building", "bulb", "burn", "burst", "business", "but", "butter", "button", 
    "by", "cake", "camera", "canvas", "card", "care", "carriage", "cart", "cat", 
    "cause", "certain", "chain", "chalk", "chance", "change", "cheap", "cheese", 
    "chemical", "chest", "chief", "chin", "church", "circle", "clean", "clear", 
    "clock", "cloth", "cloud", "coal", "coat", "cold", "collar", "colour", "comb", 
    "come", "comfort", "committee", "common", "company", "comparison", "competition", 
    "complete", "complex", "condition", "connection", "conscious", "control", "cook", 
    "copper", "copy", "cord", "cork", "cotton", "cough", "country", "cover", "cow", 
    "crack", "credit", "crime", "cruel", "crush", "cry", "cup", "current", "curtain", 
    "curve", "cushion", "damage", "danger", "dark", "daughter", "day", "dead", 
    "dear", "death", "debt", "decision", "deep", "degree", "delicate", "dependent", 
    "design", "desire", "destruction", "detail", "development", "different", 
    "digestion", "direction", "dirty", "discovery", "discussion", "disease", 
    "disgust", "distance", "distribution", "division", "do", "dog", "door", "doubt", 
    "down", "drain", "drawer", "dress", "drink", "driving", "drop", "dry", "dust", 
    "ear", "early", "earth", "east", "edge", "education", "effect", "egg", "elastic", 
    "electric", "end", "engine", "enough", "equal", "error", "even", "event", "ever", 
    "every", "example", "exchange", "existence", "expansion", "experience", "expert", 
    "eye", "face", "fact", "fall", "false", "family", "far", "farm", "fat", "father", 
    "fear", "feather", "feeble", "feeling", "female", "fertile", "fiction", "field", 
    "fight", "finger", "fire", "first", "fish", "fixed", "flag", "flame", "flat", 
    "flight", "floor", "flower", "fly", "fold", "food", "foolish", "foot", "for", 
    "force", "fork", "form", "forward", "fowl", "frame", "free", "frequent", 
    "friend", "from", "front", "fruit", "full", "future", "garden", "general", 
    "get", "girl", "give", "glass", "glove", "go", "goat", "gold", "good", 
    "government", "grain", "grass", "great", "green", "grey", "grip", "group", 
    "growth", "guide", "gun", "hair", "hammer", "hand", "hanging", "happy", 
    "harbour", "hard", "harmony", "hat", "hate", "have", "he", "head", "healthy", 
    "hear", "hearing", "heart", "heat", "help", "high", "history", "hole", 
    "hollow", "hook", "hope", "horn", "horse", "hospital", "hour", "house", "how", 
    "humour", "I", "ice", "idea", "if", "ill", "important", "impulse", "in", 
    "increase", "industry", "ink", "insect", "instrument", "insurance", "interest", 
    "invention", "iron", "island", "jelly", "jewel", "join", "journey", "judge", 
    "jump", "keep", "kettle", "key", "kick", "kind", "kiss", "knee", "knife", 
    "knot", "knowledge", "land", "language", "last", "late", "laugh", "law", 
    "lead", "leaf", "learning", "leather", "left", "leg", "let", "letter", "level", 
    "library", "lift", "light", "like", "limit", "line", "linen", "lip", "liquid", 
    "list", "little", "living", "lock", "long", "look", "loose", "loss", "loud", 
    "love", "low", "machine", "make", "male", "man", "manager", "map", "mark", 
    "market", "married", "mass", "match", "material", "may", "meal", "measure", 
    "meat", "medical", "meeting", "memory", "metal", "middle", "military", "milk", 
    "mind", "mine", "minute", "mist", "mixed", "money", "monkey", "month", "moon", 
    "morning", "mother", "motion", "mountain", "mouth", "move", "much", "muscle", 
    "music", "nail", "name", "narrow", "nation", "natural", "near", "necessary", 
    "neck", "need", "needle", "nerve", "net", "new", "news", "night", "no", 
    "noise", "normal", "north", "nose", "not", "note", "now", "number", "nut", 
    "observation", "of", "off", "offer", "office", "oil", "old", "on", "only", 
    "open", "operation", "opinion", "opposite", "or", "orange", "order", 
    "organization", "ornament", "other", "out", "oven", "over", "owner", "page", 
    "pain", "paint", "paper", "parallel", "parcel", "part", "past", "paste", 
    "payment", "peace", "pen", "pencil", "person", "physical", "picture", "pig", 
    "pin", "pipe", "place", "plane", "plant", "plate", "play", "please", 
    "pleasure", "plough", "pocket", "point", "poison", "polish", "political", 
    "poor", "porter", "position", "possible", "pot", "potato", "powder", "power", 
    "present", "price", "print", "prison", "private", "probable", "process", 
    "produce", "profit", "property", "prose", "protest", "public", "pull", 
    "pump", "punishment", "purpose", "push", "put", "quality", "question", 
    "quick", "quiet", "quite", "rail", "rain", "range", "rat", "rate", "ray", 
    "reaction", "reading", "ready", "reason", "receipt", "record", "red", 
    "regret", "regular", "relation", "religion", "representative", "request", 
    "respect", "responsible", "rest", "reward", "rhythm", "rice", "right", 
    "ring", "river", "road", "rod", "roll", "roof", "room", "root", "rough", 
    "round", "rub", "rule", "run", "sad", "safe", "sail", "salt", "same", 
    "sand", "say", "scale", "school", "science", "scissors", "screw", "sea", 
    "seat", "second", "secret", "secretary", "see", "seed", "seem", "selection", 
    "self", "send", "sense", "separate", "serious", "servant", "sex", "shade", 
    "shake", "shame", "sharp", "sheep", "shelf", "ship", "shirt", "shock", 
    "shoe", "short", "shut", "side", "sign", "silk", "silver", "simple", "sister", 
    "size", "skin", "skirt", "sky", "sleep", "slip", "slope", "slow", "small", 
    "smash", "smell", "smile", "smoke", "smooth", "snake", "sneeze", "snow", 
    "so", "soap", "society", "sock", "soft", "solid", "some", "son", "song", 
    "sort", "sound", "soup", "south", "space", "spade", "special", "sponge", 
    "spoon", "spring", "square", "stage", "stamp", "star", "start", "statement", 
    "station", "steam", "steel", "stem", "step", "stick", "sticky", "stiff", 
    "still", "stitch", "stocking", "stomach", "stone", "stop", "store", "story", 
    "straight", "strange", "street", "stretch", "strong", "structure", "substance", 
    "such", "sudden", "sugar", "suggestion", "summer", "sun", "support", 
    "surprise", "sweet", "swim", "system", "table", "tail", "take", "talk", 
    "tall", "taste", "tax", "teaching", "tendency", "test", "than", "that", 
    "the", "then", "theory", "there", "thick", "thin", "thing", "this", 
    "thought", "thread", "throat", "through", "thumb", "thunder", "ticket", 
    "tight", "till", "time", "tin", "tired", "to", "toe", "together", "tomorrow", 
    "tongue", "tooth", "top", "touch", "town", "trade", "train", "transport", 
    "tray", "tree", "trick", "trouble", "trousers", "true", "turn", "twist", 
    "umbrella", "under", "unit", "up", "use", "value", "verse", "very", "vessel", 
    "view", "violent", "voice", "waiting", "walk", "wall", "war", "warm", "wash", 
    "waste", "watch", "water", "wave", "wax", "way", "weather", "week", "weight", 
    "well", "west", "wet", "wheel", "when", "where", "while", "whip", "whistle", 
    "white", "who", "why", "wide", "will", "wind", "window", "wine", "wing", 
    "winter", "wire", "wise", "with", "woman", "wood", "wool", "word", "work", 
    "worm", "wound", "writing", "wrong", "year", "yellow", "yes", "yesterday", 
    "you", "young", "bernhard", "breytenbach", "android"
]

print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
""")

stages = [
    """
       --------
       |      |
       |      O
       |     /|\\
       |      |
       |     / \\
       -
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      |
       |     / 
       -
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      |
       |      
       -
    """,
    """
       --------
       |      |
       |      O
       |     /|
       |      |
       |      
       -
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |      
       -
    """,
    """
       --------
       |      |
       |      O
       |    
       |      
       |      
       -
    """,
    """
       --------
       |      |
       |      
       |    
       |      
       |      
       -
    """
]

length = len(words_list) # Calculate the length of the list once and store it in a variable

def get_random_word():   # Define a function to get a random word from the list
    return words_list[random.randint(0, length - 1)]

x=0
y=get_random_word() # Get a random word and store it in a variable
#print(y) Print the random word (for testing purposes)

placeholder = "" # Initialize an empty string to store the correctly guessed letters

for position in range(len(y)): # Loop through each position in the random word
    placeholder += "_" # Add an underscore to the placeholder string for each letter
print(placeholder) # Print the initial placeholder string with underscores

correct_letters = [] # Initialize an empty list to store the correctly guessed letters
guessed_letters = [] # Initialize an empty list to store all guessed letters (both correct and incorrect)
lives=0

while True:
    z=input("Guess a letter(write exit to quit): ").lower() # Prompt the user to guess a letter

    if z in correct_letters: # Check if the guessed letter has already been guessed correctly
        print("You already guessed that letter correctly!") # If the letter has already been guessed, print a message
    elif z in guessed_letters: # Check if the guessed letter has already been guessed (regardless of correctness)
        print("You already guessed that letter!") # If the letter has already been guessed, print a message
        continue # Skip the rest of the loop and prompt for another guess

    guessed_letters.append(z) # Add the guessed letter to the list of all guessed letters
    display="" # Initialize an empty string to store the display of guessed letters and underscores

    if z == "exit": # If the user types "exit", break the loop and end the game
        print("Exiting the game. The word was:", y) # Print a message indicating the game is exiting and reveal the random word
        break

    if z in y: # If the guessed letter is in the random word, check each letter in the word
        for i in y:
            if z==i:
                display += z # If the guessed letter matches the current letter, add it to the display string
                correct_letters.append(z) # Add the correctly guessed letter to the list of correct letters
            elif i in correct_letters:
                display += i # If the current letter is in the list of correct letters, add it to the display string
            else:
                display += "_" # If the guessed letter does not match the current letter, add an underscore to the display string
        print() # Print a newline after checking all letters
    else:
        print("Letter not in word") # If the guessed letter is not in the random word, print a message
        lives += 1 # Increment the number of lives lost
        print(f"You have {lives}/6 lives lost") # Print the number of lives lost
    print(stages[6-lives]) # Print the current hangman stage

    if lives == 6: # If the user has lost 6 lives, they have lost the game
        print("You lost! The word was:", y) # Print a message indicating the user has lost and reveal the random word
        break # Break the loop and end the game
    print(display) # Print the current display string with guessed letters and underscores

    if display == y: # If the display string matches the random word, the user has guessed the word correctly
        print("Congratulations! You guessed the word!") # Print a congratulatory message
        break # Break the loop and end the game
