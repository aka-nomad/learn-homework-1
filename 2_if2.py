"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def comapre_str(string1, string2):
        if type(string1) is str and type(string2) is str:
            len1 = len(string1)
            len2 = len(string2)
            
            if len1 == len2:
              return 1
            elif len1 > len2:
              return 2 
            elif string1 != string2:
              return 3
            else:
               return 'No rule for such combinations' 
        else:
            return 0
            
    for i in range(0, 4):
        x = {0:1, 1:'Learn',2:'hello', 3:'python3'}
        y = {0:'Python', 1:'learn',2:'hello', 3:'PYTHON'}
        result = comapre_str(x[i], y[i])
        print(result)
        #print(x[i], y[i])
    
if __name__ == "__main__":
    main()
