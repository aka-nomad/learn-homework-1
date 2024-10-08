"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
    answer = ''
    
    while True:
       try:
          answer = input('How are you?')
          if answer in ('Good', 'good'):
            break
       except KeyboardInterrupt:
          print('\n', 'Good-bye!!!')
          break

    
if __name__ == "__main__":
    hello_user()
