import random

def guess_the_number():
    secret_number = random.randint(1, 10)
    attempts_left = 3

    while attempts_left > 0:
        user_guess = int(input(f"Угадайте число от 1 до 10. У вас осталось {attempts_left} попытка(ок): "))

        if user_guess == secret_number:
            print("Поздравляю! Вы угадали число!")
            break
        else:
            attempts_left -= 1
            if attempts_left == 0:
                print(f"К сожалению, вы не угадали. Правильное число было {secret_number}.")
            else:
                print("Неудача. Попробуйте ещё раз.")

if __name__ == "__main__":
    guess_the_number()


