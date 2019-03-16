import random
import datetime
time = datetime.datetime.now()

def rand1(minimum, maximum, n):
    randlist = []
    for i in range(n-1):
        found = True
        r = random.randint(minimum,maximum)
        while found:
            j = 0
            found = False
            while found == False and j < len(randlist):           
                if randlist[j] == r:
                    found = True
                j = j+1
            if found:
                r = random.randint(minimum,maximum)              
        randlist.append(r)
    return randlist

def rand2(minimum, maximum, n):
    used = []
    randlist = []
    for i in range(maximum-minimum):
        used.append(False)

    for j in range(n-1):
        r = random.randint(0, maximum-minimum-1)
        while used[r]:
            r = random.randint(0, maximum-minimum-1)
        used[r] = True
        randlist.append(r + minimum)
    return randlist


def rand3(minimum, maximum, n):
    randlist = []
    options = []
    for i in range(maximum-minimum):
        options.append(i+minimum)

    for j in range(n-1):
        r = random.randint(j, maximum-minimum-1)
        randlist.append(options[r])
        options[r] = options[j]

    return randlist

      
time1 = datetime.datetime.now()
#print(time1.isoformat())
rand1(0,10000,9000)
time2 = datetime.datetime.now()
#print(time2.isoformat())
print(time2-time1)






