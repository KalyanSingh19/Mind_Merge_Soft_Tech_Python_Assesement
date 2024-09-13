import random

def roll_dice():
  return random.randint(1, 6)

def play_dice_game():

  player1_roll = roll_dice()
  player2_roll = roll_dice()

  print("Player 1 rolled:", player1_roll)
  print("Player 2 rolled:", player2_roll)

  if player1_roll > player2_roll:
    print("Player 1 wins!")
  elif player1_roll < player2_roll:
    print("Player 2 wins!")
  else:
    print("It's a tie!")

# Play the game
play_dice_game()