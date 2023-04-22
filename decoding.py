from textwrap import wrap

import visual.visual


def code_preparation_decoding(decoding_text, decoding_kay):
    """Принимает код из visual VISUAL windows
    принимает ключ из visual VISUAL windows
    разделяет на разряды, сохроняет в список
    передает в DECODING de_coding"""

    # разделение на разряды
    decoding_text_separation = wrap(decoding_text, 10)

    # декодинг на ключ
    text_decoding = []
    for i in decoding_text_separation:
        text_decoding.append(int(i) // int(decoding_kay))

    # перевод с aski
    join_code = "".join(map(str, text_decoding))
    code_sepor = wrap(join_code, 2)
    finale_code = list(map(int, code_sepor))

    # перевод в текст
    finale_text = [chr(c) for c in finale_code]
    finale_text_join = "".join(map(str, finale_text))
    finale_text_join = finale_text_join.lower()

    # вызов
    visual.visual.return_decoding_text(return_dec_text=finale_text_join)


