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
            # TODO: get ticket preferences

    def __init__(self):
        pass
        # slogging.log_listeners.listeners.append(self.listener)

match_maker = Matchmaker()

# Create buy ticket, add preferences, activate
buy_ticket = market.add()
print('buy_ticket', buy_ticket)
market.add_preference(buy_ticket, 'price', '5')
market.activate(buy_ticket)

# Create sell ticket, add preferences, activate
sell_ticket = market.add()
print('sell_ticket', sell_ticket)
market.add_preference(sell_ticket, 'price', '-7')  # TODO: handle negative numbers
market.activate(sell_ticket)

# print('reveal', market.add_sealed_offer(0, 1))

print('enumerate buy_ticket preferences')
market.get_preferences(buy_ticket)

print('enumerate sell_ticket preferences')
market.get_preferences(sell_ticket)
