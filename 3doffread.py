f=open("3d.off")
print(f)
my_list=[]

a=f.readline().strip()
print(a)

b=[]
b=f.readline().strip()
print(b[0],b[1],b[2])

verts=[]
f2=open("3dout.txt", 'w')
for vertex_i in range (int(b[0])):
    verts.append([float(s) for s in f.readline().strip().split(' ')])
    print(verts[vertex_i])
    data1=str(verts[vertex_i][0])
    data2=str(verts[vertex_i][1])
    data3=str(verts[vertex_i][2])
    f2.write(data1+','+data2+','+data3+'\n')

#print verts