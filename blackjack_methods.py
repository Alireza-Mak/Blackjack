import random, os, platform
from blackjack_arts import creator, logo, goodbye

def clear():
  '''Clear IDE based on OS system'''
  return os.system("clear") if platform.system() == "Linux" else os.system("cls") 

def correct_input_value(message, lunch_choice1, lunch_choice2):
  '''Take the message and choices and compare if the input was 
     not equal to the choices ask to enter the correct input'''
  user_input =input(message).lower()
  while user_input not in (lunch_choice1, lunch_choice2):
    user_input =input(f"Wrong input. {message}").lower()
  return user_input
      
  
def calculate_score(cards):
  '''Take a list of cards and return the score calculated from the cards'''
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def deal_cards(cards):
  '''Returns a random card by getting list of cards as a parameter from the deck'''
  card = random.choice(cards)
  return card

def compare(user_score, computer_score):
  '''Take user score and computer score and compare and return result'''
  if user_score == computer_score:
    return "Draw 😊"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0 or user_score == 21:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over, You lose 😭"
  elif computer_score > 21:
    return "Opponent over, You win 😁"
  elif user_score > computer_score:
    return "You win 😀"
  else:
    return "You lose 😤"

def play_blackjack(cards):
  '''Run Blackjack Game'''
  is_game_finish = False
  while not is_game_finish:
    clear()
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over =False
  
    for _ in range(2):
      user_cards.append(deal_cards(cards))
      computer_cards.append(deal_cards(cards))

    computer_score = 0
    user_score = 0
    is_game_over = False
    while not is_game_over:
      user_score = calculate_score(user_cards)
      computer_score = calculate_score(computer_cards)
      print(f"Your cards: {user_cards}, current score: {21 if user_score == 0  else user_score}")
      print(f"Computer's first card: {computer_cards[0]}")
  
      if user_score == 0 or user_score == 21 or user_score > 21:
        is_game_over = True
      else:
        user_should_deal = correct_input_value("Type 'y' to get another card, type 'n' to pass ", "y", "n")
        clear()
        print(logo)
        if user_should_deal == "y":
          user_cards.append(deal_cards(cards))
        else:
          is_game_over = True
  
    while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_cards(cards))
      computer_score = calculate_score(computer_cards)
  
    clear()
    print(logo)
    print(f"Your final hand : {user_cards}, final score: {21 if user_score == 0  else user_score}")
  
    print(f"Computer's final hand : {computer_cards}, final score: {computer_score}")
  
    print(compare(user_score, computer_score))
    reply = correct_input_value("Do you want to continue the game? Type 'y' or 'n' ", "y", "n")
    if reply == 'n':
      is_game_finish = True
      clear()
      print(logo + creator + goodbye)
  
  
  
  