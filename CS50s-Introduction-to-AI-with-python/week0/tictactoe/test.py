from tictactoe import *

s0 = initial_state()

ac0 = actions(s0)
print(ac0)
s1 = result(s0, ac0[1])
print(s1)

ac1 = actions(s1)
print(ac1)
s2 = result(s1, ac1[4])
print(s2)
