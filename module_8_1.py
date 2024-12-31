def add_everything_up(a, b):
    try:
        # Проверяем, что аргументы не являются None
        if a is None or b is None:
            raise ValueError("Один из аргументов равен None!")

        # Пытаемся выполнить стандартное сложение
        return a + b
    except TypeError:
        # Если возникает ошибка сложения из-за разных типов
        return str(a) + str(b)
    except ValueError as e:
        # Обработка случаев, когда аргумент равен None
        return f"Ошибка: {e}"


# Пример
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up(None, 'строка'))  # Ошибка: Один из аргументов равен None!
print(add_everything_up('123', '456'))  # 123456
