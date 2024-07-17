__UPD:__  17.07.2024 добавлена реализация Cython

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
+ короче код через встроенную python функцию MIN(), она лучше оптимизирована и
+ выполняется быстрее на 10-20% чем for, несмотря на то, что массив проходится 2 раза
+ юнит тесты с параметризацией, для большего покрытия граничных значений

/mass_sort_MIN_function.py

/tests/test_mass_sort_MIN.py

### 3. Код функции min() и цикл for реализованный через Cython 
+ 5-кратный прирост производительности по сравнению с реализацией на интерпретаторе python
+ пока что один поток, с использованием gil
+ юнит тесты с параметризацией

для сборки используется 
```
python setup.py build_ext --inplace
```

/lowlevel/setup.py
/lowlevel/mass_sort_cython.pyx

### 4. Сравнение скорости обоих функций
+ С замером времени через функцию time
+ Тестовые данные на 1 и 100 миллионов строк
+ gen_arr_100m.txt https://disk.yandex.ru/d/LAxoJ5pAlJ4Y_Q
+ gen_arr_1m.txt https://disk.yandex.ru/d/Xhn4kg1rwpCW1w

/performance/mass_sort_cython_counter.py
/performance/mass_sort_python_counter.py

### 5. Дополнительный код, который использовался для генерации данных
/generators/gen_arr_python_file.py

/generators/gen_arr_txt_file.py


### 6. Environment:
development IDE Pycharm
For other development environments there may be differences with relative file imports.

It can help for imports in VScode:
```
settings.json

"terminal.integrated.env.windows": { "PYTHONPATH": "${workspaceFolder}" }
```

### 7. How to work with this repository:

Clone repository to your machine. Navigate to the root folder of the project. Create a virtual environment. Run command pip install -r requirements.txt

After, execute to run tests:
```
pytest -s -v
```
