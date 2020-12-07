from collections import defaultdict
import re
#Thanks to u/prutsw3rk for his help

f = [line.rstrip() for line in open("data_day07.txt")]

bags_that_include = defaultdict(list)
contents = {}
for line in f:
    parent = re.search(r'(.*) bags contain', line).group(1)
    for bag in re.findall(r'\d+ (.*?) bag', line):
        bags_that_include[bag].append(parent)
    contents[parent] = re.findall(r'(\d+) (.*?) bag', line)

#Part 1
def collectbags(bag):
    t = set(bag)
    for b in bag:
        t |= collectbags(bags_that_include[b])
    return t
print("Part 1:", len(collectbags(bags_that_include['shiny gold'])))

#Part 2
def unpack(bag):
    t = 0
    for n, m in contents[bag]:
        t += int(n)*unpack(m)
    return 1+t
print("Part 2:", unpack('shiny gold')-1)