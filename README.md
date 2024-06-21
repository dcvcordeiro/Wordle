# Wordle Clone in Python

Welcome to the Wordle Clone! This project is a command-line implementation of the popular word puzzle game, Wordle, where the player has to guess a 5-letter word within six attempts.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Gameplay](#gameplay)
- [Acknowledgments](#acknowledgments)

## Features

- Command-line interface for easy interaction
- Random word selection from a predefined list
- Input validation to ensure proper guesses
- Feedback on each guess with color-coded results
  - 🟩 Green: Correct letter in the correct position
  - 🟨 Yellow: Correct letter in the wrong position
  - ⬜ Gray: Incorrect letter

## Installation

To get started with the Wordle Clone, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/dcvcordeiro/Wordle.git
    cd Wordle
    ```

2. **Create a virtual environment (optional but recommended):**

    ```sh
    conda env create -f environment.yml
    conda activate wordle_env
    ```


## Usage

To start the game, simply run the `wordle.py` script:

```sh
python wordle.py
```

## Gameplay
1. You will be prompted to enter a 5-letter word.
2. After each guess, you will receive feedback:
    - 🟩 Green means the letter is correct and in the correct position.
    - 🟨 Yellow means the letter is correct but in the wrong position.
    - ⬜ Gray means the letter is not in the word.
3. You have 6 attempts to guess the correct word.

### Example Gameplay
<img title="GUESS" alt="GUESS" src="/images/Guess.PNG">
<img title="GAME OVER" alt="GAME OVER" src="/images/Answer.PNG">


## Acknowledgments
Inspired by the original Wordle game by Josh Wardle.

---
Happy Wordling!