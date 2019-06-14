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
    '''Benchmarking different mortgages 
    
    amount = loan amount
    years = total years of repayment
    fixedRate = fixed interest rate for repayment --- example 0.07 is 7%
    pts = interest rate changes 3.25
    ptsRate = Fixed and variable rate for repayment
    varRate1 = intial varibale rate for repayment
    varRate2  = After rate hikes variable rate
    varMonths = Number of months for varibale rate
    '''        
    total_months = years*12
    fixed1 = Fixed(amount, fixedRate, total_months)
    fixed2 = FixedandVariable(amount, ptsRate, total_months, pts)
    twoRate = TwoRate(amount, varRate2, total_months, varRate1, varMonths)
    
    mortgages = [fixed1, fixed2, twoRate]
    for m in range(total_months):
        for mort in mortgages:
            mort.makePayment()
    plotMortgages(mortgages, amount)
        
# Visulisation 
import numpy as np
import matplotlib.pyplot as plt
        
def plotPayments(self, style):
    
    plt.plot(self.paid[1:], style, label = self.legend)

def plotBalance(self, style):
    
    plt.plot(self.owed, style, label = self.legend)


def plotTotPd(self, style):
    """Plot the cumulative total of the payments made"""
    totPd = [self.paid[0]]
    for i in range(1, len(self.paid)):
        totPd.append(totPd[-1] + self.paid[i])
    
    plt.plot(totPd, style, label = self.legend)

def plotNet(self, style):
    """Plot an approximation to the total cost of the mortgage
      over time by plotting the cash expended minus the equity
      acquired by paying off part of the loan"""
    totPd = [self.paid[0]]
    for i in range(1, len(self.paid)):
        totPd.append(totPd[-1] + self.paid[i])
 #Equity acquired through payments is amount of original loan
 # paid to date, which is amount of loan minus what is still owed
    equityAcquired = np.array([self.loan]*len(self.owed))
    equityAcquired = equityAcquired - np.array(self.owed)
    net = np.array(totPd) - equityAcquired
    plt.plot(net, style, label = self.legend)  
    
    
def plotMortgages(morts, amt):
    styles = ['b-', 'b-.', 'b:']
 #Give names to figure numbers
    payments = 0
    cost = 1
    balance = 2
    netCost = 3
    plt.figure(payments)
    plt.title('Monthly Payments of Different $' + str(amt)
     + ' Mortgages')
    plt.xlabel('Months')
    plt.ylabel('Monthly Payments')
    plt.figure(cost)
    plt.title('Cash Outlay of Different $' + str(amt) + ' Mortgages')
    plt.xlabel('Months')
    plt.ylabel('Total Payments')
    plt.figure(balance)
    plt.title('Balance Remaining of $' + str(amt) + ' Mortgages')
    plt.xlabel('Months')
    plt.ylabel('Remaining Loan Balance of $')
    plt.figure(netCost)
    plt.title('Net Cost of $' + str(amt) + ' Mortgages')
    plt.xlabel('Months')
    plt.ylabel('Payments - Equity $')
    for i in range(len(morts)):
         plt.figure(payments)
         morts[i].plotPayments(styles[i])
         plt.figure(cost)
         morts[i].plotTotPd(styles[i])
         plt.figure(balance)
         morts[i].plotBalance(styles[i])
         plt.figure(netCost)
         morts[i].plotNet(styles[i])
    plt.figure(payments)
    plt.legend(loc = 'upper center')
    plt.figure(cost)
    plt.legend(loc = 'best')
    plt.figure(balance)
    plt.legend(loc = 'best')