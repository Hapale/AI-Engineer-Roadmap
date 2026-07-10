class Signal:

    def action(self):

        print("General Signal")

class BuySignal(Signal):

    def action(self):

        print("BUY")

class SellSignal(Signal):

    def action(self):

        print("SELL")

buy = BuySignal()

sell = SellSignal()

buy.action()

sell.action()