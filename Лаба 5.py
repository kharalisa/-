import timeit #модуль для замера времени выполнения кода.
from itertools import product #функция для генерации декартова произведения (всех возможных комбинаций элементов)
### 1 часть
##Алгоритмический метод (без itertools)
def algorithmic_method(K):
    nechet = '1357'  # Нечётные восьмеричные цифры
    result = ['']     # Начинаем с пустой строки
    for _ in range(K):  # Повторяем K раз (по числу разрядов)
        result = [num + d for num in result for d in nechet]  # Добавляем каждую цифру к каждой строке
    return result

##функции питона
def python_method(K):
    return [''.join(p) for p in product('1357', repeat=K)] #генерирует все возможные комбинации длиной K из цифр '1','3','5','7'.
#''.join(p) — объединяет кортеж символов в строку (например, ('1','3') → '13')

K = 3  # Можно изменить разрядность
print("Алгоритмический метод:", algorithmic_method(K)[:10])  # Первые 10 чисел
print("Метод с itertools:", python_method(K)[:10])

print("\nСравнение скорости:")
print("Алгоритмический:", timeit.timeit(lambda: algorithmic_method(K), number=1000)) #замеряет время 1000 выполнений функции.
print("itertools:", timeit.timeit(lambda: python_method(K), number=1000))

### 2 часть
def optimized_method(K, max_sum):
    nechet = '1357'
    numbers = []
    
    for num in product(nechet, repeat=K):  # Перебираем все комбинации
        num_str = ''.join(num)            # Объединяем в строку (например, '135')
        summ = sum(int(d) for d in num_str)  # Считаем сумму цифр
        if summ <= max_sum:           # Если сумма <= ограничению
            numbers.append((num_str, summ))  # Добавляем в список
    
    return numbers

K = 3
max_sum = 12
numberss = optimized_method(K, max_sum)

if numberss:
    optimal = max(numberss, key=lambda x: x[1])  # Находим число с макс. суммой
    print(f"\nОптимальное число: {optimal[0]} (сумма цифр: {optimal[1]})")
else:
    print("Нет подходящих чисел")

