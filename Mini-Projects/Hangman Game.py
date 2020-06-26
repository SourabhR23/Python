import random

def hangman():
    word = random.choice(["superman", "tiger", "ironman", "pikachu", "avengers", "earth", "porsche"])
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''
    
    while len(word) > 0 :
        main = ''
        missed = 0
        
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " " # to create '_' as per length of word randomly selected

        # Winning Code
        if main == word:
            print(main)
            print("\nYou win!")
            break
        
        # Guessing Code
        print("\nGuess the word: ", main)
        guess = input()
        
        if guess in valid_letters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()
        
        # Drawing Hangman Code
        if guess not in word:
            turns = turns - 1
            
            if turns == 9:
                print("9 turns left")
                print(" ---------- ")
            if turns == 8:
                print("8 turns left")
                print(" ---------- ")
                print("     0      ")
            if turns == 7:
                print("7 turns left")
                print(" ---------- ")
                print("     0      ")            
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print(" ---------- ")
                print("     0      ")            
                print("     |      ")
                print("    /       ")    
            if turns == 5:
                print("5 turns left")
                print(" ---------- ")
                print("     0      ")            
                print("     |      ")
                print("    / \      ")  
            if turns == 4:
                print("4 turns left")
                print(" ---------- ")
                print("   \ 0      ")            
                print("     |      ")
                print("    / \      ") 
            if turns == 3:
                print("3 turns left")
                print(" ---------- ")
                print("   \ 0 /     ")            
                print("     |      ")
                print("    / \      ") 
            if turns == 2:
                print("2 turns left")
                print(" ---------- ")
                print("   \ 0 /|     ")            
                print("     |      ")
                print("    / \      ") 
            if turns == 1:
                print("1 turn left")
                print("Lasr breaths counting\n")
                print(" ---------- ")
                print("   \ 0_ /|     ")            
                print("     |      ")
                print("    / \      ")
            if turns == 0:
                print("You lost")
                print("You let kind man die")
                print(" ---------- ")
                print("     0_|     ")            
                print("    /|\      ")
                print("    / \      ")
                
    
player_name = input("Enter your name: ")
print("----------------")
print("Welcome " + player_name)
print("Try to guess the word in less than 10 try")

hangman()