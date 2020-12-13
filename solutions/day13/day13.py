x= open("data_day13.txt").readlines()
minTime, s = x[0], x[1]

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
 
 
 
if __name__ == '__main__':
    n = [3, 5, 7]
    a = [2, 3, 2]
    print(chinese_remainder(n, a))

# Above is the CRT from rosettacode.org used to answer part 2 of this problem

start, s2 = int(minTime), int(minTime)
bus = [int(x) if x != "x" else None for x in s.split(",")]

#Part 1
f = True
while f:
    for m in bus:
        if m and s2 % m == 0:
            print("Part 1:", m * (s2 - start))
            f = False
    s2 = s2 + 1

n = []
a = []
for i, m in enumerate(bus):
    if m:
        n.append(m)
        a.append(m-i)

#Part 2
print("Part 2:", chinese_remainder(n, a))