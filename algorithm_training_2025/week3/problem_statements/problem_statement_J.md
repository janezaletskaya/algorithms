## J. Упаковка и распаковка\*

**Ограничение времени:** 2 секунды  
**Ограничение памяти:** 1024 МБ  
**Ввод:** стандартный ввод  
**Вывод:** стандартный вывод  

---

Это задача с двойным запуском.  
Ваше решение будет запущено два раза.

Вам необходимо реализовать алгоритм сжатия и распаковки, который будет сжимать тексты на английском языке, записанные только маленькими английскими буквами, без пробелов, знаков препинания и вообще каких-либо символов, отличных от маленьких английских букв.  
Эти тексты являются художественными произведениями (естественным текстом).

Решение будет считаться верным, если в результате упаковки и распаковки получается исходная строка. Также необходимо, чтобы количество байт в сжатой последовательности было как минимум вдвое меньше, чем количество символов в исходной строке.

### Протокол взаимодействия

#### Первый запуск

На вход программе в первой строке передаётся слово `"pack"`.

Во второй строке передаётся строка `s` из маленьких английских букв.  
Длина строки для всех тестов находится в пределах от 100 000 до 200 000 букв.

Ваше решение должно вывести количество чисел (байт) `N` в сжатой вами последовательности.  
Во второй строке выведите `N` чисел от 0 до 255 включительно в десятичной системе счисления, разделяя их пробелами. В конце обязательно сбросьте буфер вывода и выведите перевод строки.

Количество байт не должно превышать половины от количества символов входной строки.

#### Второй запуск

На вход программе в первой строке передаётся слово `"unpack"`.

Затем в программу передаётся вывод первого запуска: количество байт, а затем числа от 0 до 255 через пробел — последовательность символов. Необходимо вывести распакованную строку.  
В конце обязательно сбросьте буфер вывода и выведите перевод строки.