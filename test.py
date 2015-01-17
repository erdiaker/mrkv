
from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
  zip, round, input, int, pow, object)

from mrkv import Markov
import random
from collections import Counter

def test1():
  # deterministic markov chain
  states = ['a', 'b', 'c', 'd', 'e']
  m = Markov(order=2)
  m.addTransitions(states)
  seq = m.generateSequence(['a','b'], 3)
  assert(seq == states)

def test2():
  # should contain only 'a' and 'b'
  length = 10
  order = 3
  states = ['a']*length + ['b']*length
  random.shuffle(states)
  m = Markov(order)
  m.addTransitions(states)
  seq = m.generateSequence(states[:order], length)
  c = Counter(seq)
  assert(c['a'] + c['b'] == length)

if __name__ == '__main__':
  test1()
  test2()

