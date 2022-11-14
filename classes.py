from fractions import Fraction

class Player:
    def __init__(self):
        self.total_money = 100  # this can be changed later
        self.bet_won = 0
        self.total_money_won = 0
        self.money_on_table = 0
        self.items = {"double_bet": 0, "triple_bet": 0, "life_line": 0}
        self.tutorials_completed = []

    def bet(self, total_bet):
        """deducts and sets up the betting game

        :param total_bet: amount the Player wants to bet
        :return:
        """

        self.money_on_table += total_bet

    def win(self, bet_type):
        """calculates the winnings"""

        money_won = int(self.money_on_table * (0.1 if bet_type == "small"
                                               else 0.3 if bet_type == "med" else 0.5))
        self.total_money += money_won
        self.total_money_won += money_won
        self.bet_won += 1
        self.money_on_table = 0

        return money_won

    def lose(self):
        """calculates the losings"""

        self.total_money -= self.money_on_table
        self.money_on_table = 0


class Yintercept:
    def __init__(self, equation):
        self.equation = f'{equation[0]} + {equation[1]}= {equation[2]}'
        self.step1 = f'{equation[1]} = - {equation[0]} + {equation[2]}'
        self.step2 = f'1/6 x ({equation[1]} = - {equation[0]} + {equation[2]})'
        self.step3 = f'(1/6 x {equation[1]}) = (1/6 x - {equation[0]}) + (1/6 x {equation[2]})'
        self.step4 = f'7/6y = -x + 9/6'
        self.step5 = f'6/7 x (7/6y = -x + 9/6)'
        self.step6 = f'(6/7 x 7/6y) = (6/7 x -x) + (6/7 x 9/6)'
        self.step7 = f'y = -6x/7 + 9/7'
        self.step8 = 'DONE'
        self.steps = [self.equation, self.step1, self.step2, self.step3, self.step4, self.step5, self.step6, self.step7, self.step8]
