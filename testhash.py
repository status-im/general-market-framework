#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bitcoin
from ethereum import tester, utils

state = tester.state()

# 0 288
# 100 288
# ('zpadhash', 92268809646399479600174377094284069493881770942972924356240893702142402791897L)
# ('sha3int_zpad', 27004694829266425565490061128739172021375112860617960595218055460725948937951L)
# ('sha3int', 27004694829266425565490061128739172021375112860617960595218055460725948937951L)
# 0 270
# 200 270
# ('hash_arr', 8151782650644729368062958368917604144436969866772708851468873220389632519965L)
# ('hash_param', 7896341980786613614968953046582703950699541199067738665672778972695176727887L)
# ('hash_param_zpad', 7896341980786613614968953046582703950699541199067738665672778972695176727887L)
# ('hash_hardcode', 7896341980786613614968953046582703950699541199067738665672778972695176727887L)
# [Finished in 0.6s]

code = '''
def hash_arr(test:arr):
    return(sha3(test:arr):uint256)

def hash_param(a, b, c):
    return(sha3([a, b, c]:arr):uint256)

def foo():
    return(sha3([0, 0, 1]:arr):uint256)
'''

# hash_arr also gives wildly different results depending on hash_param existence

hashtest = state.abi_contract(code)

tmp = [0, 0, 1]


print('hash_arr', hashtest.hash_arr(tmp))
print('hash_param', hashtest.hash_param(tmp[0], tmp[0], tmp[0]))

print(hashtest.foo())
a = utils.sha3(''.join(map(lambda x: utils.zpad(utils.encode_int(x), 32), tmp)))
print(utils.decode_int(a))
