class Data(object):
    def __init__(self, c, x, y, z):
        self.c = c
        self.x = x
        self.y = y
        self.z = z

my_list=[]
with open("glukosa.txt") as f:
    f.readline()
    f.readline()
    for line in f.readlines():
        data=line.split()
        my_list.append(Data(data[0], data[1], data[2], data[3]))

for data in my_list:
    print(data.c, data.x, data.y, data.z, '')