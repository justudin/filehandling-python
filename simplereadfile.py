f = open('data.txt')
d = f.readlines()

# print as an array
print([x.split() for x in d])

# print specific lines only
print(d[0])
print(d[1])

# or like this
lines = [1, 2]
i=0
for line in f:
    print(i)
    if i in lines:
        print(i)
    i+=1
