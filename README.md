__UPD:__  17.07.2024 добавлена реализация Cython

__UPD 2:__  19.07.2024 добавлена реализация Nogil

## Задание
#### Напишите функцию, на вход которой приходит массив чисел. Функция возвращает сумму двух минимальных элементов массива.

Например, если дан массив [4, 0, 3, 19, 492, -10, 1], то результатом будет -10, потому что два минимальных числа -10 и 0, а их сумма -10.

Напишите минимум 3 модульных теста на эту функцию.

__HINT:__ учти, что массив может быть пустым, или без цифр, или состоять из 100 млн. элементов, поэтому надо учесть разные граничные условия.


### 1. Основной код через цикл for 
+ нагляднее для других языков программирования
+ сложность O(n), проходим по массиву один раз при поиске
+ добавлены юнит тесты с параметризацией

/mass_sort_FOR_cycle.py

/tests/test_mass_sort_FOR.py

### 2. Код через функцию min() 
+ короче код через встроенную python функцию MIN(), она лучше оптимизирована и выполняется быстрее чем for
+ юнит тесты с параметризацией, для большего покрытия граничных значений

/mass_sort_MIN_function.py

/tests/test_mass_sort_MIN.py

### 3. Код функции min() и цикл for реализованный через Cython с использованием gil
+ 5-кратный прирост производительности по сравнению с реализацией на интерпретаторе python
+ GIL или Python Global Interpreter Lock  — это блокировка, позволяющая только одному потоку управлять интерпретатором
+ Python. Он нужен для корректного управления памятью.
+ юнит тесты с параметризацией

Для сборки используется 
```
python setup.py build_ext --inplace
```

### 4. Код реализованный через Cython с отключением gil
+ 10-кратный прирост производительности по сравнению с реализацией Cython with gil
+ Насколько я понимаю, невозможно как-то декомпозировать основной цикл и разбить на параллельное 
+ выполнение, так как поиск двух минимальных значений требует последовательное сравнение элементов.
+ И прирост скорости появился из-за отказа от ввода данных с помощью списка python, заменив его на массив double.
+ Следующим шагом можно попробовать файл для компиляции на чистом C++
+ юнит тесты с параметризацией

для сборки используется 
```
python setup.py build_ext --inplace
```

/lowlevel/setup.py
/lowlevel/mass_sort_cython.pyx

### 5. Сравнение скорости работы функций
+ С замером времени через функцию time
+ Тестовые данные на 1 и 100 миллионов строк
+ gen_arr_100m.txt https://disk.yandex.ru/d/LAxoJ5pAlJ4Y_Q
+ gen_arr_1m.txt https://disk.yandex.ru/d/Xhn4kg1rwpCW1w

```
100 mil array:
Load file time: 16.605615854263306 

Result Python FOR:   (0.0, 'Time: 10.83065152168274')
Result Python MIN:   (0.0, 'Time: 6.88863205909729')
Result Cython FOR:   (0.0, 'Time: 2.1274640560150146')
Result Cython MIN:   (0.0, 'Time: 1.9042606353759766')
Result Cython Nogil: (0.0, 'Time: 0.19514966011047363')
```

/performance/mass_sort_test_perf.py

### 6. Дополнительный код, который использовался для генерации данных
/generators/gen_arr_python_file.py

/generators/gen_arr_txt_file.py


### 7. Environment:
development IDE Pycharm

python version 3.11

For other development environments there may be differences with relative file imports.

It can help for imports in VScode:
```
settings.json

"terminal.integrated.env.windows": { "PYTHONPATH": "${workspaceFolder}" }
```

### 8. How to work with this repository:

Clone repository to your machine. Navigate to the root folder of the project. Create a virtual environment. Run command pip install -r requirements.txt

After, execute to run tests:
```
pytest -s -v
```
