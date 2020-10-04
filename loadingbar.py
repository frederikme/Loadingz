import sys
import time


class Loadingbar:

    def __init__(self, length_of_loop, explanation="", amount_of_bars=30):

        self.length_of_loop = length_of_loop
        self.amount_of_bars = amount_of_bars
        sys.stdout.write("{}\n".format(explanation))
        self.update(index=-1)

    def update(self, index):
        sys.stdout.write('\r')

        percentage_loaded = int((index + 1)*100 / self.length_of_loop)

        if percentage_loaded > 100:
            percentage_loaded = 100

        # [===>----] 45% of new matches scraped
        amount_of_equals = int(percentage_loaded / 100 * self.amount_of_bars)
        amount_of_minus = self.amount_of_bars - amount_of_equals - 1

        printout = "[{}>{}] {}%".format('=' * amount_of_equals, '-' * amount_of_minus, percentage_loaded)
        sys.stdout.write(printout)
        sys.stdout.flush()
        time.sleep(0.25)
