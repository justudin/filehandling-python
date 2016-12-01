columndHeader = ['name', 'email', 'password']
dbList = []

def main():
    global  dbList
    f = open("datacomma.txt", "r")
    for line in f:
        entryDict = {}
        tempList = line.split(',')
        for i, header in enumerate(columndHeader):
            entryDict[header] = tempList[i].strip()
        dbList.append(entryDict)
    f.close()

main()
print(dbList[0])