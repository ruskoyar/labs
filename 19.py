#Задание 1

print("Дан целочисленный массив размера N. Удалить из массива все соседние одинаковые элементы, оставив их первые вхождения.")
print("Введите N:")
n=int(input())
print("Введите значения элементов массива:")
a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
b=[a[0]]
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        b.append(a[i+1])
a=b
print("Результат:", a)
        
#Задание 2

print("Дан целочисленный массив размера N. Удалить из массива все элементы, встречающиеся ровно два раза, и вывести размер полученного массива и его содержимое.")
print("Введите N:")
n=int(input())
print("Введите значения элементов массива:")
a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
i=0
l=len(a)
while i<l:
    if a.count(a[i])==2:
        a.pop(a.index(a.pop(i)))
    i+=1
    l=len(a)
print("Результат:", a,". Размер =", len(a))

#Задание 3

print("Дан массив размера N. Вставить элемент с нулевым значением перед минимальным и после максимального элемента массива.")
print("Введите N:")
n=int(input())
print("Введите значения элементов массива:")
a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
mn=a[0]
mx=a[0]
mni=0
mxi=0
for i in range(len(a)):
    if mx<a[i]:
        mx=a[i]
        mxi=i
    if mn>a[i]:
        mn=a[i]
        mni=i
if mxi<mni:
    a.insert(mni,0)
    a.insert(mxi+1,0)
else:
    a.insert(mxi+1,0)
    a.insert(mni,0)
print("Результат:", a)

#Задание 4

print("Дан массив размера N. После каждого отрицательного элемента массива вставить элемент с нулевым значением.")
print("Введите N:")
n=int(input())
print("Введите значения элементов массива:")
a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
i=0
l=len(a)
while i<l:
    if a[i]<0:
        a.insert(i+1,0)
    i+=1
    l=len(a)
print("Результат:", a)

#Задание 5

print("Дан массив размера N. Перед каждым положительным элементом массива вставить элемент с нулевым значением.")
print("Введите N:")
n=int(input())
print("Введите значения элементов массива:")
a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
i=0
l=len(a)
while i<l:
    if a[i]>0:
        a.insert(i,0)
        i+=1
    i+=1
    l=len(a)
print("Результат:", a)
    

