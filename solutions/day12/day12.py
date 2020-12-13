x = open('data_day12.txt')
f = [line.strip() for line in x]
asdf = 0
position = [0, 0]
actions = ["N", "S", "E", "W", "L", "R", "F"]
direc = 1

#Part 1
print(position)
if direc == 0:
    print("^")
elif direc == 1:
    print(">")
elif direc == 2:
    print("v")
elif direc == 3:
    print("<")

for i in f:
    asdf += 1
    a = i[0]
    e = int(i[1:])
    if a == actions[0]:
        position[0] += e
    elif a == actions[1]:
        position[0] -= e
    elif a == actions[2]:
        position[1] += e
    elif a == actions[3]:
        position[1] -= e
    elif a == actions[4]:
        direc -= e/90
        if direc < 0:
            direc += 3
    elif a == actions[5]:
        direc += e/90
        if direc > 3:
            direc -= 4
    elif a == actions[6]:
        if direc == 0:
            position[0] += e
        elif direc == 1:
            position[1] += e
        elif direc == 2:
            position[0] -= e
        elif direc == 4:
            position[1] -= e
manVal = abs(position[0]) + abs(position[1])
print(manVal)
    

sin = {0:0, 90:1, 180:0, 270:-1}
cos = {0:1, 90:0, 180:-1, 270:0}
    
x = y = dir = 0
wx = 10
wy = 1
for op, val in [(x[:1],int(x[1:])) for i in f]:
    if op == 'N':
        wy += val
    elif op == 'S':
        wy -= val
    elif op == 'E':
        wx += val
    elif op == 'W':
        wx -= val
    elif op == 'R':
        nwx = wx*cos[-val%360] - wy*sin[-val%360]
        nwy = wx*sin[-val%360] + wy*cos[-val%360]
        wx, wy = nwx, nwy
    elif op == 'L':
        nwx = wx*cos[val%360] - wy*sin[val%360]
        nwy = wx*sin[val%360] + wy*cos[val%360]
        wx, wy = nwx, nwy
    else:
        x += val*wx
        y += val*wy

print(abs(x)+abs(y))


#Part 2, much more simple and shorter than part 1

p = 0+0j
w = 10+1j

o = {'E':1+0j,'N':0+1j,'W':-1+0j,'S':0-1j}
rotation = {'L':0+1j,'R':0-1j}

for line in f:
    letter = line[0]
    number = int(line[1:-1])
    d = w-p
    if letter in "ENWS":
        w += number*o[letter]
    elif letter == "F":
        p += number*d
        w += number*d
    elif letter in "RL":
        d *= rotation[letter]**(number//90)
        w = p+d

print(p,abs(p.real)+abs(p.imag))