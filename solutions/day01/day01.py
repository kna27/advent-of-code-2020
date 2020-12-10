numbers = open("data_day01.txt").readlines()
from itertools import permutations

for x in range(len(numbers)):
    numbers[x] = int(numbers[x])

#Part 1
solutions1 = [pair for pair in permutations(numbers, 2) if sum(pair) == 2020]
p1 = solutions1[0][0]*solutions1[0][1]

#Part 2
solutions2 = [pair for pair in permutations(numbers, 3) if sum(pair) == 2020]
p2 = solutions2[0][0]*solutions2[0][1]*solutions2[0][2]

print('Part 1:', p1)
print('Part 2:', p2)