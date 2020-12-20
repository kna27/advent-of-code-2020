from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

# Above is the CRT from rosettacode.org used to answer part 2 of this problem

x= open("data_day13.txt").readlines()

minTime, schedule = int(x[0]), x[1]
start, s2 = minTime, minTime

busses = [int(x) if x != "x" else None for x in schedule.split(",")]

#Part 1
f = True
while f:
    for i in busses:
        if i and s2 % i == 0:
            print("Part 1:", i * (s2 - start))
            f = False
    s2 += 1

#Part 2
n = []
a = []
for i, m in enumerate(busses):
    if m:
        n.append(m)
        a.append(m-i)


print("Part 2:", chinese_remainder(n, a))