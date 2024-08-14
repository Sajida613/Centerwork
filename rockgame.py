# Best Gaming Program

import random

# Function to play Rock, Paper, Scissors
def play_rps():
  choices = ["rock", "paper", "scissors"]
  computer = random.choice(choices)
  user = input("Enter your choice (rock/paper/scissors): ").lower()
  if user == computer:
    print("Tie!")
  elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
    print("You win!")
  else:
    print("Computer wins!")

# Function to play Hangman
def play_hangman():
  word = random.choice(["apple", "banana", "cherry"])
  guesses = 6
  while guesses > 0:
    print("Guess the word: ", end="")
    for char in word:
      if char in guesses:
        print(char, end="")
      else:
        print("_", end="")
    print()
    guess = input("Enter your guess: ").lower()
    if guess in word:
      guesses -= 1
    else:
      print("Incorrect guess!")
  print("Word was:", word)

# Main program
while True:
  print("1. Play Rock, Paper, Scissors")
  print("2. Play Hangman")
  print("3. Exit")
  choice = input("Enter your choice: ")
  if choice == "1":
    play_rps()
  elif choice == "2":
    play_hangman()
  elif choice == "3":
    break
  else:
    print("Invalid choice. Please try again.")


