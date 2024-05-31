# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:47:42 2020

@author: z3525552
"""
from datetime import datetime,timedelta
def compute_tax(income):
     # (cutoff, percent, additive)
    # S is reused from the previous iteration of the loop
    
    tax_brackets = [
        (18200, 0, 0), (45000, 0.16, 0), (135000, 0.30, 4288), (190000, 0.37, 31288)
    ]
    # The final bracket, use if the income is bigger than any cutoff
    highest_bracket = (None, 0.45, 51637)
    previous_cutoff = 0
    for cutoff, percent, additive in tax_brackets:
        if income <= cutoff:
            break
        previous_cutoff = cutoff
    else:
        # If we get here we never found a bracket to stop in
        _, percent, additive = highest_bracket

    tax = (income - previous_cutoff) * percent + additive
    return tax, percent

def run():
    
    year = datetime.now().year
    next_year = str((datetime.today()+ timedelta(days=365)).year)[2:]
    income = input(f"Enter yearly gross remuneration for tax caluculation  ")
    print()
    gross = int(income)
    income_tax, marginal_rate = compute_tax(gross)
    medicare_levey = 0.02*(gross)
    heading_tpl = f'Your tax summary for income year {year}-{next_year}'
    print(heading_tpl)
    print()
    print("*"* 52)
    total_tax = income_tax + medicare_levey
    effective_rate = 100*(total_tax/gross)
    rate_percent = 100*marginal_rate
    net_income = gross - (income_tax + medicare_levey)
    print(f"{'Total taxable income:':>35} ${gross}\n")
    
    print(f'Income tax payable ${income_tax:.2f}')
    print(f'Medicare levey $ {medicare_levey:.2f}')
    print(f'Total tax $ {total_tax:.2f}\n')
    
    print(f'Net income after tax & Medicare levy: ${net_income:.2f}')
    print(f'Marginal tax rate {rate_percent}%')
    
if __name__ == '__main__':
    run()