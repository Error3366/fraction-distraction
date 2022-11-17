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

        if self.total_money < 0:
            self.total_money = 0


class Yintercept:
    def __init__(self, equation):
        self.equation = f'{equation[0]} + {equation[1]}= {equation[2]}'
        self.step1 = f'Isolate 7y: {equation[1]} = - {equation[0]} + {equation[2]}'
        self.step2 = f'Divide equation by 1/7: 1/7 x ({equation[1]} = - {equation[0]} + {equation[2]})'
        self.step3 = f'(1/7 x {equation[1]}) = (1/7 x - {equation[0]}) + (1/7 x {equation[2]})'
        self.step4 = f'7/7y = -6x/7 + 9/7'
        self.step5 = f'y = -6x/7 + 9/7'
        self.step6 = 'DONE'
        self.steps = [self.equation, self.step1, self.step2, self.step3, self.step4, self.step5, self.step6]


class Transform:

    def __init__(self):
        self.equation = f' 3 4/6 '
        self.step1 = f'3 + 4/6'
        self.step2 = f'3 = 18/6'
        self.step3 = f'18/6 + 4/6'
        self.step4 = f'(18+4)/6'
        self.step5 = f'22/6'
        self.step6 = 'DONE'
        self.steps = [self.equation, self.step1, self.step2, self.step3, self.step4, self.step5, self.step6]


class Add:
    def __init__(self):
        self.equation = f'4/7 + 8/5'
        self.step1 = f'(5/5 × 4/7) + (7/7 × 8/5)'
        self.step2 = f'20/35 + 56/35'
        self.step3 = f'76/35'
        self.step4 = f'DONE'
        self.steps = [self.equation, self.step1, self.step2, self.step3, self.step4]


class Divide:
    def __init__(self):
        self.equation = f'(4/7) ÷  (8/5)'
        self.step1 = f'Multiply 4/7 by reciprocal of 8/5'
        self.step2 = f'4/7 × 5/8'
        self.step3 = f'(4 × 5) / (7 × 8)'
        self.step4 = f'20/56'
        self.step5 = f'DONE'
        self.steps = [self.equation, self.step1, self.step2, self.step3, self.step4, self.step5]


class Multiply:
    def __init__(self):
        self.equation = f' 7/9 × 2/3'
        self.step1 = f'(7 × 2) / (9 × 3)'
        self.step2 = f'14/27'
        self.step3 = 'DONE'
        self.steps = [self.equation, self.step1, self.step2, self.step3]


class LCD:

    def __init__(self):
        self.equation = f'Find Least Common Denominator of 2/9 and 7/6'
        self.step1 = f'Factorize 9 and 6'
        self.step2 = f'9 = 3 × 3  and 6 = 3 × 2'
        # need step in between here to explain next step of finding lcd
        self.step3 = f'LCD = 3 × 3 × 2'
        self.step4 = f'LCD = 18'
        self.step5 = 'DONE'
        self.steps = [self.equation, self.step1, self.step2, self.step3, self.step4, self.step5]


class Subtract:

    def __init__(self):
        self.equation = f'3/7 - 5/14'
        self.step1 = f'LCD = 14'
        self.step2 = f' (2/2 × 3/7) - (1/1 × 5/14)'
        self.step3 = f'6/14 - 5/14'
        self.step4 = f'(6-5)/14'
        self.step5 = f'1/14'
        self.step6 = 'DONE'
        self.steps = [self.equation, self.step1, self.step2, self.step3, self.step4, self.step5, self.step6]
