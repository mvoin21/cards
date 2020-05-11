from random import shuffle
import collections

Card = collections.namedtuple('Card', ['ranks', 'suits'])


class _Cards:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'крести пики буби черви'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]


class DeckOfCards(_Cards):

    def __len__(self):
        print(len(self._cards))

    @property
    def get_top_card(self):
        print(self._cards[-1])
        del self._cards[-1]

    @property
    def shuffle_deck(self):
        shuffle(self._cards)
        print('Колода перетасована')


richard = DeckOfCards()

richard.get_top_card
richard.shuffle_deck
richard.get_top_card
richard.get_top_card
richard.__len__()