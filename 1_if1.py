"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = int(input('Please enter your age:'))

    def detect(age):
        if 3 <= age <= 6:
            return 'You should be in kindergarden'
        elif 7 <= age <=18:
            return 'You should be in school boy'
        elif 18 <= age <= 23:
            return 'You should be in University dude'
        else:
            return 'You should probably work man'
        
    result = detect (age)
    print(result)

if __name__ == "__main__":
    main()
