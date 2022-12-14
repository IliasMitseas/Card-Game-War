# Card
# Suit , Rank, Value
import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")

ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
          "Nine", "Ten", "Jack", "Queen", "King", "Ace")

values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven": 7, "Eight": 8,
          "Nine":9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for i in suits:
            for y in ranks:
                created_card = Card(i, y)
                self.all_cards.append(created_card)

    def shuffle(self):
        #shuffle the deck
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            #list of multiples Card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single Card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name}: has {len(self.all_cards)} cards"

#Game setup
player_one = Player("Ilias")
player_two = Player("John")
new_deck = Deck()
new_deck.shuffle()

for i in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
# while
count = 0
while game_on:
    count += 1
    print(f"Round {count}")
    if len(player_one.all_cards) == 0:
        print("Player one out of Cards! Player two wins")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player two out of Cards! Player one wins")
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)

            at_war = False
        else:
            print("WAR")
            if len(player_one.all_cards) < 5:
                print("Player one unable to declare war")
                print("Player two WINS")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print("Player two unable to declare war")
                print("Player one WINS")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())