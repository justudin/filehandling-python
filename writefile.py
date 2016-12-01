lines = ["first line\n", "second line\n", "third line\n"]
f = open('t1.txt', 'w')
f.writelines(lines)
f.close()