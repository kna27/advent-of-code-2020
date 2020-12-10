file = open("data_day10.txt").readlines()
data = [int(line.strip()) for line in file if line.strip()]
data.sort()

#Part 1
data = [0] + data + [data[-1] + 3]
last = 0
one, three = 0, 0
for x in data:
    if x - last == 1:
        one += 1
    elif x - last == 3:
        three += 1
    last = x
p1 = one * three
print("Part 1:", p1)

#Part 2
dat = [1]
for i in range(1, len(data)):
    sol = 0
    for x in range(i):
        if data[x] + 3 >= data[i]:
            sol += dat[x]
    dat.append(sol)
print("Part 2:", sol)