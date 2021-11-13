class ATM_Card:
    def __init__(self,defaultpin,defaultbalance):
            self.defaultpin = defaultpin
            self.defaultbalance = defaultbalance

    def cekpinawal(self):
        return self.defaultpin

    def ceksaldoawal(self):
        return self.defaultbalance
