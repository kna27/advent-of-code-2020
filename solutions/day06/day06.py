x = open("data_day06.txt").read()
newList = x.split("\n\n")

while("" in newList) : 
    newList.remove("") 

final = 0
#Part 1
for i in newList:
    i = i.replace('\n', '')
    unique = []
    for char in i:
        if char not in unique:
            unique.append(char)
    final += len(unique)
    unique.clear()

print("Part 1:", final)


#Part 2
def intersection(first, *others):
    return set(first).intersection(*others)

final = 0
for i in newList:
    people = [set(x) for x in i.split('\n')]
    final += len(intersection(*people))

print("Part 2:", final)