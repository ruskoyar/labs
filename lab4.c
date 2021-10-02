// lab1.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <stdio.h>
#include <locale.h>
#include <stdlib.h>

int main()
{
    setlocale(LC_ALL, "Rus");

    /* Задание 1 */

    int a, b, S, P;
    printf("Нахождение площади и периметра прямоугольника. Введите а и b:");
    scanf_s("%d %d", &a, &b);
    S = a * b;
    P = 2 * (a + b);
    printf("\nS = %d, P = %d\n", S, P);

    /* Задание 2 */

    int d;
    float L, pi;
    pi = 3.14;
    printf("Нахождение длины окружности. Введите диаметр:");
    scanf_s("%d", &d);
    L = pi * d;
    printf("\nL = %f\n", L);

    /* Задание 3 */

    printf("Нахождение среднего арифметического двух чисел. Введите а и b:");
    scanf_s("%d %d", &a, &b);
    printf("\nСреднее арифметическое: %f\n", (float)(a + b) / 2);

    /* Задание 4 */

    printf("Нахождение суммы, разности, произведения и частного квадратов двух чисел. Введите а и b:");
    scanf_s("%d %d", &a, &b);
    a *= a;
    b *= b;
    printf("\nСумма: %d", a + b);
    printf("\nРазность: %d", a - b);
    printf("\nПроизведение: %d", a * b);
    printf("\nЧастное: %f\n", (float)a / (float)b);

    /* Задание 5 */

    printf("Нахождение суммы, разности, произведения и частного модулей двух чисел. Введите а и b:");
    scanf_s("%d %d", &a, &b);
    a = abs(a);
    b = abs(b);
    printf("\nСумма: %d", a + b);
    printf("\nРазность: %d", a - b);
    printf("\nПроизведение: %d", a * b);
    printf("\nЧастное: %f\n", (float)a / (float)b);
}
