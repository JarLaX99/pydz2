# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))
num1=1
for _ in range(s) :
    num2 = (s-num1)
    if (num2)+num1== s and num2*num1 == p :
        print(num1,num2)
        break
    else :
        num1+=1
else :
    print("Ошибка: Введите коректные числа")