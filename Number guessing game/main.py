import random
import sys
import time



def generate_num():
    """Generates a random number between start and end"""
    try:
        lower_bound = int(input("Enter the lower bound of the range: "))
        upper_bound = int(input("Enter the upper bound of the range: "))
        if upper_bound < 0 or lower_bound < 0:
            print("The bounds must be positive")
            return generate_num()
        if lower_bound > upper_bound:
            print("The lower bound is greater than the upper bound")
            return generate_num()

    except ValueError:
        print("Please enter valid integers (numbers)")
        return generate_num()
    random_num = random.randint(lower_bound, upper_bound)
    return {"upper_bound": upper_bound, "lower_bound": lower_bound, "random_num": str(random_num)}

def game_flow():
    """Restart the game, if user wants to"""
    game_status = input("Do you want to continue playing? Y/N: ")
    if game_status == "Y" or game_status == "y":
        main()
    if game_status == "N" or game_status == "n":
        print("Thank you for playing!")
        time.sleep(3)
        sys.exit()
    else:
        print("Please enter Y or N")
        return game_flow()

def main():

    print("Welcome to the Number Guessing Game!")
    random_num_info = generate_num()
    attempts = 0
    while True:
        try:
            attempts += 1
            print(f"Attempt #{attempts}")

            user_guess = input(f"Guess a random number between "
                           f"{random_num_info["lower_bound"]} "
                           f"and {random_num_info["upper_bound"]}: ")

            if user_guess == random_num_info["random_num"]:
                print("Congratulations, you guessed it!")
                print("Attempts used: ", attempts)
                game_flow()
            else:
                if int(user_guess) < int(random_num_info["random_num"]):
                    print("Too low")
                else:
                    print("Too high")
        except ValueError:
            print("Please enter valid integers (numbers)")
            time.sleep(1)
            attempts -= 1
            continue



main()

