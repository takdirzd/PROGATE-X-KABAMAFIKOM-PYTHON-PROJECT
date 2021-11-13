from atm_card import ATM_Card
class customer:
    def __init__ (self,id,custpin = 1234,custbalance= 1234):
        self.id = id
        self.pin = custpin
        self.balance = custbalance

    def checkid(self):
        return self.id
    def checkcustpin(self):
        return self.pin
    def checkcustbalance(self):
        return self.balance

    def withdrawbalance(self, nominal):
        self.balance -= nominal
    def depositbalance(self, nominal):
        self.balance += nominal
