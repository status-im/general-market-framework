#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ethereum import tester
import os

from matchmaker import Matchmaker

state = tester.state()

# Create Market Contract
# TODO: remove gas
market = state.abi_contract('contracts/market.se', gas=10000000)

# Create Match Maker
match_maker = Matchmaker(state, market)

# Create buy ticket, add preferences, activate
buy_ticket = market.add()
market.add_preference(buy_ticket, 'head', 10)
market.add_preference(buy_ticket, 'tail', 20)
market.add_preference(buy_ticket, 'price', 5)
market.activate(buy_ticket)

# Create sell ticket, add preferences, activate
sell_ticket = market.add()
market.add_preference(sell_ticket, 'price', -5)
market.activate(sell_ticket)

# Move into Sealed Window
print('sealed window')
state.mine(n=1)

# Move into Reveal Window
print('reveal window')
state.mine(n=2)

print('accept window')
# Move into Accept Window
state.mine(n=1)
print('fin')
