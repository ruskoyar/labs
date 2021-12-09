def ser(a):
    b=[]
    c=[]
    cur=a[0]
    n=1
    for i in range(1,len(a)):
        if cur!=a[i]:
            c.append(n)
            b.append(cur)
            n=1
            cur=a[i]
        else:
            n+=1
        if i==len(a)-1:
            c.append(n)
            b.append(cur)
    return [b,c]

def perm3(a):
    b=[]
    for i in range(len(a)-2):
        for ii in range(i+1,len(a)-1):
            for iii in range(ii+1,len(a)):
                b.append([a[i],a[ii],a[iii]])
    return b

def dist(x1,x2,y1,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

#Задание 1

print("Дан целочисленный массив A размера N. Назовем серией группу подряд идущих одинаковых элементов, а длиной серии — количество этих элементов (длина серии может быть равна 1). Сформировать два новых целочисленных массива B и C одинакового размера, записав в массив B длины всех серий исходного массива, а в массив C — значения элементов, образующих эти серии")
print("Введите N:")
n=int(input())
print("Введите значения элементов массива:")
a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
s=ser(a)
b=s[0]
c=s[1]
print("Результат: b =",b,", c =",c)

#Задание 2

print("Дано целое число L (> 0) и целочисленный массив размера N. Заменить каждую серию массива, длина которой больше L, на один элемент с нулевым значением")
print("Введите L:")
l=int(input())
print("Введите N:")
n=int(input())
print("Введите значения элементов массива:")
a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
s=ser(a)
b=s[0]
c=s[1]
d=[]
for i in range(len(c)):
    if c[i]>l:
        d.append(0)
    else:
        for k in range(c[i]):
            d.append(b[i])
print("Результат:", d)

#Задание 3

print("Дано целое число K (> 0) и целочисленный массив размера N. Поменять местами последнюю серию массива и его серию с номером K ")
print("Введите K:")
k=int(input())
print("Введите N:")
n=int(input())
print("Введите значения элементов массива:")
a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
s=ser(a)
b=s[0]
c=s[1]
d=[]
for i in range(len(c)):
    if i==len(c)-1:
        for m in range(c[k-1]):
            d.append(b[k-1])
        break
    if i==k-1:
        for m in range(c[len(c)-1]):
            d.append(b[len(c)-1])
    else:
        for m in range(c[i]):
            d.append(b[i])
print("Результат:",d)

#Задание 4

print("Дано множество A из N точек (точки заданы своими координатами x, y). Среди всех точек этого множества, лежащих во второй четверти, найти точку, наиболее удаленную от начала координат. Если таких точек нет, то вывести точку с нулевыми координатами")
print("Введите N:")
n=int(input())
print("Введите координаты точек:")
a=[]
for i in range(n):
    t=input().split()
    a.append([int(t[0]),int(t[1])])
c=[0,0]
ms=0
for i in range(len(a)):
    x=a[i][0]
    y=a[i][1]
    if x<=0 and y>=0:
        s=(x**2+y**2)**0.5
        if ms<s:
            ms=s
            c=[x,y]
print("Результат:",c)

#Задание 5

print("Дано множество A из N точек (N > 2, точки заданы своими координатами x, y). Найти наибольший периметр треугольника, вершины которого принадлежат различным точкам множества A, и сами эти точки (точки выводятся в том же порядке, в котором они перечислены при задании множества A).")
print("Введите N:")
n=int(input())
print("Введите координаты точек:")
a=[]
for i in range(n):
    t=input().split()
    a.append([int(t[0]),int(t[1])])
b=perm3(a)
mp=0
for i in range(len(b)):
    p=0
    x1=b[i][0][0]
    x2=b[i][1][0]
    x3=b[i][2][0]
    y1=b[i][0][1]
    y2=b[i][1][1]
    y3=b[i][2][1]
    p=dist(x1,x2,y1,y2)+dist(x2,x3,y2,y3)+dist(x1,x3,y1,y3)
    if mp<p:
        c=b[i]
        mp=p
print("Результат: p =",mp,", координаты точек -",c)
