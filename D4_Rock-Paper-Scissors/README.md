# D3 — Rock–Paper–Scissors (CLI Game)

A simple command-line implementation of the classic **Rock–Paper–Scissors** game in Python.  
The player chooses Rock, Paper, or Scissors, the computer makes a random choice, and the program determines whether the player **wins, loses, or draws**.

This project focuses on **conditionals, randomization, input validation, and basic function design**.

---

## ✨ Features

- Command-line game with clear text instructions  
- ASCII art for Rock, Paper, and Scissors to make the game more visual  
- Player chooses between:
  - `0` → Rock  
  - `1` → Paper  
  - `2` → Scissors  
- Computer randomly chooses its move using Python’s `random` module  
- Game result is determined based on Rock–Paper–Scissors rules:
  - Rock beats Scissors  
  - Paper beats Rock  
  - Scissors beats Paper  
  - Same choice → Draw  
- Basic input validation:
  - Ensures the player chooses only 0, 1, or 2  
  - Handles non-numeric input with a friendly error message  

---

## 🧠 What I Practiced

- Working with `input()` and converting string input to integers (`int()`)  
- Using the `random` module (`random.randint`) to simulate computer choices  
- Implementing conditional logic with `if / elif / else`  
- Designing a small function (`decide_choice`) to separate game logic from input/output  
- Applying basic type hints in Python (`player_choice: int`, `-> str`)  
- Looping with `while True` for input validation  

---

## 🗂 Project Structure

```text
D3_RockPaperScissors/
├── main.py      # Game implementation
└── README.md    # Project description
