#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ethereum import tester
import os

from matchmaker import Matchmaker
from trader import Trader

state = tester.state()

# Create Market Contract
# TODO: remove gas
market = state.abi_contract('contracts/market.se', gas=10000000)

# Create Actors
match_maker = Matchmaker(state, market, name='MatchMaker')
buyer = Trader(state, market, name='Buyer')
seller = Trader(state, market, name='Seller')

# Setup our simple Buy and Sell tickets
buyer.new_ticket(5)
seller.new_ticket(-5)

# Run the Network!
state.mine(n=20)
