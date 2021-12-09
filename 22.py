#Задание 1

print("Дана матрица размера M × N. Преобразовать матрицу, поменяв местами минимальный и максимальный элемент в каждой строке.")
print("Введите M:")
m=int(input())
print("Введите N:")
n=int(input())
print("Введите значения элементов матрицы (построчно):")
a=[]
for i in range(m):
    a.append([int(x) for x in input().split()])
for i in range(m):
    mn=a[0][0]
    mx=mn
    mnk=0
    mxk=0
    for k in range(len(a[i])):
        if mn>a[i][k]:
            mn=a[i][k]
            mnk=k
        if mx<a[i][k]:
            mx=a[i][k]
            mxk=k
    c=a[i][mnk]
    a[i][mnk]=a[i][mxk]
    a[i][mxk]=c
for i in range(len(a)):
    print(a[i])

#Задание 2

print("Дана матрица размера M × N. Поменять местами столбцы, содержащие минимальный и максимальный элементы матрицы.")
print("Введите M:")
m=int(input())
print("Введите N:")
n=int(input())
print("Введите значения элементов матрицы (построчно):")
a=[]
for i in range(m):
    a.append([int(x) for x in input().split()])
mn=a[0][0]
mx=mn
mxk=0
mnk=0
for i in range(len(a)):
    for k in range(len(a[i])):
        if mn>a[i][k]:
            mnk=k
            mn=a[i][k]
        if mx<a[i][k]:
            mx=a[i][k]
            mxk=k
print(mnk,mxk,mn,mx)
for i in range(len(a)):
    c=a[i][mnk]
    a[i][mnk]=a[i][mxk]
    a[i][mxk]=c
for i in range(len(a)):
    print(a[i])

#Задание 3

print("Дана матрица размера M × N (M и N — четные числа). Поменять местами левую верхнюю и правую нижнюю четверти матрицы")
print("Введите M:")
m=int(input())
print("Введите N:")
n=int(input())
print("Введите значения элементов матрицы (построчно):")
a=[]
for i in range(m):
    a.append([int(x) for x in input().split()])
for i in range(len(a)):
    for k in range(len(a[i])):
        if k<len(a[i])-i-1:
            c=a[i][k]
            a[i][k]=a[len(a[i])-i-1][len(a)-k-1]
            a[len(a[i])-i-1][len(a)-k-1]=c
for i in range(len(a)):
    print(a[i])

#Задание 4

print("Дана матрица размера M × N. Упорядочить ее строки так, чтобы их первые элементы образовывали возрастающую последовательность.")
print("Введите M:")
m=int(input())
print("Введите N:")
n=int(input())
print("Введите значения элементов матрицы (построчно):")
a=[]
for i in range(m):
    a.append([int(x) for x in input().split()])
for i in range(len(a)):
    for k in range(len(a)-1):
        if a[k][0]>a[k+1][0]:
            c=a[k]
            a[k]=a[k+1]
            a[k+1]=c
for i in range(len(a)):
    print(a[i])

#Задание 5

print("Дана квадратная матрица A порядка M. Найти сумму элементов каждой ее диагонали, параллельной главной (начиная с одноэлементной диагонали).")
print("Введите M:")
m=int(input())
print("Введите N:")
n=int(input())
print("Введите значения элементов матрицы (построчно):")
a=[]
for i in range(m):
    a.append([int(x) for x in input().split()])
c=[]
for n in range(len(a[0])-1,0,-1):
    i=0
    k=n
    s=0
    while i<len(a) and k<len(a[i]):
        s+=a[i][k]
        i+=1
        k+=1
    c.append(s)
for n in range(1,len(a)):
    i=n
    k=0
    s=0
    while i<len(a) and k<len(a[i]):
        s+=a[i][k]
        i+=1
        k+=1
    c.append(s)
print(c)
