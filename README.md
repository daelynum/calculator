# calculator
calculator using FastApi framework 


Как мне кажется игнорировать пробелы (как того требует задание) не совсем корректно.

В примере тестового задания (* 5 + - 4 → ошибка ) указано, что должна быть ошибка.
Однако если игнорировать пробелы, то результат будет равен 1 (5 + -4 = 1)

Касательно решения задания:
Пробовал регулярное выражение, которое сортирует строку, но такое решение мне показалось нереальным (если вставлять везде пробелы, то не ясно как использовать отрицательное число, если схлопывать все пробелы, то вместо оператора может получиться отрицательное или положительное число), так же пробовал как в подсказке использовать Польскую нотацию, но для меня это оказалось тяжело, в итоге решил генерировать список элементов из строки, используя каждое число или оператор для получения финального результата.
