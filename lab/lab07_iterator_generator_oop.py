def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1."""
    i = 1
    while True:
        yield i
        i += 1

def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier."""

    ###############
    # My Solution #
    ###############

    for x in it:
        yield x * multiplier

def hailstone(n):

    ###############
    # My Solution #
    ###############

    yield n
    if n != 1:
        if n % 2 == 0:
            yield from hailstone(n//2)
        else:
            yield from hailstone(n * 3 + 1)+


# Magic the Lambda-ing!


import random

class Card:
    cardtype = 'Staff'

    def __init__(self, name, attack, defense):
        """
        Create a Card object with a name, attack,
        and defense.
        """

        ###############
        # My Solution #
        ###############

        self.name = name
        self.attack = attack
        self.defense = defense

    def power(self, other_card):
        """
        Calculate power as:
        (player card's attack) - (opponent card's defense)/2
        where other_card is the opponent's card.
        """

        ###############
        # My Solution #
        ###############

        return self.attack - (other_card.defense/2)


    def effect(self, other_card, player, opponent):
        """
        Cards have no default effect.
        """
        return

    def __repr__(self):
        """
        Returns a string which is a readable version of
        a card, in the form:
        <cardname>: <cardtype>, [<attack>, <defense>]
        """
        return '{}: {}, [{}, {}]'.format(self.name, self.cardtype, self.attack, self.defense)

    def copy(self):
        """
        Returns a copy of this card.
        """
        return Card(self.name, self.attack, self.defense)

class Player:
    def __init__(self, deck, name):
        """Initialize a Player object.
        A Player starts the game by drawing 5 cards from their deck. Each turn,
        a Player draws another card from the deck and chooses one to play.
        """

        ###############
        # My Solution #
        ###############

        self.deck = deck
        self.name = str(name)
        self.hand = []
        for _ in range(5):
            self.draw()
        

    def draw(self):
        """Draw a card from the player's deck and add it to their hand."""

        ###############
        # My Solution #
        ###############    

        assert not self.deck.is_empty(), 'Deck is empty!'

        self.hand.append(self.deck.cards[0])
        self.deck.cards.pop(0)


    def play(self, card_index):
        """Remove and return a card from the player's hand at the given index."""


        ###############
        # My Solution #
        ###############

        return self.hand.pop(card_index)

    def display_hand(self):
        """
        Display the player's current hand to the user.
        """
        print('Your hand:')
        for card_index, displayed_card in zip(range(len(self.hand)),[str(card) for card in self.hand]):
            indent = ' '*(5 - len(str(card_index)))
            print(card_index, indent + displayed_card)

    def play_random(self):
        """
        Play a random card from hand.
        """
        return self.play(random.randrange(len(self.hand)))

######################
# Optional Questions #
######################

class TutorCard(Card):
    cardtype = 'Tutor'

    def effect(self, other_card, player, opponent):
        """
        Discard the first 3 cards in the opponent's hand and have
        them draw the same number of cards from their deck.
        """

        ###############
        # My Solution #
        ###############

        for _ in range(3):
            opponent.hand.pop(0)

        for _ in range(3):
            opponent.draw()

        print('{} discarded and re-drew 3 cards!'.format(opponent.name))

    def copy(self):
        """
        Create a copy of this card.
        """
        return TutorCard(self.name, self.attack, self.defense)

class TACard(Card):
    cardtype = 'TA'

    def effect(self, other_card, player, opponent):
        """
        Swap the attack and defense of an opponent's card.
        """

        ###############
        # My Solution #
        ###############

        other_card.attack, other_card.defense = other_card.defense, other_card.attack

    def copy(self):
        """
        Create a copy of this card.
        """
        return TACard(self.name, self.attack, self.defense)

class ProfessorCard(Card):
    cardtype = 'Professor'

    def effect(self, other_card, player, opponent):
        """
        Adds the attack and defense of the opponent's card to
        all cards in the player's deck, then removes all cards
        in the opponent's deck that share an attack or defense
        stat with the opponent's card.
        """

        ###############
        # My Solution #
        ###############
       
        for card in player.deck.cards:
            card.attack+= other_card.attack
            card.defense+= other_card.defense
        
        opponent.deck.cards = [card for card in opponent.deck.cards if card.attack != other_card.attack or card.defense != other_card.defense]

        orig_opponent_deck_length = len(opponent.deck.cards)
        discarded = orig_opponent_deck_length - len(opponent.deck.cards)
        if discarded:
            print('{} cards were discarded from {}\'s deck!'.format(discarded, opponent.name))
            return

    def copy(self):
        return ProfessorCard(self.name, self.attack, self.defense)