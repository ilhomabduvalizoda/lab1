def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
        return None


def main():
    global result
    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")

        choice = input("Введите номер операции (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)

            if result is not None:
                print(f"Результат: {result}")

        elif choice == '5':
            break
        else:
            print("Неправильный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()