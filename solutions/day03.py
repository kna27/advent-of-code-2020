x = open("data_day03.txt").readlines()
lines = []
for i in x:
    lines.append(i.strip())

def checkCrash(run, rise):
    t = 0
    y = 0
    for x in range(0, len(lines), rise):
        if lines[x][y] == "#":
            t += 1
        y = (y + run) % len(lines[0])
    return t

# Part 1
print("Part 1:", checkCrash(3,1))

# Part 2
print("Part 2:", checkCrash(1,1)*checkCrash(3,1)*checkCrash(5,1)*checkCrash(7,1)*checkCrash(1,2))