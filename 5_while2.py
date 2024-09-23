"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    dicts = {
        "как дела": "Хорошо!", "что делаешь": "Программирую", "сколько тебе лет":"У меня нет возраста", "любишь питон":"Да"
        }
    
    while True:
        answer = input("Задай свой вопрос:").lower()
        if answer[-1] == '?':
            answer = answer.rstrip('?')

        if answer in ("Пока", "пока"):
            print("Пока!")
            break
        else:
            print(f"Пользователь: {answer}\nПрограмма:{dicts.get(answer, 'У меня нет ответа на данный вопрос')}")
            
if __name__ == "__main__":
    ask_user(questions_and_answers)
