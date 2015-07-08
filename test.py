# -*- coding: utf-8 -*-

from ethereum import tester, slogging

state = tester.state()


def listener(msg):
    if msg['event'] == 'LOG':
        print(msg['topics'])

slogging.log_listeners.listeners.append(listener)

with open('contracts/market.se') as fh:
    market_se = fh.read()


market = state.abi_contract(market_se)

ticket = market.add()
print(ticket)
ticket2 = market.add()
print(ticket)
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
