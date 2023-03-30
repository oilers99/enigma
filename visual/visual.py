import tkinter
from tkinter import *

import main
def windows():
    """Основное окно
    2 поля ввода, 2 поля для ключа, 2 кнопки, 2 поля вывода"""

    def click_code():
        """передает текст в tests TEST test_en
         передает ключ в tests TEST test_kay"""
        pass

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
    lbl_kay_1 = tkinter.Label(top, text="         Введите ключ: (32-99)", font=16)
    lbl_kay_1.grid(row=2, column=0, sticky="W", padx=10, pady=5)

    # поле ввода ключ КОД
    kay_code = tkinter.Entry(top, font=14)
    kay_code.grid(row=2, column=1, padx=10, pady=5)
    lbl_kay_2 = tkinter.Label(top, text="        Введите ключ: (32-99)", font=16)
    lbl_kay_2.grid(row=2, column=1, sticky="W", padx=10, pady=5)

    # кнопка закодить
    button_code_text = tkinter.Button(top, text="Поехали!!!", font=16, width=20, command=click_code)
    button_code_text.grid(row=2, column=0, padx=10, pady=5, sticky="E")

    # кнопка раскодить
    button_decode = tkinter.Button(top, text="Поехали!!!", font=16, width=20, command=click_decode)
    button_decode.grid(row=2, column=1, padx=10, pady=5, sticky="E")

    # место под вывод кода
    lbl_return_code = tkinter.Text(top, font=14, wrap="char")
    lbl_return_code.grid(row=3, column=0, sticky="NESW", padx=10, pady=5)
    top.grid_rowconfigure(3, weight=1)

    # место для вывода текста
    lbb_return_text = tkinter.Text(top, font=14, wrap="char")
    lbb_return_text.grid(row=3, column=1, sticky="NESW", padx=10, pady=5)

    top.mainloop()
