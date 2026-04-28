def calculate() -> float:
    """Безопасное деление и вывод первого элемента списка."""
    a = 10
    b = 1
    if b == 0:
        raise ValueError("Деление на ноль не допускается")
    result = a / b

    numbers = [1, 2, 3]
    if numbers:                     # проверка на непустой список
        print(numbers[0])
    else:
        print("Список пуст")

    return result

# Удалена функция do_everything — она не нужна

print("Результат:", calculate())