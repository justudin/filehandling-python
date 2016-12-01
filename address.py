addressbook = []
with open('address.txt', 'r') as f:
    for line in f:
        name, city = line[:17], line[17:]
        last, first = name.split(',')
        addressbook.append((first, last, city))

print(addressbook[0])
print(addressbook[0][0])
print(addressbook[0][1])
print(addressbook[0][2])
