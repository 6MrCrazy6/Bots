import telebot
from FilmComedia import *
from FilmHorror import *
from FilmCriminal import *
from Answer import *

bot = telebot.TeleBot('TOKEN')
prepareDb('db/Films.db')
prepareDb1('db/Question.db')

@bot.message_handler(commands=['start'])
def start(message):
    username = message.from_user.first_name
    bot.send_message(message.chat.id, f'Привіт {username}, я Каспер! Хочешь поговорити зі мною чи є якесь питання?')

@bot.message_handler(commands=['comedia'])
def comedia(message):
        filmsComedia = getFilmsComedia('db/Films.db')
        bot.send_message(message.chat.id, f'З комедій можу порадити: \n{filmsComedia}')

@bot.message_handler(commands=['horror'])
def horror(message):
        filmsHorror = getFilmsHorror('db/Films.db')
        bot.send_message(message.chat.id, f'З жахів можу порадити: \n{filmsHorror}')

@bot.message_handler(commands=['criminal'])
def criminal(message):
        filmsCriminal = getFilmsCriminal('db/Films.db')
        bot.send_message(message.chat.id, f'З кримінальних фільмів можу порадити: \n{filmsCriminal}')

@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id, f'Радий був допомогти!\n'
                                      f'Якщо захочете поговорити чи потрібна буде допомога введіть знову команду /start')


@bot.message_handler(content_types=["text"])
def text(message):
    if message.chat.type == 'private':
        if message.text == 'Поговорити':
            bot.send_message(message.chat.id, f'Добре, як настрій?' + '\U0001f642')
        if message.text == 'Так собі':
            bot.send_message(message.chat.id, f'Чому? Щось сталось?'
                                            f'Я можу якось допомогти тобі підняти настрій?' + '\U0001f61f')
        if message.text == 'Можеш порекомендувати якийсь фільм?':
            bot.send_message(message.chat.id, f'Так, звісно! Який жанр вас цікавить?\n'
                                              f'/comedia \n'
                                              f'/horror \n'
                                              f'/criminal \n')
        if message.text == 'Потрібна допомога':
                bot.send_message(message.chat.id, 'Думаю зможу допомогти вам. Задавайте питання.')
                bot.register_next_step_handler(message, answer)

def answer(message):
    user_text = message.text
    app_text = []
    app_text.append(user_text)
    answeer = getAnswer('db/Question.db', user_text, "answer")
    if answeer == []:
        bot.send_message(message.chat.id, f'Я не знаю відповідь на данне питання=(')
        addAnswer('db/Question.db', user_text)
        bot.send_message(message.chat.id, f'Можете дати відповідь на це питання?')
        bot.register_next_step_handler(message, updatAnswer)
    else:
        bot.send_message(message.chat.id, f'Відповідь на данне питання таке: \n'
                                          f'{answeer}')
        bot.register_next_step_handler(message, stop)

def updatAnswer(message):
    user_answer = message.text
    app_answer = []
    app_answer.append(user_answer)
    setAnswer('db/Question.db', user_answer)
    bot.send_message(message.chat.id, f'Дякую за допомогу!' + '\U0001f642')
    bot.register_next_step_handler(message, stop)

@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id, f'Радий був допомогти!\n'
                                      f'Якщо захочете поговорити чи потрібна буде допомога введіть знову команду /start')

bot.polling(none_stop=True)
