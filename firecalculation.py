from rich import print
from rich.console import Console
from rich.prompt import Prompt

def calculate_fire_number(annual_expenses, withdrawal_rate=0.04):
    """
    Calculate the amount of money needed to achieve financial independence.

    Parameters:
    annual_expenses (float): The amount of money you need to cover your annual expenses.
    withdrawal_rate (float): The safe withdrawal rate. Default is 4% (0.04).

    Returns:
    float: The total amount of money needed to achieve financial independence.
    """
    return annual_expenses / withdrawal_rate

def calculate_years_to_fire(current_savings, annual_contribution, annual_return_rate, fire_number):
    """
    Calculate the number of years needed to reach financial independence.

    Parameters:
    current_savings (float): The amount of money currently saved.
    annual_contribution (float): The amount of money contributed to the savings annually.
    annual_return_rate (float): The annual return rate of the investments.
    fire_number (float): The target amount needed for financial independence.

    Returns:
    int: The number of years needed to reach financial independence.
    """
    years = 0
    while current_savings < fire_number:
        current_savings += current_savings * annual_return_rate + annual_contribution
        years += 1
    return years

def main():
    console = Console()

    # User inputs with rich prompts
    annual_expenses = float(Prompt.ask("[bold green]Enter your annual expenses[/]", default="40000"))
    withdrawal_rate = float(Prompt.ask("[bold green]Enter your withdrawal rate (default is 4%)[/]", default="0.04"))
    current_savings = float(Prompt.ask("[bold green]Enter your current savings[/]", default="100000"))
    annual_contribution = float(Prompt.ask("[bold green]Enter your annual contribution[/]", default="20000"))
    annual_return_rate = float(Prompt.ask("[bold green]Enter your expected annual return rate (as a decimal, e.g., 0.07 for 7%)[/]", default="0.07"))

    # Calculate the FIRE number
    fire_number = calculate_fire_number(annual_expenses, withdrawal_rate)
    console.print(f"\n[bold blue]To achieve financial independence, you need to save:[/bold blue] [bold yellow]${fire_number:,.2f}[/bold yellow]")

    # Calculate the number of years to reach FIRE
    years_to_fire = calculate_years_to_fire(current_savings, annual_contribution, annual_return_rate, fire_number)
    console.print(f"[bold blue]With your current savings and annual contributions, you will reach financial independence in:[/bold blue] [bold yellow]{years_to_fire} years[/bold yellow]")

if __name__ == "__main__":
    main()
