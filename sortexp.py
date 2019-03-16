import random
import datetime
time = datetime.datetime.now()

nums = []
maxnum = 10000
for i in range(maxnum):
    n = random.randint(0,maxnum)
    nums.append(n)

print(len(nums))


def selection_sort(l):
    passes = 0
    while passes < len(l):
        count = passes+1
        minimum = passes
        while(count < len(l)):
            if(l[count] < l[minimum]):
                minimum = count
            count += 1
        #swap
        temp = l[passes]
        l[passes] = l[minimum]
        l[minimum] = temp
        passes += 1
    return l

def bubble_sort(l):
    swapped = True
    passes = 1
    while swapped == True:
        swapped = False
        comparison=0
        while comparison < (len(l) - passes):
            if l[comparison] < l[comparison+1]:
                #swap
                temp = l[comparison]
                l[comparison] = l[comparison+1]
                l[comparison+1] = temp
                swapped = True
            comparison += 1
        passes += 1
    return l

num_copy = nums       
time = datetime.datetime.now()
print(time.isoformat())
bubble_sort(num_copy)
time = datetime.datetime.now()
print(time.isoformat())
