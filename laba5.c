#include <stdio.h>
#include <locale.h>
#include <math.h>

int main()
{
    setlocale(LC_ALL, "Rus");

    /* Задание 1 */

    int x1, x2, y1, y2;
    printf("Нахождение расстояния между двумя точками. Введите х1, y1, x2, у2: ");
    scanf_s("%d %d %d %d", &x1, &y1, &x2, &y2);
    printf("Расстояние: %f\n", sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)));

    /* Задание 2 */

    int a, b, c, ac, bc;
    printf("Нахождение длины отрезков АС и ВС и их суммы. Введите А, В, С: ");
    scanf_s("%d %d %d", &a, &b, &c);
    ac = abs(c - a);
    bc = abs(c - b);
    printf("|AC| = %d, |BC| = %d, |AC| + |BC| = %d\n", ac, bc, ac + bc);

    /* Задание 3 */

    printf("Нахождение произведения длин AC и BC (точка С расположена между А и В). Введите А, В, С: ");
    scanf_s("%d %d %d", &a, &b, &c);
    printf("|AC| * |BC| = %d\n", abs(c - a) * abs(c - b));

    /* Задание 4 */

    printf("Нахождение периметра P и площади S прямоугольника, стороны которого параллельны осям координат. Введите координаты двух противоположных вершин x1, y1, x2, y2: ");
    scanf_s("%d %d %d %d", &x1, &y1, &x2, &y2);
    printf("P = %d, S = %d\n", 2 * (abs(x2 - x1) + abs(y2 - y1)), (abs(x2 - x1) * abs(y2 - y1)));

    /* Задание 5 */

    int x3, y3;
    double p;
    printf("Нахождение периметра Р и площади S треугольника. введите координаты вершин x1, y1, x2, y2, x3, y3: ");
    scanf_s("%d %d %d %d %d %d", &x1, &y1, &x2, &y2, &x3, &y3);
    double A = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
    double B = sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2));
    double C = sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2));
    p = (A+B+C) / 2;
    printf("P = %f, S = %f", A + B + C, sqrt(p * (p - A) * (p - B) * (p - C)));
}