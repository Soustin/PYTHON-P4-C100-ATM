class Atm(object):
    def __init__(self, cardNo, pinNo, cardHolder):
        self.cardNo = cardNo
        self.pinNo = pinNo
        self.cardHolder = cardHolder
        print("Card Number: " + self.cardNo + " Pin Number: " + self.pinNo + " CardHolder Name: " + self.cardHolder)
    def cashWithdrawl(self):
        print("Withdraw Cash")
    def balanceEnquiry(self):
        print("Enquiry on Balance")
        
NotansATM = Atm("1234567890123456", "1874", "Notan Roy")
print(NotansATM.__init__(NotansATM.cardNo, NotansATM.pinNo, NotansATM.cardHolder))
print(NotansATM.cashWithdrawl())
print(NotansATM.balanceEnquiry())