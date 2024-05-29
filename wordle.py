from enum import Enum

class LETTER(Enum):
    WRONG = '#D3D3D3'     # Letter does not exist in the answer (Light Gray)
    PARTIAL = '#FFFF33'   # Letter exists in the answer, but wrong place (Yellow)
    CORRECT = '#00FF00'   # Letter exists and it is right place (Green)


def launch_game():
    """
    Main controller for the game flow
    """
    print("Hello World!")


def check_word(guess:str, answer:str) -> bool:
    """Checks if the user guess is the correct answer"""
    return guess == answer


def check_attempt(guess:str, answer:str) -> list(LETTER):
    """
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
    validation = check_attempt("test","part")
    print(validation)