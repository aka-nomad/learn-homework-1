"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging, ephem, settings, datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

"""
PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}
"""

def get_constellation(update, context):
    try:
        user_planet = update.message.text.split()[1].lower()
        current_date = datetime.datetime.now().strftime('%Y/%m/%d')
        planets = {
            'mercury': ephem.Mercury(), 'venus':ephem.Venus(), 'mars':ephem.Mars(),'jupiter':ephem.Jupiter(), 
            'saturn':ephem.Saturn(), 'uranus':ephem.Uranus(), 'neptun':ephem.Neptune()
            }

        if user_planet != '':
            planet = planets.get(user_planet)
            compute = planet.compute(current_date)
            update.message.reply_text(ephem.constellation(planet)[1])
    except IndexError:
        update.message.reply_text('ERROR! You do not determine the planet')
    
    u = ephem.planet
    print()
    ephem.constellation

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
