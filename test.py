# -*- coding: utf-8 -*-

from ethereum import tester, slogging
import os

state = tester.state()

# Create Market Contract
market = state.abi_contract('contracts/market.se', gas=10000000)


# Create Match Maker
class Matchmaker:
    def listener(self, msg):
        if msg['event'] == 'LOG':
            print('announce', msg['topics'])

    def __init__(self):
        slogging.log_listeners.listeners.append(self.listener)

match_maker = Matchmaker()

# Create buy ticket, add preferences, activate
buy_ticket = market.add()
market.add_preference(buy_ticket, "price", 5)
market.activate(buy_ticket)

# Create sell ticket, add preferences, activate
sell_ticket = market.add()
market.add_preference(sell_ticket, "price", -5)
market.activate(sell_ticket)



# head = tail = xorll.insert("head", 10, 0, 0)
# tail = xorll.insert("tail", 20, 0, tail)

# tail = xorll.insert("monkey", 30, xorll.np(tail), tail)
# tail = xorll.insert("finger", 40, xorll.np(tail), tail)

# print('---')
# xorll.traverse(head)
# print('---')
# xorll.traverse(tail)
# print('---')
# xorll.test()
