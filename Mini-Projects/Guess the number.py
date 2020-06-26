from random import randint

def game():
    n = randint(0, 50)

    number_of_guesses = 1
    
    print("Number of guesses is limited to only 9 times: ")
    
    while (number_of_guesses <= 9):
        
        guess_number = int(input("\nGuess the number :\n"))
        
        while guess_number not in range (0, 50):
            guess_number = int(input("\nInvalid Input. Please select number between 0-50: "))

        if guess_number < n:
            print("You enter less number please input greater number.\n")

        elif guess_number > n:
            print("You enter greater number please input smaller number.\n ")

        else:
            print("You won\n")
            print(number_of_guesses, "No.of guesses player took to finish.")
            break

        print(9 - number_of_guesses, "No. of guesses left")
        number_of_guesses = number_of_guesses + 1

    if(number_of_guesses > 9):
        print("GAME OVER!")
        
    again()
        
def again():
    var = input("""
        Do you want to continue
        Press 'y' for Yes or 'n' for No
        """)
    if var == 'y':
        game()
    elif var == 'n':
        print("\nThank You for Playing" + "\nSee you later")
    else:
        again()

game()    
