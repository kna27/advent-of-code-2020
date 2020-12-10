data = open("data_day08.txt").read().splitlines()

ops=[]
for line in data:
    op = line.split()[0]
    val = int(line.split()[1])
    ops.append((op,val))

def accumulator(ops):
    repeat = False
    acc = 0
    x = 0
    ran=set()
    while x<len(ops):
        if x in ran:
            repeat=True
            break
        ran.add(x)
        op = ops[x][0]
        val = ops[x][1]
        if op=='acc':acc += val
        elif op=='jmp':x += val-1
        x += 1
    return acc, repeat

#Part 1
print("Part 1:",accumulator(ops)[0])

#Part 2
swap={'nop':'jmp','jmp':'nop'}
for x,(op,val) in enumerate(ops):
    if op in ['nop','jmp']:
        acc,rep = accumulator(ops[:x]+[(swap[op],val)]+ops[x+1:])
        if not rep: print("Part 2:", acc)