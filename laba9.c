#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Rus");

    /*  Задание 1 */

    int n;
    printf("С начала суток прошло N секунд (N — целое). Найти количество секунд, прошедших с начала последней минуты. Введите N: ");
    scanf_s("%d", &n);
    printf("Ответ: %d\n", n % 60);

    /* Задание 2 */

    int k;
    printf("Дни недели пронумерованы следующим образом: 0 — воскресенье, 1 — понедельник, 2 — вторник, . . . , 6 — суббота. Дано целое число K, лежащее в диапазоне 1–365. Определить номер дня недели для K-го дня года, если известно, что в этом году 1 января было понедельником. Введите K: ");
    scanf_s("%d", &k);
    printf("Ответ: %d\n", k % 7);

    /* Задание 3 */

    printf("Дни недели пронумерованы следующим образом: 1 — понедельник, 2 — вторник, . . . , 6 — суббота, 7 — воскресенье. Дано целое число K, лежащее в диапазоне 1–365, и целое число N, лежащее в диапазоне 1–7. Определить номер дня недели для K-го дня года, если известно, что в этом году 1 января было днем недели с номером N. Введите K, N: ");
    scanf_s("%d %d", &k, &n);
    printf("Ответ: %d\n", k % 7 + n - 1);

    /* Задание 4 */

    int a, b, c;
    printf("Даны целые положительные числа A, B, C. На прямоугольнике размера A x B размещено максимально возможное количество квадратов со стороной C (без наложений). Найти количество квадратов, размещенных на прямоугольнике, а также площадь незанятой части прямоугольника. Введите A, B, C: ");
    scanf_s("%d %d %d", &a, &b, &c);
    n = a / c * (b / c);
    printf("Кол-во размещенных квадратов: %d\nНезанятая площадь: %d\n", n, a * b - n * c * c);

    /* Задание 5 */

    printf("Дан номер некоторого года (целое положительное число). Определить соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год. Введите год: ");
    scanf_s("%d", &a);
    if (a % 100 == 0) {
        n = a / 100;
    }
    else {
        n = a / 100 + 1;
    }
    printf("Номер столетия: %d", n);
}