import random


"""
    Este arquivo foi o esboço inicial para o projeto antes de fazer melhorias.
"""


class Player:
    def __init__(self, behavior, starting_balance):
        self.position = 0
        self.behavior = behavior
        self.balance = starting_balance
        self.properties = []

    def take_turn(self, board):
        roll = random.randint(1, 6)
        position = (self.position + roll) % 20
        property = board[position]

        if property.owner is None:
            if self.behavior == "impulsive":
                self.buy_property(property)
            elif self.behavior == "demanding":
                if property.rent > 50:
                    self.buy_property(property)
            elif self.behavior == "cautious":
                if self.balance - property.price >= 80:
                    self.buy_property(property)
            elif self.behavior == "random":
                if random.random() < 0.5:
                    self.buy_property(property)
        elif property.owner is not self:
            self.pay_rent(property)

        if position == 19:
            self.balance += 100

    def buy_property(self, property):
        self.balance -= property.price
        self.properties.append(property)
        property.owner = self

    def pay_rent(self, property):
        self.balance -= property.rent
        property.owner.balance += property.rent


class Property:
    def __init__(self, price, rent):
        self.price = price
        self.rent = rent
        self.owner = None


def play_game(player1, player2, player3, player4):
    board = [Property(random.randint(50, 200), random.randint(10, 50)) for i in range(20)]
    players = [player1, player2, player3, player4]
    random.shuffle(players)

    turn = 0
    while turn < 1000:
        for player in players:
            if player.balance >= 0:
                player.take_turn(board)
            else:
                players.remove(player)

        turn += 1

        if len(players) == 1:
            return players[0], turn

    balances = [player.balance for player in players]
    winner = players[balances.index(max(balances))]

    return winner, turn


def simulate(num_simulations):
    impulsives = 0
    demandings = 0
    cautious = 0
    randoms = 0
    total_turns = 0
    games_timed_out = 0

    player1 = Player("impulsive", 300)
    player2 = Player("demanding", 300)
    player3 = Player("cautious", 300)
    player4 = Player("random", 300)

    for i in range(num_simulations):

        winner, turns = play_game(player1, player2, player3, player4)
        total_turns += turns

        if winner is None:
            games_timed_out += 1
        elif winner.behavior == "impulsive":
            impulsives += 1
        elif winner.behavior == "demanding":
            demandings += 1
        elif winner.behavior == "cautious":
            cautious += 1
        elif winner.behavior == "random":
            randoms += 1

    print("Number of games timed out:", games_timed_out)
    print("Average number of turns per game:", total_turns / num_simulations)
    print("Percentage of wins by behavior:")
    print("  Impulsive:", impulsives / num_simulations * 100, "%")
    print("  Demanding:", demandings / num_simulations * 100, "%")
    print("  Cautious:", cautious / num_simulations * 100, "%")
    print("  Random:", randoms / num_simulations * 100, "%")

    if impulsives > demandings and impulsives > cautious and impulsives > randoms:
        print("Impulsive behavior wins the most.")
    elif demandings > impulsives and demandings > cautious and demandings > randoms:
        print("Demanding behavior wins the most.")
    elif cautious > impulsives and cautious > demandings and cautious > randoms:
        print("Cautious behavior wins the most.")
    else:
        print("Random behavior wins the most.")


if __name__ == "__main__":
    simulate(300)