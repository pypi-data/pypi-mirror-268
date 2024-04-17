import random
suits = ["♥", "♦", "♣", "♠"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# Assign card values
values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

def create_deck(int=1):
    """Create 1 deck of 52*int cards"""
    decks = []
    for suit in suits:
        for rank in ranks:
            card = {"Suit": suit, "Rank": rank, "Value": values[rank]}
            decks.append(card)
    decks *= int
    random.shuffle(decks)
    return decks

def show_card(card):
    """Return the ascii art for a given card"""
    rank = card["Rank"]
    suit = card["Suit"]
    card_value = f"{rank}{suit}"
    ascii_card = f"""
┌─────────┐
│         │
│    {card_value:<2}   │
│         │
│    {suit}    │
│         │
│    {card_value:>2}   │
│         │
└─────────┘
"""
    if len(card_value) > 2:
        ascii_card = f"""
┌─────────┐
│         │
│    {card_value:<2}  │
│         │
│    {suit}    │
│         │
│    {card_value:>2}  │
│         │
└─────────┘
"""
    return ascii_card

def show_hand(hand):
    """Return the ascii art for a given hand with cards displayed horizontally"""
    hand_lines = [""] * 10  # Number of lines in each card representation
    for card in hand:
        card_lines = show_card(card).split('\n')
        for i in range(len(hand_lines)):
            hand_lines[i] += card_lines[i] + "  "  # Add spacing between cards
    return '\n'.join(hand_lines)

