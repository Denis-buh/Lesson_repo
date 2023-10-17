



import math


print("-" * 60)
print("!{: ^28}!".format('X'), "{: ^28}!".format('y = f(x)'))
print("-" * 60)


for i in range(-500, 1000, 55):
    i /= 100
    # print(i)
    if i < -1:
        print("!{: ^28}!".format(i), "{: ^29}!".format(i ** 2))
        
    if 0 <= i <= 12.5:
        print("!{: ^28}!".format(i), 
              "{: ^29}!".format((math.e ** i) + 5 + math.cos(0.001 * i)))
        
    '''if i > 12.5:
        print("{: ^30}".format(i), 
              "{: ^30}".format((i ** 2) - 3 + (2.5 * (i ** 2))))'''
        
    