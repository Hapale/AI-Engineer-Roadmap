class BuySignal:

    def execute(self):

        print("BUY")


class SellSignal:

    def execute(self):

        print("SELL")


signals = [BuySignal(), SellSignal()]

for signal in signals:

    signal.execute()