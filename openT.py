print("1")
f = open('t.txt')
line = f.readline()
while line:
    print(line)
    line = f.readline()

print("2")
f = open('t.txt')
for line in f.readlines():
    print(line),

print("3")
f = open('t.txt')
for line in f.xreadlines():
    print(line),

print("4")
f = open('t.txt')
for line in f:
    print(line),