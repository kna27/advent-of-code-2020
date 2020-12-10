from collections import namedtuple
Entry = namedtuple("Entry", "low high char pw")

inpt = []
for line in open("data_day02.txt"):
    allowed, char, pw = line.split()
    minNum, maxNum = map(int, allowed.split('-'))
    inpt.append(Entry(minNum, maxNum, char[0], pw))


#Part 1
def valid_1(num):
    return num.low <= num.pw.count(num.char) <= num.high

#Part 2
def valid_2(num):
    return (num.pw[num.low-1]==num.char) ^ (num.pw[num.high-1]==num.char)

print("Part 1:", sum(map(valid_1, inpt)))
print("Part 2:", sum(map(valid_2, inpt)))