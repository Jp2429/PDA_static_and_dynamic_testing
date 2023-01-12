import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def test_check_for_ace(self):
        card= Card("hearts",10)
        result=CardGame.check_for_ace(self,card)
        self.assertEqual(result,False)

    def test_highest_card(self):
        card1= Card("hearts",10)
        card2= Card("spade",1)
        result=CardGame.highest_card(self,card1,card2)
        self.assertEqual(result,card1)

    def test_cards_total(self):
        card1= Card("hearts",10)
        card2= Card("spade",1)
        card3= Card("diamond",7)
        cards=[card1,card2,card3]
        result=CardGame.cards_total(self,cards)
        self.assertEqual(result,"You have a total of 18")