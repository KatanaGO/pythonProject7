def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += item  # Пытаемся добавить элемент к результату
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1  # Увеличиваем счётчик некорректных данных

    return result, incorrect_data


def calculate_average(numbers):
    try:
        # Проверяем, является ли numbers коллекцией (например, списком)
        if not hasattr(numbers, '__iter__'):
            raise TypeError('В numbers записан некорректный тип данных')

        total_sum, incorrect_data = personal_sum(numbers)

        try:
            average = total_sum / (len(numbers) - incorrect_data)  # Считаем среднее арифметическое
            return average
        except ZeroDivisionError:
            return 0  # Если делим на 0, возвращаем 0

    except TypeError as e:
        print(e)
        return None


# Примеры вызова функций
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строка
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только числа
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё работает корректно
