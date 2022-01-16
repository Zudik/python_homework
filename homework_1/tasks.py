from typing import List

# Написать функцию, которая позволяет пользователю вводить числа, буквы и слова с клавиатуры.
# Все элементы сохраняются в список до тех пор, пока не будет введена пустая строка. 
# Функция возвращает итоговый список.

def input_list() -> List:
    final_list = []
    input_data = input()
    while input_data:
        final_list.append(input_data)
        input_data = input()
    return final_list

# Написать функцию, которая принимает 1 аргумент n.
# n - целое число от 1 до 12. 
# В результате работы функция возвращает время года к которому принадлежит месяц n.

def season(n: int) -> str:  
    assert n < 13 and n >= 0  
    return {
        1: 'Весна',
        2: 'Лето',
        3: 'Осень',
    }.get(n//3, 'Зима')

# Написать функцию, которая принимает 1 аргумент n - целое число и выводит первые n чисел Фибоначчи.

def fib(n: int) -> List:
    assert n >= 0
    fib_list = [0,1]
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return fib_list
    for i in range(1, n-1):
        fib_list.append(fib_list[i] + fib_list[i-1])
    return fib_list

# Пользователь вводит список произвольной длины. 
# Вывести количество одинаковых элементов. 
# Для ввода списка использовать функцию из 1-го задания.

def number_identical_elements() -> str:
    input_list_p = input_list()
    dict_output = {word:input_list_p.count(word) for word in input_list_p}
    print('Элемент\t|\tЧастота')
    for i in dict_output:
        print(i, "\t|\t", dict_output[i])
    return dict_output

# Написать функцию, которая вычисляет среднее арифмитическое чисел в последовательности.
# Последовательность чисел передаётся через аргумент.

def mean_input(numbers: List) -> float:
    if len(numbers) == 0:
        return 0
    return sum(numbers)/len(numbers)

# Написать функцию, которая принимает 1 аргумент - целое число и возвращает True,
# если число простое и False в обратном случае

def is_prime(n: int) -> bool:
    m = 2
    while n % m != 0:
        m += 1
    return m == n

# Пользователь вводит текст. Вывести самое длинное слово и наиболее часто встречаемое слово

def longest_frequently_used():
    s = input()
    words = s.split(' ')
    sorted_words_len = sorted(words, key=len)
    sorted_words_count = sorted(words, key=lambda x: words.count(x))
    return sorted_words_len[-1], sorted_words_count[-1]
