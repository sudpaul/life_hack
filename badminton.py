# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:52:11 2020

@author: z3525552
"""

import operator

class Player:

    max_name_len = 0
    template = '{name:>{name_len}} paid ${paid:7.2f}'

    def __init__(self, name, paid=0.0):
        self.name = name
        self.paid = float(paid)
        if len(name) > Player.max_name_len:
            Player.max_name_len = len(name)

    def pay(self, amount):
        self.paid += float(amount)

    def display(self):
        return Player.template.format(
            name = self.name,
            name_len = self.max_name_len,
            paid = self.paid,
        )

class Budget:
    """
    Class ``badminton.Budget`` represents the budget for a badminton session.
    """
    
    
    def __init__(self, *names,court_hire = 30.00):
        self._players = {name: Player(name) for name in names}
        self._cost = court_hire

    def total(self):
        return sum(c.paid for c in self._players.values())

    def people(self):
        return sorted(self._players)

    def contribute(self, name, amount):
        if name not in self._players:
            raise LookupError("Name not in budget")
        self._players[name].pay(amount)

    def individual_share(self):
        return self.total() / len(self._players)

    def report(self):
        """report displays names and amounts due or owed"""
        share = self.individual_share()
        heading_tpl = 'Total: $ {:.2f}; single session cost: $ {:.2f}'
        print(heading_tpl.format(self.total(), self._cost))
        print("-"* 52)
        sorted_players = sorted(self._players.values(), key=operator.attrgetter('paid'))
        for player in sorted_players:
            balance = f'balance: $ {player.paid - share:7.2f}'
            print(player.display(), balance, sep=', ')
