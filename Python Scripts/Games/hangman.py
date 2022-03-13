import random
# library that we use in order to choose
# on random words from a list of words

name = input("What is your name? ")
# Here the user is asked to enter the name first

print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks'
         'abruptly',
         'absurd',
         'abyss',
         'affix',
         'askew',
         'avenue',
         'awkward',
         'axiom',
         'azure',
         'bagpipes',
         'bandwagon',
         'banjo',
         'bayou',
         'beekeeper',
         'bikini',
         'blitz',
         'blizzard',
         'boggle',
         'bookworm',
         'boxcar',
         'boxful',
         'buckaroo',
         'buffalo',
         'buffoon',
         'buxom',
         'buzzard',
         'buzzing',
         'buzzwords',
         'caliph',
         'cobweb',
         'cockiness',
         'croquet',
         'crypt',
         'curacao',
         'cycle',
         'daiquiri',
         'dirndl',
         'disavow',
         'dizzying',
         'duplex',
         'dwarves',
         'embezzle',
         'equip',
         'espionage',
         'euouae',
         'exodus',
         'faking',
         'fishhook',
         'fixable',
         'fjord',
         'flapjack',
         'flopping',
         'fluffiness',
         'flyby',
         'foxglove',
         'frazzled',
         'frizzled',
         'fuchsia',
         'funny',
         'gabby',
         'galaxy',
         'galvanize',
         'gazebo',
         'giaour',
         'gizmo',
         'glowworm',
         'glyph',
         'gnarly',
         'gnostic',
         'gossip',
         'grogginess',
         'haiku',
         'haphazard',
         'hyphen',
         'iatrogenic',
         'icebox',
         'injury',
         'ivory',
         'ivy',
         'jackpot',
         'jaundice',
         'jawbreaker',
         'jaywalk',
         'jazziest',
         'jazzy',
         'jelly',
         'jigsaw',
         'jinx',
         'jiujitsu',
         'jockey',
         'jogging',
         'joking',
         'jovial',
         'joyful',
         'juicy',
         'jukebox',
         'jumbo',
         'kayak',
         'kazoo',
         'keyhole',
         'khaki',
         'kilobyte',
         'kiosk',
         'kitsch',
         'kiwifruit',
         'klutz',
         'knapsack',
         'larynx',
         'lengths',
         'lucky',
         'luxury',
         'lymph',
         'marquis',
         'matrix',
         'megahertz',
         'microwave',
         'mnemonic',
         'mystify',
         'naphtha',
         'nightclub',
         'nowadays',
         'numbskull',
         'nymph',
         'onyx',
         'ovary',
         'oxidize',
         'oxygen',
         'pajama',
         'peekaboo',
         'phlegm',
         'pixel',
         'pizazz',
         'pneumonia',
         'polka',
         'pshaw',
         'psyche',
         'puppy',
         'puzzling',
         'quartz',
         'queue',
         'quips',
         'quixotic',
         'quiz',
         'quizzes',
         'quorum',
         'razzmatazz',
         'rhubarb',
         'rhythm',
         'rickshaw',
         'schnapps',
         'scratch',
         'shiv',
         'snazzy',
         'sphinx',
         'spritz',
         'squawk',
         'staff',
         'strength',
         'strengths',
         'stretch',
         'stronghold',
         'stymied',
         'subway',
         'swivel',
         'syndrome',
         'thriftless',
         'thumbscrew',
         'topaz',
         'transcript',
         'transgress',
         'transplant',
         'triphthong',
         'twelfth',
         'twelfths',
         'unknown',
         'unworthy',
         'unzip',
         'uptown',
         'vaporize',
         'vixen',
         'vodka',
         'voodoo',
         'vortex',
         'voyeurism',
         'walkway',
         'waltz',
         'wave',
         'wavy',
         'waxy',
         'wellspring',
         'wheezy',
         'whiskey',
         'whizzing',
         'whomever',
         'wimpy',
         'witchcraft',
         'wizard',
         'woozy',
         'wristwatch',
         'wyvern',
         'xylophone',
         'yachtsman',
         'yippee',
         'yoked',
         'youthful',
         'yummy',
         'zephyr',
         'zigzag',
         'zigzagging',
         'zilch',
         'zipper',
         'zodiac',
         'zombie'
         ]

# Function will choose one random
# word from this list of words
word = random.choice(words)


print("Guess the characters")

guesses = ''

# any number of turns can be used here
turns = 12


while turns > 0:

    # counts the number of times a user fails
    failed = 0

    # all characters from the input
    # word taking one at a time.
    for char in word:

        # comparing that character with
        # the character in guesses
        if char in guesses:
            print(char)

        else:
            print("_")

            # for every failure 1 will be
            # incremented in failure
            failed += 1

    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("You Win")

        # this print the correct word
        print("The word is: ", word)
        break

    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    guess = input("guess a character:")

    # every input character will be stored in guesses
    guesses += guess

    # check input with the character in word
    if guess not in word:

        turns -= 1

        # if the character doesn’t match the word
        # then “Wrong” will be given as output
        print("Wrong")

        # this will print the number of
        # turns left for the user
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")
