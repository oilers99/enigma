import tkinter
from tkinter import *
import main


def windows():
    """Основное окно
    2 поля ввода, 2 поля для ключа, 2 кнопки, 2 поля вывода"""

    def click_code():
        """обрабатывает клик, проверят
        если ошибка передает в visual VISUAL miss_send
        если ошибок нет MAIN text_preparation"""
        text_pre = text_entry.get("1.0", "end")
        text_pre = text_pre.upper()
        kay_pre = kay_text.get()
        text_pre_aski = [ord(c) for c in text_pre]

        # проверка на ошибки
        count = 0
        if int(kay_pre) not in range(31, 100):
            count += 1
        for i in text_pre_aski:
            if int(i) not in range(31, 96) and int(i) != 10:
                count += 10

        # передача ошибки и вызов
        if count == 1:
            miss_send(kay_miss="Неверный ключ!")
        if count > 1 and count % 2 == 0:
            miss_send(kay_miss="Только английские буквы и цифры")
        if count > 1 and count % 2 != 0:
            miss_send(kay_miss="Миша, всё хуйня, давай по новой ...!")

        # ошибки нет!!! передаем в MAIN
        if count == 0:
            main.text_preparation(kay_to_coding=kay_pre, text_to_coding=text_pre)

    def click_decode():
        """передает код и ключ в DECODING code_preparation"""
        pass

    # основное окно
    top = tkinter.Tk()
    top.resizable(False, False)
    top.title("EnIgma")
    top.geometry("1600x750")

    # текст
    lbl_1 = tkinter.Label(top, text="Введите текст (только английские буквы и цыфры) ", font=16)
    lbl_1.grid(row=0, column=0)
    top.grid_columnconfigure(0, weight=780)

    lbl_2 = tkinter.Label(top, text="Введите код", font=16)
    lbl_2.grid(row=0, column=1)
    top.grid_columnconfigure(1, weight=780)

    # поле ввода ТЕКСТ
    text_entry = tkinter.Text(top, font=14, wrap="char")
    text_entry.grid(row=1, column=0, sticky="NESW", padx=10, pady=5)
    top.grid_rowconfigure(1, weight=450)

    # поле ввода КОД
    code_entry = tkinter.Text(top, font=14, wrap="char")
    code_entry.grid(row=1, column=1, sticky="NESW", padx=10, pady=5)
    top.grid_rowconfigure(1, weight=450)

    # поле ввода ключ ТЕКСТА
    kay_text = tkinter.Entry(top, font=14)
    kay_text.grid(row=2, column=0, padx=10, pady=5)
    lbl_kay_1 = tkinter.Label(top, text="       Введите ключ: (32-99)", font=16)
    lbl_kay_1.grid(row=2, column=0, sticky="W", padx=10, pady=5)

    # поле ввода ключ КОД
    kay_code = tkinter.Entry(top, font=14)
    kay_code.grid(row=2, column=1, padx=10, pady=5)
    lbl_kay_2 = tkinter.Label(top, text="       Введите ключ: (32-99)", font=16)
    lbl_kay_2.grid(row=2, column=1, sticky="W", padx=10, pady=5)

    # кнопка закодить
    button_code_text = tkinter.Button(top, text="Поехали!!!", font=16, width=20, command=click_code)
    button_code_text.grid(row=2, column=0, padx=10, pady=5, sticky="E")

    # кнопка раскодить
    button_decode = tkinter.Button(top, text="Поехали!!!", font=16, width=20, command=click_decode)
    button_decode.grid(row=2, column=1, padx=10, pady=5, sticky="E")

    # место под вывод кода
    text_miss = tkinter.Text()
    lbl_return_code = tkinter.Text(top, font=14, wrap="char")
    lbl_return_code.grid(row=3, column=0, sticky="NESW", padx=10, pady=5)
    top.grid_rowconfigure(3, weight=1)

    # место для вывода текста
    lbb_return_text = tkinter.Text(top, font=14, wrap="char")
    lbb_return_text.grid(row=3, column=1, sticky="NESW", padx=10, pady=5)

    # вызов
    top.mainloop()


def miss_send(kay_miss):
    """принимает из visual VISUAL windows click_code
    ошибку, выдает сообшение"""
    masage_miss = tkinter.Text(font=14, wrap="char")
    masage_miss.grid(row=3, column=0, sticky="NESW", padx=10, pady=5)
    masage_miss.insert("1.0", f"{kay_miss}")

def is_work(is_work_code):
    """принимает закодированный текст из MAIN encryption
    выводит в окно"""
    masage_print = tkinter.Text(font=14, wrap="char")
    masage_print.grid(row=3, column=0, sticky="NESW", padx=10, pady=5)
    masage_print.insert("1.0", f"{is_work_code}")

