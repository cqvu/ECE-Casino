import random

def shuffle_deck():
    deck = []
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']
    suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']

    for suit in suits:
        for value in values:
            deck.append(value + ' of ' + suit)

    random.shuffle(deck)
    print("A new deck of cards has been shuffled")
    return deck

def get_value(card):
    if card == 'J':
        value = 11
    elif card == 'Q':
        value = 12
    elif card == 'K':
        value = 13
    elif card == 'A':
        value = 14
    else:
        value = int(card)
    return value

def war(deck):
    # each player gets half of the deck
    p1 = deck[0, len(deck)/2]
    p2 = deck[len(deck)/2, len(deck)]
    in_play = []
    turn = 1

    # play until either player has no cards left
    while len(p1) != 0 and len(p2) != 0:
        print("Turn: " + turn)

        # pop the first card from both decks
        p1_card = p1.pop(0)
        p2_card = p2.pop(0)
        in_play = [p1_card, p2_card]

        print(player_name + " played a " + p1_card)
        print("Bot played a " + p2_card)

        #if p1_card is greater, p1 takes both cards
        if get_value(p1_card) > get_value(p2_card):
            p1.extend(in_play)
            in_play.clear()

        #if p2_card is greater, p2 takes both cards
        elif get_value(p2_card) > get_value(p1_card):
            p2.extend(in_play)
            in_play.clear()

        #if tie, each player puts down 2 cards and compare the 2nd card
        #elif get_value(p1_card) == get_value(p2_card):
