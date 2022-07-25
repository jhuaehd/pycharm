import random

RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')


# Pass in the deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop()  # pop one off the top of the deck and return
    return thisCard


# Pass in the deck and this function returns a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  # make a copy of starting deck
    random.shuffle(deckListOut)
    return deckListOut


startingDeckList = []

for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)

        print(cardDict)

