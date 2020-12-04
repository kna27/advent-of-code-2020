i = open("data_day04.txt").read()
reqFields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
p2List = []
with open("data_day04.txt") as file:
    passportFile = [x for x in file.read().split("\n\n") if x]

# Part 1
part1 = 0
for line in passportFile:
    if all(x in line for x in reqFields):
        part1 += 1
        p2List.append(line)
print("Part 1:", part1)

# Part 2, THANK YOU TO REDDIT USER u/thebasementtapes FOR HIS SOLUTION!
def passport():
    txt = open("data_day04.txt").read()
    txt = txt.split("\n\n")
    total_count = 0
    new_list = []
    
    for i in txt:
        i = i.split("\n")
        i = " ".join(i)
        i = i.split(" ")
        new_list.append(i)

    for i in new_list:
        count_per_passport = 0
        for j in i:
            if j[0:3] == "byr":
                if int(j[-4:]) >= 1920 and int(j[-4:]) <= 2002:
                    count_per_passport += 1
            if j[0:3] == "iyr":
                if int(j[-4:]) >= 2010 and int(j[-4:]) <= 2020:
                    count_per_passport += 1            
            if j[0:3] == "eyr":
                if int(j[-4:]) >= 2020 and int(j[-4:]) <= 2030:
                    count_per_passport += 1              
            if j[0:3] == "hgt":
                if j[-2:] == "cm":
                    try:
                        if int(j[-5:-2]) >= 150 and int(j[-5:-2]) <= 193:
                            count_per_passport += 1   
                    except:
                        pass
                if j[-2:] == "in":
                    if int(j[-4:-2]) >= 59 and int(j[-4:-2]) <= 76:
                        count_per_passport += 1   
            if j[0:3] == "hcl":
                try:                
                    if j[-7] == "#":
                        count_per_passport += 1
                except:
                    pass
            if j[0:3] == "ecl":
                if j[-3:] == "amb":
                    count_per_passport += 1
                if j[-3:] == "blu":
                    count_per_passport += 1
                if j[-3:] == "brn":
                    count_per_passport += 1
                if j[-3:] == "gry":
                    count_per_passport += 1
                if j[-3:] == "grn":
                    count_per_passport += 1  
                if j[-3:] == "hzl":
                    count_per_passport += 1    
                if j[-3:] == "oth":
                    count_per_passport += 1                                                                            
            if j[0:3] == "pid":
                if j[4:].isdigit() and len(j[4:]) == 9:
                    count_per_passport += 1                
        if count_per_passport == 7:
            total_count += 1
    return total_count - 1

print("Part 2:", passport())
