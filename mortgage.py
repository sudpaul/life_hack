# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 10:31:28 2018

@author: Sudipta
"""

def findPayment(loan,rate, month):
    
    return loan*((rate*(1+rate)**month)/((1+rate)**month -1))

class Mortgage(object):
    
   def __init__(self, loan, annualrate, months):
         
       self.loan = loan
       self.rate = annualrate/12
       self.months = months
       self.paid = [0.0]
       self.outstanding = [loan]
       self.payment = findPayment(loan, self.rate, months)
       self.legend = None
         
   def makePayment(self):
        
       self.paid.append(self.payment)
       reduction = self.payment - self.outstanding[-1]*self.rate
       self.outstanding.append(self.outstanding[-1] - reduction)
        
   def getTotalPaid(self):
        
       return sum(self.paid)
    
   def __str__(self):
        
       return self.legend
        
class Fixed(Mortgage):
     
    def __init__(self, loan, rate, months):
        Mortgage.__init__(self, loan, rate, months)
        self.legend = 'Fixed, ' + str(round(rate*100, 2)) + '%'
        
class FixedandVariable(Mortgage):
    
    def __init__(self, loan, rate, months, variable):
        Mortgage.__init__(self, loan, rate, months)
        self.variable = variable
        self.paid = [loan*(variable/100)]
        self.legend = 'Fixed, ' + str(round(rate*100, 2)) + '%, '\
                      + str(variable) + ' variable rate'

class TwoRate(Mortgage):
    
    def __init__(self, loan, rate, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths 
        self.teaserRate = teaserRate
        self.nextRate = rate/12
        self.legend = str(teaserRate*100) + '% for  ' + str(self.teaserMonths)\
                     + ' months, then ' + str(round(rate*100, 2)) + '%'
                     
    def makePayment(self):
        if len(self.paid) == self.teaserMonths +1 :
            self.rate = self.nextRate
            self.payment = findPayment(self.outstanding[-1], self.rate, 
                                       self.months- self.teaserMonths)
        Mortgage.makePayment(self)

def compareMortgages(amount, years, fixedRate, pts, ptsRate, varRate1,
                     varRate2, varMonths):
    total_months = years*12
    fixed1 = Fixed(amount, fixedRate, total_months)
    fixed2 = FixedandVariable(amount, ptsRate, total_months, pts)
    twoRate = TwoRate(amount, varRate2, total_months, varRate1, varMonths)
    
    mortgages = [fixed1, fixed2, twoRate]
    for month in range(total_months):
        for mortgage in mortgages:
            mortgage.makePayment()
    for m in mortgages:
        print(m)
        print(' Total payments = $' + str(int(m.getTotalPaid())))