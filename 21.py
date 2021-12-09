#Задание 1

print("Дана квадратная матрица A порядка M (M — нечетное число). Начиная с элемента A1,1 и перемещаясь против часовой стрелки, вывести все ее элементы по спирали: первый столбец, последняя строка, последний столбец в обратном порядке, первая строка в обратном порядке, оставшиеся элементы второго столбца и т. д.; последним выводится центральный элемент матрицы.")
print("Введите M:")
m=int(input())
print("Введите значения элементов матрицы (построчно):")
a=[]
for i in range(m):
    a.append([int(x) for x in input().split()])
i=0
k=0
n=0
while n<=m//2:
    if k==m//2+1 and i==m//2+1:
        print(a[k][i])
        break
    while k<m-n:
        print(a[k][i])
        k+=1
    k-=1
    i+=1
    while i<m-n:
        print(a[k][i])
        i+=1
    i-=1
    while k>n:
        k-=1
        print(a[k][i])
    while i>n+1:
        i-=1
        print(a[k][i])
    k+=1
    n+=1
        
#Задание 2

print("Дана матрица размера M × N и целое число K (1 ≤ K ≤ M). Найти сумму и произведение элементов K-й строки данной матрицы.")
print("Введите M:")
m=int(input())
print("Введите N:")
n=int(input())
print("Введите K:")
k=int(input())-1
print("Введите значения элементов матрицы (построчно):")
a=[]
for i in range(m):
    a.append([int(x) for x in input().split()])
s=0
p=1
for i in range(n):
    s+=a[k][i]
    p*=a[k][i]
print("Сумма =", s, ", произведение =", p)

#Задание 3

print("Дана матрица размера M × N. Найти номер ее столбца с наименьшим произведением элементов и вывести данный номер, а также значение наименьшего произведения.")
print("Введите M:")
m=int(input())
print("Введите N:")
n=int(input())
print("Введите значения элементов матрицы (построчно):")
a=[]
for i in range(m):
    a.append([int(x) for x in input().split()])
mp=1000**10
for i in range(n):
    p=1
    for k in range(m):
        p*=a[k][i]
    if p<mp:
        mp=p
        s=i+1
print("Номер столбца -", s, ", произведение =", mp)

#Задание 4

print("Дана матрица размера M × N. В каждом ее столбце найти количество элементов, больших среднего арифметического всех элементов этого столбца")
print("Введите M:")
m=int(input())
print("Введите N:")
n=int(input())
print("Введите значения элементов матрицы (построчно):")
a=[]
for i in range(m):
    a.append([int(x) for x in input().split()])
s=[]
for i in range(n):
    c=0
    for k in range(m):
        c+=a[k][i]
    s.append(c/m)
p=[]
for i in range(n):
    c=0
    for k in range(m):
        if a[k][i]>s[i]:
            c+=1
    p.append(c)
for i in range(len(p)):
    print(str(i+1)+"-й столбец -", p[i])

#Задание 5

print("Дана целочисленная матрица размера M × N. Найти номер первого из ее столбцов, содержащих только нечетные числа. Если таких столбцов нет, то вывести 0.")
print("Введите M:")
m=int(input())
print("Введите N:")
n=int(input())
print("Введите значения элементов матрицы (построчно):")
a=[]
for i in range(m):
    a.append([int(x) for x in input().split()])
c=0
for i in range(n):
    stop=True
    for k in range(m):
        if a[k][i]%2==0:
            stop=False
    if stop:
        c=i+1
        break
print("Результат:", c)
