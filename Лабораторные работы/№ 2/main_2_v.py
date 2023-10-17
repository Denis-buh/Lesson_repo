
import math

print('-'*33)
print('!', ' '*5, 'x', ' '*5, '!', ' ' *1, 'y = f (x)', ' '*1, '!')
print('-'*33)

for x in range (-2, 8):
    x *= math.pi/4
    if x > 2.5:
        y = x + 1
    if 0 <= x <= 1.5:
        y = 1 + x ** 2
    if x < 0:
        y = x * math.log (abs(math.cos(x)), math.e)
    print('!', '{:13.3}'.format(x), '!', '{:13.3}'.format(y), '!')