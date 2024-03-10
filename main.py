#В консоль вводится 2 числа, нужно проверить, является ли произведения остатков от деления каждого числа на 2 числа больше среднего арифметического этих чисел.
#(Ввод в консоль нужно проделать 10 раз)
#Проверку нужно запихнуть в функцию, которая возвращает либо True, либо False



def check_products(num1, num2):
  summ = (num1 + num2) / 2
  product = (num1 % 2) * (num2 % 2)
  return summ > product

for i in range(10):
    num1 = int(input())
    num2 = int(input())
    result = check_products(num1, num2)
    print(result)
