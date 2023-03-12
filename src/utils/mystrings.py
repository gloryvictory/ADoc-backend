import re


def strip_last(s: str, ch: str = ' ') -> str:
    if s and s[-1] == ch:
        return s[:-1]
    return s


def str_cleanup(s: str):  # удаляем лишние пробелы
    out_s = s
    while '  ' in out_s:
        out_s = out_s.strip().replace('  ', ' ')
    return out_s
    # return out_s, len(s) - len(out_s)


# def clean_string(value):
#     return re.sub('[ ]{2,}', ' ', value.strip())

def removing_leading_whitespaces(text):
    return re.sub(r"^\s+", "", text)