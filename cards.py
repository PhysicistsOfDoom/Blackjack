#Mapping of suits to their symbols
suits = {
    '♣': 'clubs',
    '♦': 'diamonds',
    '♥': 'hearts',
    '♠': 'spades'
}

#Mapping of ranks
ranks = {
    'A': 'ace',
    'K': 'king',
    'Q': 'queen',
    'J': 'jack',
    10: '10',
    9: '9',
    8: '8',
    7: '7',
    6: '6',
    5: '5',
    4: '4',
    3: '3',
    2: '2',
}

#Build a dictionary to map tuples to file paths
cards_to_paths = {
    (rank, suit): f"media/fronts/{suits[suit]}_{ranks[rank]}.png"
    for suit in suits
    for rank in ranks
}
