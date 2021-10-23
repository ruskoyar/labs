#include <stdio.h>
#include <locale.h>
#include <math.h>

int main()
{
    setlocale(LC_ALL, "Rus");

    /* Задание 1 */

    int a, b, c;
    printf("Перенос значения из А в В и из В в А. Введите А и В: ");
    scanf_s("%d %d", &a, &b);
    c = a;
    a = b;
    b = c;
    printf("A = %d, B = %d\n", a, b);

    /* Задание 2 */

    int d;
    printf("Перенос значений из A в B, из B в C, из C в A. Введите А, В, С: ");
    scanf_s("%d %d %d", &a, &b, &c);
    d = c;
    c = b;
    b = a;
    a = d;
    printf("A = %d, B = %d, C = %d\n", a, b, c);

    /* Задание 3 */

    printf("Перенос значений из A в С, из С в В, из В в A. Введите А, В, С: ");
    scanf_s("%d %d %d", &a, &b, &c);
    d = a;
    a = b;
    b = c;
    c = d;
    printf("A = %d, B = %d, C = %d\n", a, b, c);

    /* Задание 4 */

    double x, y;
    printf("Нахождение значения функции y = 3x^6 - 6x^2 - 7 . Введите х: ");
    scanf_s("%lf", &x);
    y = 3 * pow(x, 6) - 6 * pow(x, 2) - 7;
    printf("y = %lf\n", y);

    /* Задание 5 */

    printf("Нахождение значения функции y = 4(x-3)^6 - 7(x-3)^3 + 2. Введите х: ");
    scanf_s("%lf", &x);
    y = 4 * pow(x - 3, 6) - 7 * pow(x - 3, 3) + 2;
    printf("y = %lf\n", y);

    /* Задание 6 */

    double A, B, C;
    printf("Вычисление A^8 c использованием вспомогательной переменной и трех операций умножения. Введите А: ");
    scanf_s("%lf", &A);
    B = A * A;
    B = B * B;
    B = B * B;
    printf("A^6 = %lf\n", B);

    /* Задание 7 */

    printf("Вычисление A^15 c использованием двух вспомогательный переменный и пяти операций умножения. Введите А: ");
    scanf_s("%lf", &A);
    B = A * A;
    B = B * B * A;
    C = B * B * B;
    printf("A^15 = %lf\n", C);

    return 0;
}