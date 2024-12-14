import tkinter as tk
import string
import random

class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.password_label = None
        self.length_entry = None
        self.title("Генератор паролей")
        self.geometry("300x250")

        self.lower_case_var = tk.BooleanVar(value=False)
        self.digits_var = tk.BooleanVar(value=False)
        self.special_chars_var = tk.BooleanVar(value=False)

        self.create_widgets()

    def create_widgets(self):
        label_length = tk.Label(self, text="Длина пароля:")
        label_length.pack(pady=(20, 0))

        self.length_entry = tk.Entry(self, width=30)
        self.length_entry.insert(0, "8")  # Default value
        self.length_entry.pack(pady=(0, 20))

        check_lower_case = tk.Checkbutton(self, text="Включить алфавит нижнего регистра [a-z]",
                                          variable=self.lower_case_var)
        check_lower_case.pack()

        check_digits = tk.Checkbutton(self, text="Включить цифры [0-9]", variable=self.digits_var)
        check_digits.pack()

        check_special_chars = tk.Checkbutton(self, text="Включить спецсимволы [! @ # $ %]",
                                             variable=self.special_chars_var)
        check_special_chars.pack()

        generate_button = tk.Button(self, text="Сгенерировать пароль",
                                    command=self.generate_password)
        generate_button.pack(pady=(20, 0))

        self.password_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.password_label.pack(pady=(20, 0))

    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())
        except ValueError:
            self.password_label.config(text="Ошибка: длина пароля должна быть числом!", fg="red")
            return

        character_set = ""

        if self.lower_case_var.get():
            character_set += string.ascii_lowercase
        if self.digits_var.get():
            character_set += string.digits
        if self.special_chars_var.get():
            character_set += "!@#$%"

        if len(character_set) == 0:
            self.password_label.config(text="Ошибка: выберите хотя бы один параметр!", fg="red")
            return

        password = ''.join(random.choice(character_set) for _ in range(password_length))
        self.password_label.config(text=f"Сгенерированный пароль: {password}", fg="black")

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()