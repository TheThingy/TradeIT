# ! /usr/bin/env python3



class Loan:
    def __init__(self, loan):
        self.loan = loan

    def get_loan(self):
        return self.loan

    def set_loan(self, amount):
        self.loan = amount

    def do_intrest(self):
        self.loan *= 1.05
