import datetime
i = datetime.datetime.now()

f= open("country-list.csv","r")
print(f)
countries_list = []
countries_dict = {}
for line in f:
    #print(line)
    l = line.split(',')
    countries_list.append(l[0])
    countries_dict[l[0]] = int(l[1])
f.close()
print(len(countries_list))

print(i.isoformat())
passes = 0
while passes < len(countries_dict):
    count = passes+1
    minimum = passes
    while(count < len(countries_dict)):
        if(countries_dict[countries_list[count]] < countries_dict[countries_list[minimum]]):
            minimum = count
        count += 1
    #swap
    temp = countries_list[passes]
    countries_list[passes] = countries_list[minimum]
    countries_list[minimum] = temp
    passes += 1
    
print(i.isoformat())

print(countries_list)


    
    

              
