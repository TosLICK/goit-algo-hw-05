def caching_fibonacci():
    cache= {}
    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache: # якщо n-те число вже у кеші, то одразу його повертаємо
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # використовуємо рекурсію, щоб визначити n-те число як...
        return cache[n] # ... ф-ція fibonacci від (n-1)-того числа + fibonacci від (n-2)-того числа і повертаємо
    return fibonacci # відбувається замикання

# fib = caching_fibonacci()

# print(fib(10))
# print(fib(15))