#Задание 1

print("Дан массив размера N и целые числа K и L (1 ≤ K ≤ L ≤ N). Найти среднее арифметическое элементов массива с номерами от K до L включительно.")
print("Введите N, K, L: ")
n=int(input())
k=int(input())-1
l=int(input())
print("Введите значения элементов массива:")
a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
s=0
for i in range(k,l):
    s+=a[i]
s/=l-k
print("Результат:", s)

#Задание 2

print("Дан целочисленный массив размера N, не содержащий одинаковых чисел. Проверить, образуют ли его элементы арифметическую прогрессию. Если образуют, то вывести разность прогрессии, если нет — вывести 0.")
print("Введите N:")
n=int(input())
print("Введите значения элементов массива:")
a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
d=a[1]-a[0]
for i in range(1,len(a)):
    if a[i]-a[i-1]!=d:
        d=0
        break
print("Результат:", d)

#Задание 3

print("Дан массив A размера N. Найти минимальный элемент из его элементов с четными номерами: A2, A4, A6...")
print("Введите N:")
n=int(input())
print("Введите значения элементов массива:")
a=input().split()
m=int(a[1])
for i in range(len(a)):
    a[i]=int(a[i])
for i in range(1,len(a),2):
    m=min(m,a[i])
print("Результат:", m)

#Задание 4

print("Дан массив размера N. Найти номер его последнего локального максимума (локальный максимум — это элемент, который больше любого из своих соседей).")
print("Введите N:")
n=int(input())
print("Введите значения элементов массива:")
a=input().split()
m=-1
for i in range(len(a)):
    a[i]=int(a[i])
for i in range(len(a)):
    if (i==0 and a[0]>a[1]) or (i==len(a)-1 and a[len(a)-1]>a[len(a)-2]):
        m=i+1
    elif a[i]>a[i-1]and a[i]>a[i+1]:
        m=i+1
if m==-1:
    print("Локальных максимумов не существует.")
else:
    print("Результат:", m)

#Задание 5

print("Дан целочисленный массив размера N, содержащий ровно два одинаковых элемента. Найти номера одинаковых элементов и вывести эти номера в порядке возрастания")
print("Введите N:")
n=int(input())
print("Введите значения элементов массива:")
a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
for i in range(len(a)-1):
    f=False
    for k in range(i+1,len(a)):
        if a[i]==a[k]:
            f=True
            print(i+1,k+1)
            break
    if f:
        break

        
