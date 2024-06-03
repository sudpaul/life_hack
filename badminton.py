import operator
from rich.console import Console
from rich.table import Table
from rich.text import Text

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
            name=self.name,
            name_len=Player.max_name_len,
            paid=self.ppaid,
        )

class Budget:
    """
    Class ``badminton.Budget`` represents the budget for a badminton session.
    """
    def __init__(self, *names, court_hire=30.00, shuttle_cost=10.00):
        self._players = {name: Player(name) for name in names}
        self._cost = court_hire + shuttle_cost
        self._shuttle_cost = shuttle_cost

    def total(self):
        return sum(c.paid for c in self._players.values())

    def people(self):
        return sorted(self._players)

    def contribute(self, name, amount):
        if name not in self._players:
            raise LookupError("Name not in budget")
        self._players[name].pay(amount)

    def individual_share(self):
        return self._cost / len(self._players)

    def report(self):
        """report displays names and amounts due or owed"""
        share = self.individual_share()
        heading_tpl = 'Total: $ {:.2f}; single session cost: $ {:.2f}'
        
        console = Console()
        table = Table(title="Badminton Session Report")

        table.add_column("Player", justify="right", style="cyan", no_wrap=True)
        table.add_column("Paid", justify="right", style="green")
        table.add_column("Balance", justify="right", style="magenta")

        console.print(heading_tpl.format(self.total(), self._cost))
        console.print("-"* 52)
        
        sorted_players = sorted(self._players.values(), key=operator.attrgetter('paid'))
        for player in sorted_players:
            balance = player.paid - share
            balance_text = Text(f"${balance:7.2f}")
            if balance < 0:
                balance_text.stylize("bold red")
            table.add_row(player.name, f"${player.paid:7.2f}", balance_text)
        
        console.print(table)

# Example usage:
budget = Budget("Asif", "Sudipta", "Tipu", "Emon", "Suman", "Ashraf", court_hire=34, shuttle_cost=36.00)
budget.contribute("Asif", 50)
budget.contribute("Sudipta",75)
budget.contribute("Tipu", 35)
budget.report()
