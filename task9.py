# 1) Попросить пользователя ввести текст. В результате вывести процент букв в
# верхнем
# регистре (заглавные) и в нижнем регистре (прописные).
def func():
    text = input('Please wite your text: ')
    upper_ = 0
    lower_ = 0
    for i in text:
        if i.isupper():
            upper_ += 1
        else:
            lower_ += 1
    result = upper_ + lower_
    b = (upper_ / result) * 100
    c = (lower_ / result) * 100
    print(round(b, 2), "%", "Upper")
    print(round(c, 2), "%", "lower")
func()
