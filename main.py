from blackjack_methods import play_blackjack, correct_input_value, clear
from blackjack_arts import goodbye, logo, creator, cards

clear()
print(logo + creator)
start_game = correct_input_value("Do you want to play a game of a Blackjack? Type 'y' or 'n' ", "y", "n")

play_blackjack(cards) if start_game =='y' else print(goodbye)