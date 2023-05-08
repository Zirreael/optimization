# Алгоритм Нелдера-Мида
Метод Нелдера — Мида — метод оптимизации (поиска минимума) функции от нескольких переменных. Простой и в тоже время эффективный метод, позволяющий оптимизировать функции без использования градиентов. Метод надежен и, как правило, показывает хорошие результаты, хотя и отсутствует теория сходимости.
Алгоритм заключается в формировании симплекса (simplex) и последующего его деформирования в направлении минимума, посредством трех операций:

1) Отражение (reflection);
2) Растяжение (expansion);
3) Сжатие (contract);

Симплекс представляет из себя геометрическую фигуру, являющуюся n — мерным обобщением треугольника. Для одномерного пространства — это отрезок, для двумерного — треугольник. Таким образом n — мерный симплекс имеет n + 1 вершину.