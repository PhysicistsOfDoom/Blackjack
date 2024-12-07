from cards import cards_to_paths
from logic import Deck

deck = Deck()

# Example card tuple
card = deck.original_deck[0]  # Ace of Diamonds

# Get the file path
file_path = cards_to_paths[card]
print(file_path)  # Output: /media/fronts/diamonds_ace.png
