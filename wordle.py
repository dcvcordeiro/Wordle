from enum import Enum

class LETTER(Enum):
    WRONG = '#D3D3D3'     # Letter does not exist in the answer (Light Gray)
    PARTIAL = '#FFFF33'   # Letter exists in the answer, but wrong place (Yellow)
    CORRECT = '#00FF00'   # Letter exists and it is right place (Green)


def launch_game():
    """
    Main controller for the game flow
    """
    user_guesses = []
    solution = get_solution()

    for _ in range(0,6):
        user_guess = ask_user_guess()
        user_guesses.append(user_guess)
        if check_word(user_guess, solution):
            print("Correct Solution")
            return


def get_solution() -> str:
    """Generate a pseudo-random solution for the game"""
    return "tests"


def ask_user_guess() -> str:
    user_guess = ""
    while not check_guess_validity(user_guess):
        user_guess = input("Enter guess: ")
        user_guess = user_guess.lower()
    return user_guess


def check_guess_validity(user_guess:str) -> bool:
    if user_guess == "":
        return False

    if len(user_guess) != 5 or not user_guess.isalpha():
        print("The guess must have 5 letters")
        return False
    
    return True
    
    # hook to check if it is a valid word

def check_word(guess:str, answer:str) -> bool:
    """Checks if the user guess is the correct answer"""
    return guess == answer


def check_attempt(guess:str, answer:str) -> list(LETTER):
    """
        Compare user guess with solution and return a color coded mapping
    """
    validation = []
    for i, j in zip(guess, answer):
        if i == j:
            validation.append(LETTER.CORRECT)
        elif i in answer:
            validation.append(LETTER.PARTIAL)
        else:
            validation.append(LETTER.WRONG)
    return validation


if __name__ == "__main__":
    launch_game()
