import visual.visual
from textwrap import wrap


def text_preparation(kay_to_coding, text_to_coding):
    """Принимает текст и ключь из visual VISUAL windows click_code
    разделяет на разряды, сохроняет в список
    передает в MAIN encryption"""

    # перевод в аски удаление 10ки
    aski_text = [ord(c) for c in text_to_coding]
    aski_text.remove(10)

    # склейка и нарезка на разряды
    join_text_aski = "".join(map(str, aski_text))
    join_text_aski = wrap(join_text_aski, 8)
    len_last_aski = (8 - len(join_text_aski[-1])) // 2
    if len_last_aski != 0:
        join_text_aski[-1] = join_text_aski[-1] + "32" * len_last_aski

    # вызов
    encryption(use_kay=kay_to_coding, use_code=join_text_aski)


def encryption(use_kay, use_code):
    """Принимает список из MAIN text_preparation,
    шифрует, соеденяет, передаеет в
    visual VISUAL ****"""

    # кодирование
    coding_text = []
    for i in use_code:
        coding_text.append(int(i) * int(use_kay))

    # склейка
    return_code = "".join(map(str, coding_text))

    # вызов
    visual.visual.is_work(is_work_code=return_code)


def main():
    visual.visual.windows()


if __name__ == "__main__":
    main()
