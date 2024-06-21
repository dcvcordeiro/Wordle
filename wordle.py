from random import choice
from rich.console import Console
from rich.theme import Theme

from string import ascii_uppercase


NR_GUESSES = 6
NR_LETTERS = 5

console = Console(width=50, theme=Theme({"warning": "red on yellow"}))

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue] :jigsaw:  {headline} :jigsaw:[/]\n")

def launch_game():
    """
    Main controller for the game flow
    """
    user_guesses = ["_" * NR_LETTERS] * NR_GUESSES
    solution = get_solution()

    for i in range(NR_GUESSES):
        refresh_page(f"GUESS {i+1}")

        show_guesses(user_guesses, solution)
        user_guesses[i] = ask_user_guess(user_guesses)

        if user_guesses[i] == solution:
            break

    game_over(user_guesses, solution, user_guesses[i] == solution)

def game_over(user_guesses, solution, answered_correctly):
    refresh_page(f"GAME OVER")
    show_guesses(user_guesses, solution)

    if answered_correctly:
        console.print(f"\n[bold white on green]Correct, the word is {solution}[/]")
    else:
        console.print(f"\n[bold white on red]Sorry, the word was {solution}[/]")

def get_solution() -> str:
    """Generate a pseudo-random solution for the game"""
    with open("word_lists/wordle_answers.txt", "r") as fp:
        valid_answers = fp.read().split("\n")
    return choice(valid_answers).upper()


def ask_user_guess(previous_guesses) -> str:
    user_guess = ""
    while not check_guess_validity(user_guess) and user_guess not in previous_guesses:
        user_guess = console.input("Enter guess: ")
        user_guess = user_guess.upper()
        if user_guess in previous_guesses:
            console.print(f"You have already guessed: {user_guess}")
    return user_guess


def check_guess_validity(user_guess:str) -> bool:
    if user_guess == "":
        return False

    if len(user_guess) != 5 or not user_guess.isalpha():
        console.print("The guess must have 5 letters", style="warning")
        return False
    
    with open("word_lists/valid_wordle_words.txt", "r") as fp:
        valid_guesses = fp.read().split("\n")
    
    if user_guess.lower() not in valid_guesses:
        console.print("Guess is not a valid word", style="warning")
        return False
    
    return True

def show_guesses(user_guesses, solution):
    letter_status = {letter: letter for letter in ascii_uppercase}

    for guess in user_guesses:
        styled_guess = []
        for guess_letter, correct_letter in zip(guess, solution):
            if guess_letter == correct_letter:
                style = "bold white on green"
            elif guess_letter in solution:
                style = "bold white on yellow"
            elif guess_letter != "_":
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{guess_letter}[/]")

            if guess_letter != "_":
                letter_status[guess_letter] = f"[{style}]{guess_letter}[/]"

        console.print("".join(styled_guess), justify="center")
    console.print("\n" + "".join(letter_status.values()), justify="center")
if __name__ == "__main__":
    launch_game()
