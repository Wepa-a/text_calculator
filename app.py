numbers = {
    "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9,
    "десять": 10, "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,
    "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19, "двадцать": 20,
    "тридцать": 30, "сорок": 40, "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70, "восемьдесят": 80, "девяносто": 90
}

operations = {
    "плюс": "+",
    "минус": "-",
    "умножить": "*",
    "разделить": "/"
}

def text_to_number(text):
    """Преобразование числового текста в целое число."""
    parts = text.split()
    number = 0
    for part in parts:
        if part in numbers:
            number += numbers[part]
    return number


def number_to_text(number):
    """Преобразование числа в текстовое представление."""
    if number in numbers.values():
        return list(numbers.keys())[list(numbers.values()).index(number)]
    tens = (number // 10) * 10
    units = number % 10
    text = ""
    if tens:
        text += list(numbers.keys())[list(numbers.values()).index(tens)]
    if units:
        if text:
            text += " "
        text += list(numbers.keys())[list(numbers.values()).index(units)]
    return text


def calc(expression: str):
    """Вычисление выражения с числовыми и текстовыми значениями."""
    tokens = expression.split()

    # Первая часть числа
    num1_tokens = []
    while tokens and (tokens[0] in numbers):
        num1_tokens.append(tokens.pop(0))

    num1 = text_to_number(" ".join(num1_tokens))

    if not tokens:
        raise ValueError("Неверный формат выражения. Ожидается операция.")

    # Операция
    operation = tokens.pop(0)
    if operation in operations:
        operation = operations[operation]
    else:
        raise ValueError(f"Неизвестная операция: {operation}")

    if tokens and tokens[0] in {"на", "с", "в"}:
        tokens.pop(0)

    # Вторая часть числа
    num2_tokens = []
    while tokens and (tokens[0] in numbers):
        num2_tokens.append(tokens.pop(0))

    num2 = text_to_number(" ".join(num2_tokens))

    # Выполнение операции
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ZeroDivisionError("Деление на ноль.")
        result = num1 // num2  # Используем целочисленное деление
    else:
        raise ValueError("Операция не поддерживается")

    return number_to_text(result)


# Запрос задачи у пользователя
expression = input("Введите задачу (например, 'два плюс три'): ").lower()

# Выполнение вычисления и вывод результата
try:
    result = calc(expression)
    print(f"Результат: {result}")
except Exception as e:
    print(f"Ошибка: {e}")

