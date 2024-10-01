import random

def main():
    # Introduction message
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    
    # Initialize variables
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            # Prompt user for input
            user_input = input("Enter your guess: ")
            
            # Convert input to integer
            guess = int(user_input)
            
            # Increment the attempt count
            attempts += 1

            # Check the user's guess
            if guess < target_number:
                print("Too low!")
            elif guess > target_number:
                print("Too high!")
            else:
                guessed_correctly = True
                print(f"Congratulations! You have guessed the number in {attempts} attempts.")
                
        except ValueError:
            # Handle invalid input (non-numeric values)
            print("Invalid input. Please enter a number between 1 and 100.")
            
    # Ending message is handled within the loop when the user guesses correctly

if __name__ == "__main__":
    main()


