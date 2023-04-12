#!/usr/bin/env python
"""
Play the rock paper scissors game
"""
import sys
import random

def play():
    # Take user input: 's', 'p', or 'r'
    player_choice = input("Enter 'r' for rock, 'p' for paper, or 's' for scissors: ")
    # Set computer choice
    computer_choice = random.choice(['r', 'p', 's'])
    print(f"Computer choice: {computer_choice}")
    # Check logic: Tie, Win, or lost
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'r' and computer_choice == 's') or \
         (player_choice == 'p' and computer_choice == 'r') or \
         (player_choice == 's' and computer_choice == 'p'):
        print("You win!")
    else:
        print("Computer wins!")

def check_win(player, opponent):
    """Returns True if player wins

    Args:
        player (string): player hand
        opponent (string): opponent hand

    Returns:
        True: If player wins
    """
    if (player == 'r' and opponent == 's') or \
       (player == 'p' and opponent == 'r') or \
       (player == 's' and opponent == 'p'):
        return True
    else:
        return False

# Call the play() function to start the game
play()