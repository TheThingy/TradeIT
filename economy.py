# ! /usr/bin/env python3



class Loan:
    def __init__(self, loan, interest=0.05):
        self.loan = loan
        self.interest = interest

    def get_loan(self):
        return self.loan

    def set_loan(self, amount):
        self.loan = amount
        
    def add_loan(self, amount):
        self.loan += amount

    def get_interest(self):
        return self.loan*self.interest
