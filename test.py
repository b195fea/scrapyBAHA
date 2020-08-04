from pypinyin import pinyin, lazy_pinyin, Style

a = pinyin('中心', heteronym=True)
b = pinyin('中心', style=Style.BOPOMOFO)  # 注音风格
print(b)