import sqlite3
import hashlib
import tkinter as tk
from tkinter import *
from functools import partial

def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    if row is not None:
        db_username = row[0]
        db_password = row[1]
        encrypted_pw = encrypt_password(password)
        if db_username == username and db_password == encrypted_pw:
            return True
    return False

def register_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES (?, ?)", (username, encrypt_password(password)))
    conn.commit()
    conn.close()
    return True

def open_registration_window():
    reg_win = Toplevel(root)
    reg_win.title("Регистрация")
    Label(reg_win, text="Логин:").grid(row=0, sticky=E)
    reg_uname = Entry(reg_win, width=25)
    reg_uname.grid(row=0, column=1)
    Label(reg_win, text="Пароль:").grid(row=1, sticky=E)
    reg_passwd = Entry(reg_win, show="*", width=25)
    reg_passwd.grid(row=1, column=1)
    Button(reg_win, text="Зарегистрироваться", command=partial(register_user, reg_uname.get(), reg_passwd.get())).grid(row=2, sticky=W+E+N+S)
    Button(reg_win, text="Отмена", command=reg_win.destroy).grid(row=2, column=1, sticky=W+E)

def open_login_window():
    login_win = Toplevel(root)
    login_win.title("Авторизация")
    Label(login_win, text="Логин:").grid(sticky=E)
    login_uname = Entry(login_win, width=25)
    login_uname.grid(row=0, column=1)
    Label(login_win, text="Пароль:").grid(row=1, sticky=E)
    login_passwd = Entry(login_win, show="*", width=25)
    login_passwd.grid(row=1, column=1)
    Button(login_win, text="Войти", command=partial(check_login, login_uname.get(), login_passwd.get())).grid(row=2, sticky=W+E+N+S)
    Button(login_win, text="Отмена", command=login_win.destroy).grid(row=2, column=1, sticky=W+E)

root = tk.Tk()
root.title("Авторизация")
Button(root, text="Вход", command=open_login_window).pack(side=LEFT)
Button(root, text="Регистрация", command=open_registration_window).pack(side=RIGHT)
root.bind("<Escape>", lambda e: root.quit())
root.mainloop()
