﻿## Задание
#### Напишите функцию, на вход которой приходит массив чисел. Функция возвращает сумму двух минимальных элементов массива.

Например, если дан массив [4, 0, 3, 19, 492, -10, 1], то результатом будет -10, потому что два минимальных числа -10 и 0, а их сумма -10.

Напишите минимум 3 модульных теста на эту функцию.

__HINT:__ учти, что массив может быть пустым, или без цифр, или состоять из 100 млн. элементов, поэтому надо учесть разные граничные условия.


### 1. Основной код через цикл for 
+ нагляднее для других языков программирования
+ сложность O(n), проходим по массиву один раз при поиске
+ юнит тесты в отдельном файле

/mass_sort_FOR_cycle.py

### 2. Код через функцию min() 
+ короче код через встроенную функцию python
+ быстрее на 10-20% чем for, несмотря на то, что массив проходится 2 раза
+ юнит тесты с параметризацией, для большего покрытия граничных значений

/mass_sort_MIN_function.py

### 3. Сравнение скорости обоих функций
+ С замером времени через perf_counter
+ Тестовые данные на 1 и 100 миллионов строк
+ gen_arr_100m.txt https://disk.yandex.ru/d/LAxoJ5pAlJ4Y_Q
+ gen_arr_1m.txt https://disk.yandex.ru/d/Xhn4kg1rwpCW1w
/performance/mass_sort_perf_counter.py

### 4. Дополнительный код, который использовался для генерации данных
/generators/gen_arr_python_file.py

/generators/gen_arr_txt_file.py


### 5. How to work with this repository:

Clone repository to your machine. Navigate to the root folder of the project. Create a virtual environment. Run command pip install -r requirements.txt

After, execute __"pytest -s -v"__ to run test.

