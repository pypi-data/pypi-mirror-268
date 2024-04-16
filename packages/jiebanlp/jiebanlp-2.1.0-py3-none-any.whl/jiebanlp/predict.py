import jieba.posseg as pseg
from .constant import flag_meanings


# 解析
def parser(text):
    words = pseg.cut(text)
    tagged_words = [
        {'word': word, 'flag': flag, 'flag_meaning': flag_meanings.get(flag, "未知")}
        for word, flag in words
    ]
    return tagged_words