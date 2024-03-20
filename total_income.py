from re import findall
from typing import Callable


def generator_numbers(text: str):
    pattern = r"\d+\.\d+" # шаблон, що відповідає числу float
    match = findall(pattern, text) # знаходимо усі входження дійсних чисел у тексті і створюємо з них список
    for num in match:
        yield float(num) # повертаємо усі дійсні числа як генератор

def sum_profit(text: str, func: Callable) -> float:
    result = 0
    for num in func(text): # перебираємо усі числа з генератора 
        result += num
    return result

# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід," \
#        "доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# total_income = sum_profit(text, generator_numbers)
# print(f"Загальний дохід: {total_income}")