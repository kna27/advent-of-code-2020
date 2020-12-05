with open("data_day05.txt", "r") as f:
    data = f.read().splitlines()

finalSeats = []

#Part 1
for line in data:
    vertical = line[0:7]
    backHalf = 0
    frontHalf = 127

    for x in vertical:
        half = (frontHalf - backHalf + 1) / 2
        if x == "F":
            frontHalf -= half
        elif x == "B":
            backHalf += half

    horizontal = line[7:]
    left = 0
    right = 7
    
    for i in horizontal:
        half = (right - left + 1) / 2
        if i == "L":
            right -= half
        elif i == "R":
            left += half

    finalSeats.append(int(backHalf * 8 + left)) 
seat = max(finalSeats)

print("Part 1:", seat)
 
#Part 2
for x in range(min(finalSeats), seat):
    if x not in finalSeats:
        print("Part 2:", x)