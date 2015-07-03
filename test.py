# -*- coding: utf-8 -*-

from ethereum import tester, slogging

state = tester.state()


def listener(msg):
    if msg['event'] == 'LOG':
        print(msg)

slogging.log_listeners.listeners.append(listener)

with open('contracts/minheap.se') as fh:
    minheap_se = fh.read()

with open('contracts/xorlist.se') as fh:
    xorlist_se = fh.read()


minheap = state.abi_contract(minheap_se)
xorlist = state.abi_contract(xorlist_se)

minheap.push(5)
minheap.push(10)
# minheap.pop()
print(minheap.top())
