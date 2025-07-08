# Class Activities + Review (Classes)


'''
1.  Create a class called Card. The card should have two instance attributes:
        - value: (2-10, Ace, Jack, King, Queen)
        - suit: (hearts, spades, diamonds, clubs)
    Make sure you write an __init__ method to be sure to assign value and suit
    to your card object.

    Then write three instance methods:
        - getSuit() which returns the suit of the card.
        - getValue() which returns the value of the card (in terms of blackjack).
          numbered cards (2-10) are worth their respective points. Face cards (Jack, 
          King, Queen) are worth 10 points. And an Ace is worth 11.
        - __str__() (note the two underscores before and after) which returns a string
          "[value] of [suit]" (e.g. "Ace of Spades", or "Queen of Hearts"). The 
          __str__() method is another special method like __init__. It tells python 
          what to print when you call print(object).
'''
class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_suit(self):
        return self.suit

    def get_value(self):
        if self.value in ['Jack', 'King', 'Queen']:
            return 10
        elif self.value == 'Ace':
            return 11
        else:
            return int(self.value)

    def __str__(self):
        return f"{self.value} of {self.suit}"

#example
my_card = Card('Ace', 'Spades')
print(my_card.get_suit())  
print(my_card.get_value())  
print(str(my_card))

'''
2.  Create another Class called Deck. This class should have two attribute.
        - suits (a list of suits ['hearts', 'spades', 'diamonds', 'clubs'])
        - values (a list of values ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'King', 'Queen', 'Ace'])
    
    Create an __init__ method for Deck that creates the deck of 52 cards. Each of those
    52 cards should be created using the Card class.
        HINT: start off with an empty list self.cards = []
        HINT: You can use a double for-loop and your Card class to create your deck
              more easily than copy-pasting all 52 options
    
    Define an instance method, shuffle() which shuffles the order of your deck.
    look up some of the functions in the random library for this
        - 
    Define an instance method, draw(), which "deals" the last card in cards by removing
    it from cards, and returning it (hint: pop).

    Create a Deck object, shuffle it, and print out the result of drawing 5 cards

    BONUS: Also return the cumulative value using the getValue function in your Card
    class
'''

import random

class Deck:
    def __init__(self):
        self.suits = ['hearts', 'spades', 'diamonds', 'clubs']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'King', 'Queen', 'Ace']
        self.cards = []

        for suit in self.suits:
            for value in self.values:
                card = Card(value, suit)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            return None 
        return self.cards.pop()


def calculate_cumulative_value(cards):
    return sum(card.get_value() for card in cards)

#example
deck = Deck()
deck.shuffle()
drawn_cards = [deck.draw() for _ in range(5)]
for card in drawn_cards:
    print(card)
cumulative_value = calculate_cumulative_value(drawn_cards)
print("Cumulative Value:", cumulative_value)

#Higher or Lower Game 
def higher_or_lower_game():
    deck = Deck()
    deck.shuffle()

    score = 0
    current_card = deck.draw()

    while True:
        print("Current Card:", current_card)
        guess = input("Will the next card be higher or lower? Enter 'h' for higher, 'l' for lower: ").lower()

        if guess not in ['h', 'l']:
            print("Invalid input. Please enter 'h' for higher or 'l' for lower.")
            continue

        next_card = deck.draw()

        if next_card is None:
            print("No more cards in the deck. Game over.")
            break

        print("Next Card:", next_card)

        if (guess == 'h' and next_card.get_value() > current_card.get_value()) or \
           (guess == 'l' and next_card.get_value() < current_card.get_value()):
            print("Correct!")
            score += 1
        else:
            print("Incorrect. Game over.")
            break

        current_card = next_card

    print("Your score:", score)

if __name__ == "__main__":
    higher_or_lower_game()
