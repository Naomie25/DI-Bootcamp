# Exercise 1: Quizz

# What is a class?
# A class is a blueprint for creating objects,
# and defines what an object is and what it can do

# What is an instance?
# An instance is a specific object created from a class.

# What is encapsulation?
# Keeping data safe and private inside a class, 
# and only letting it be accessed or changed in controlled ways.

# What is abstraction?
# Showing only what’s necessary and hiding the complexity behind the scenes.


# What is inheritance?
# A way for a new class to reuse code from an existing class.

# What is multiple inheritance?
# A class that inherits attributes and methods from multiple classes at the same time.

# What is polymorphism?
# Different objects can use the same action but do it in their own way

# What is method resolution order or MRO?
# MRO is the rule Python uses to decide where to find a method 
# or attribute when you call it on an object. 
# It checks the class itself first, then its parents, in a specific order, 
# to know which one to use. 
# This is important when a class has multiple parents.


#Exercise 2: Create a deck of cards class
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit    # Hearts, Diamonds, Clubs, Spades
        self.value = value  # A,2,3,...,10,J,Q,K

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []  # Will hold Card objects
        self._build_deck()

    def _build_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        # Ensure all 52 cards are present
        if len(self.cards) != 52:
            self._build_deck()
        random.shuffle(self.cards)

    def deal(self):
        if self.cards:
            return self.cards.pop()  # Remove and return the last card
        else:
            return None  # No cards left to deal

# Example usage
deck = Deck()
deck.shuffle()

card = deck.deal()
if card:
    print("Dealt card:", card)
else:
    print("No cards left to deal.")
