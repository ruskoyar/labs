#Задание 1

print("Дан символьный файл, содержащий по крайней мере один символ пробела. Удалить все его элементы, расположенные перед первым символом пробела, включая и этот пробел.")
input()
f=open('file1.txt')
text=f.read()
text=text[text.find(' ')+1:]
f=open('file1.txt','w')
f.write(text)
f.close()

#Задание 2

print("Дано имя файла и целые положительные числа N и K. Создать текстовый файл с указанным именем и записать в него N строк, каждая из которых состоит из K символов «*» (звездочка).")
print("Введите имя файла:")
name=input()
print("Введите N:")
n=int(input())
print("Введите K:")
k=int(input())
f=open(name+'.txt','w')
for i in range(n):
    for ii in range(k):
        f.write('*')
    f.write('\n')
f.close()

#Задание 3

print("Даны два текстовых файла. Добавить в начало первого файла содержимое второго файла")
input()
f1=open("file3_1.txt")
text1=f1.read()
f1.close()
f2=open("file3_2.txt")
text2=f2.read()
f2.close()
text=text2+text1
f1=open("file3_1.txt",'w')
f1.write(text)
f1.close()

#Задание 4

print("Дан текстовый файл. Заменить в нем все подряд идущие пробелы на один пробел.")
input()
f=open('file4.txt')
text=f.read()
text=' '.join(text.split())
f.close()
f=open('file4.txt','w')
f.write(text)
f.close()

#Задание 5

print("Дан текстовый файл. Найти количество абзацев в тексте, если первая строка каждого абзаца начинается с 5 пробелов («красная строка»). Пустые строки между абзацами не учитывать.")
input()
f=open('file5.txt')
text=f.read()
print("Результат:", text.count('     '))
f.close()
