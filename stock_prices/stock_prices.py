#!/usr/bin/python

import argparse


def find_max_profit(price):
    profit_loss = -100
    for i in range(0, len(price)):
        buy_to_open = i
        for j in range(0, len(price)):
            sell_to_close = j
            if price[j] - price[i] > profit_loss and buy_to_open < sell_to_close:
                profit_loss = price[j] - price[i]
    return profit_loss


if __name__ == '__main__':
            # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
