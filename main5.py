import requests

def get_exchange_rate(base_currency, target_currency):
    api_key = "141f654b848b3d077a9698bc"
    api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        rate = data["conversion_rate"]
        return rate
    else:
        print(f"Ошибка при получении курса валют: статус-код {response.status_code}")
        return None

def convert_amount(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate:
        converted_amount = amount * rate
        return round(converted_amount, 2)
    else:
        return None

def main():
    while True:
        print("\nДобро пожаловать в конвертер валют!\n")
        print("1. Рубли в Доллары")
        print("2. Доллары в Рубли")
        print("3. Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            rubles = float(input("Введите сумму в рублях: "))
            dollars = convert_amount(rubles, "RUB", "USD")
            if dollars:
                print(f"{rubles} рублей = {dollars} долларов")
        elif choice == "2":
            dollars = float(input("Введите сумму в долларах: "))
            rubles = convert_amount(dollars, "USD", "RUB")
            if rubles:
                print(f"{dollars} долларов = {rubles} рублей")
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()