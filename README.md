# Hangman-Game
# Python Hangman Game

A classic command-line implementation of the Hangman game built using Python. This interactive game selects a random word from a vast built-in dictionary, features progressive ASCII art gallows, and tracks your remaining lives as you guess letters.

---

## 🚀 Features

* **Extensive Word Bank:** Features an embedded library of over 800 diverse words, including specialized terms like `"android"`, `"bernhard"`, and `"breytenbach"`.
* **Dynamic ASCII Art:** Displays a progressive hangman visual that updates stage-by-stage every time an incorrect guess is made.
* **Smart Input Validation:**
    * Automatically handles uppercase and lowercase inconsistencies.
    * Alerts you if you try to guess a letter you have already selected.
* **Graceful Exit:** Allows players to cleanly quit mid-game by typing `exit`.

---

## 🛠️ Requirements & Installation

No external libraries or dependencies are required! The game runs entirely on vanilla Python using the built-in `random` module.

1. Ensure you have **Python 3.x** installed on your system.
2. Save the game script to a file named `hangman.py`.

---

## 🎮 How to Play

1. Run the script from your terminal:
   ```bash
   python hangman.py
   ```
2. The game will display an ASCII banner and a hidden word represented by underscores (`_ _ _ _`).
3. Enter a single letter at the prompt to guess.
4. **Winning:** Successfully fill in all the blanks before running out of lives.
5. **Losing:** If you guess incorrectly 6 times, the full hangman is drawn and the game is over.
6. **Quitting:** Type `exit` at any time to reveal the word and close the game.

---

## 🧠 Game Logic Breakdown

* **`lives` Tracking:** The game starts with `lives = 0` (representing lives lost). Each mistake increments this value up to a maximum of `6`.
* **Visual Indexing:** The script renders the gallows state using `stages[6 - lives]`, ensuring the structure matches your current safety margin.
* **Guess Cache:** Two list states (`correct_letters` and `guessed_letters`) work concurrently to block repetitive inputs and preserve game flow.
