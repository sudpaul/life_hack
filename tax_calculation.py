from datetime import datetime, timedelta
from typing import Tuple, Optional
from rich.console import Console
from rich.table import Table

def compute_tax(income: int) -> Tuple[float, float]:
    """
    Compute the income tax based on predefined tax brackets.

    Args:
        income (int): The total taxable income.

    Returns:
        Tuple[float, float]: A tuple containing the calculated tax and the marginal tax rate.
    """
    tax_brackets = [
        (18200, 0, 0), (45000, 0.16, 0), (135000, 0.30, 4288), (190000, 0.37, 31288)
    ]
    # Australian resident individual tax rates for 2025-26
    # $0 – $18,200: Nil (Tax-Free Threshold)
    # $18,201 – $45,000: 16 cents for each $1 over $18,200
    # $45,001 – $135,000: $4,288 plus 30 cents for each $1 over $45,000
    # $135,001 – $190,000: $31,288 plus 37 cents for each $1 over $135,000
    # $190,001 and over: $51,538 plus 45 cents for each $1 over $190,000 
    highest_bracket = (None, 0.45, 51637)
    previous_cutoff = 0
    
    for cutoff, percent, additive in tax_brackets:
        if income <= cutoff:
            break
        previous_cutoff = cutoff
    else:
        _, percent, additive = highest_bracket

    tax = (income - previous_cutoff) * percent + additive
    return tax, percent

def run() -> None:
    """
    Run the tax calculation program.

    Prompts the user to enter their yearly gross income, computes the tax,
    and displays a summary using a formatted table.
    """
    console = Console()
    
    current_year = datetime.now().year
    previous_year = str((datetime.today() + timedelta(days=-365)).year)[2:]
    
    income = input(f"Enter yearly gross remuneration for tax calculation: ")
    gross = int(income)
    income_tax, marginal_rate = compute_tax(gross)
    medicare_levy = 0.02 * gross
    
    total_tax = income_tax + medicare_levy
    effective_rate = 100 * (total_tax / gross)
    rate_percent = 100 * marginal_rate
    net_income = gross - total_tax
    
    heading = f'Your tax summary for income year {current_year}-{previous_year}'
    
    table = Table(title=heading)
    
    table.add_column("Description", justify="right", style="cyan", no_wrap=True)
    table.add_column("Amount", justify="right", style="magenta")
    
    table.add_row("Total taxable income:", f"${gross}")
    table.add_row("Income tax payable:", f"${income_tax:.2f}")
    table.add_row("Medicare levy:", f"${medicare_levy:.2f}")
    table.add_row("Total tax:", f"${total_tax:.2f}")
    table.add_row("Net income after tax & Medicare levy:", f"${net_income:.2f}")
    table.add_row("Marginal tax rate:", f"{rate_percent:.2f}%")
    
    console.print(table)

if __name__ == '__main__':
    run()
