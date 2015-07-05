# -*- coding: utf-8 -*-

from ethereum import tester, slogging

state = tester.state()


def listener(msg):
    if msg['event'] == 'LOG':
        print(msg['topics'])

slogging.log_listeners.listeners.append(listener)

with open('contracts/minheap.se') as fh:
    minheap_se = fh.read()

with open('contracts/xorll.se') as fh:
    xorll_se = fh.read()


minheap = state.abi_contract(minheap_se)
# xorll = state.abi_contract(xorll_se)

# minheap.push(5)
# minheap.push(2)
# minheap.push(10)
# print(minheap.top(), minheap.size())

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
