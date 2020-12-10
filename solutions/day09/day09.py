from itertools import permutations
nums = open("data_day09.txt").readlines()

for x in range(len(nums)):
    nums[x] = int(nums[x])

#Part 1
for i in range(25, len(nums)):
    p1 = nums[i]
    prev = nums[i - 25: i]
    if not any((p1 - x) in prev for x in prev):
        break
print("Part 1:", p1)

#Part 2
for i in range(2, len(nums)):
    possCombos = [nums[k:k+i] for k in range(0, len(nums))]
    if p1 in [sum(combo) for combo in possCombos]:
        answerList = possCombos[[sum(combo) for combo in possCombos].index(p1)]
        answerList.sort()
        p2 = answerList[0] + answerList[-1]
        break
print("Part 2:", p2)
