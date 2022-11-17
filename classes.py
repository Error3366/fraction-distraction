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
