class Studentiki:
    id=0
    fio=''
    id_project=0
    clas=''
    score=0

students=[]
f=open('students.csv')
j=0

for i in f:
    s=i.split(',')
    if (s[3][:-1])== '10':
        b=Studentiki()
        b.fio=s[1]
        b.score==int(s[4])
        students.append(b)
for i in range(len(students)):
    j=i
    print(students[j].fio)
    t=students[i]
    while j>0 and students[j-1].score<t.score:
        students[j]=students[j-1]
        j-=1
    students[j]=t


print(len(students))

print(students[0].fio)
print(students[1].fio)
print(students[2].fio)
