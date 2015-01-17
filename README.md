mrkv
====
A simple library for playing with discrete-time Markov chains. Python 2 & 3
compatible.

# Examples
```python
from mrkv import Markov

# create a Markov chain of order 1.
m = Markov(order=1)           

# add some transitions
m.addTransition('a', 'b')     
m.addTransition('b', 'a')

# generate a single state
state = m.generate('a')  # should be 'b'

# add a sequence of transitions
m.addTransitions(['c', 'd', 'e', 'f'])
seq = m.generateSequence('c', 3)  # should be ['d', 'e', 'f']

# a non-deterministic chain.
m2 = Markov(order=1)
m2.addTransitions('bbaabbabbbbbababaaaaabbab')
noidea = m2.generateSequence('b', 7) # a sequence of a's and b's length 7
```

# License
MIT

