import random
import telebot
from datetime import datetime
from dbWorker import *
from dbWorker2 import *
from dbTime import *

bot = telebot.TeleBot('TOKEN')
prepareDb('db/AllLitres.db')
prepareDb3('db/Timer.db')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Приветствую в баре! Чего желаете?')
    bot.send_message(message.chat.id, 'Список алкогольных напитков - /listalcoholdrinks \n'
                                      'Список безалкогольных напитков - /listnonalcoholdrinks\n')

@bot.message_handler(commands=['listalcoholdrinks'])
def listalcoholdrink(message):
    bot.send_message(message.chat.id, 'Вот список всех алкогольных напитков:3')
    bot.send_message(message.chat.id, 'Пиво - /drinkbeer \n'
                                      'Вино - /drinkwine \n'
                                      'Водка - /drinkvodka \n'
                                      'Виски - /drinkwhiskey \n'
                                      'Коньяк - /drinkcognac \n'
                                      'Пина колада - /drinkpinacolada \n'
                                      'Глинтвейн- /drinkmulledwine \n'
                                      'Саке - /drinksake \n'
                                      'Текила - /drinktequila \n'
                                      'Мохито - /drinkmojito \n'
                                      'Сидр - /drinkcider \n')

@bot.message_handler(commands=['listnonalcoholdrinks'])
def listnonalcoholdrinks(message):
    bot.send_message(message.chat.id, 'Вот список всех безалкогольных напитков:3')
    bot.send_message(message.chat.id, 'Чай - /drinktea \n'
                                      'Коффе- /drinkcoffe \n'
                                      'Кока-кола - /drinkcocacola \n'
                                      'Бабл Ти - /drinkbubbletea \n'
                                      'Морс - /drinkfruitdrink \n'
                                      'Молочный коктейль - /drinkmilkshake \n'
                                      'Спрайт - /drinksprite \n'
                                      'Фанта - /drinkfanta \n'
                                      'Безалкогольное пиво - /drinknonalcoholicbeer \n'
                                      'Безалкогольное мохито - /drinknonalcoholicmojito\n'
                                      'Вода - /drinkwater \n'
                                      'Содова - /drinkcreamsoda \n')

@bot.message_handler(commands=['drinkbeer'])
def drinkbeer(message):
    init_user('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres('db/AllLitres.db', user_name, "beer")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л пива.</em>' + '\U0001F37A \n'
                                         f'Всего вы выпили - {summ_litres} л пива', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "beer", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres('db/AllLitres.db', user_name, "beer")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л пива.</em>' + '\U0001F37A \n'
                                         f'Всего вы выпили - {summ_litres} л пива', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "beer", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinkwine'])
def drinkwine(message):
    init_user('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres('db/AllLitres.db', user_name, "wine")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л вина.</em>' + '\U0001F37A \n'
                                        f'Всего вы выпили - {summ_litres} л вина', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "wine", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres('db/AllLitres.db', user_name, "wine")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л вина.' + '\U0001F377 \n'
                                        f'Всего вы выпили - {summ_litres} л вина </em>\n', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "wine", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinkvodka'])
def drinkvodka(message):
    init_user('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres('db/AllLitres.db', user_name, "vodka")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л водки.</em>' + '\U0001F376\U0001F321 \n'
                                        f'Всего вы выпили - {summ_litres} л водки', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "vodka", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres('db/AllLitres.db', user_name, "vodka")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л водки.' + '\U0001F376\U0001F321 \n'
                                        f'Всего вы выпили - {summ_litres} л водки </em>\n', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "vodka", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinkwhiskey'])
def drinkwhiskey(message):
    init_user('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres('db/AllLitres.db', user_name, "whiskey")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л виски.</em>' + '\U0001F943 \n'
                         f'Всего вы выпили - {summ_litres} л виски', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "whiskey", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres('db/AllLitres.db', user_name, "whiskey")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л виски.' + '\U0001F943 \n'
                                        f'Всего вы выпили - {summ_litres} л виски </em>\n', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "whiskey", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinkcognac'])
def drinkcognac(message):
    init_user('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres('db/AllLitres.db', user_name, "cognac")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л коньяку.</em>' + '\U0001F943\U0001F9CA \n'
                                         f'Всего вы выпили - {summ_litres} л коньяка', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "cognac", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres('db/AllLitres.db', user_name, "cognac")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л коньяку.' + '\U0001F943\U0001F9CA \n'
                                         f'Всего вы выпили - {summ_litres} л коньяка </em>\n', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "cognac", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinkmulledwine'])
def drinkmulledwine(message):
    init_user('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres('db/AllLitres.db', user_name, "mulledwine")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л глинтвейна.' + '\U00002615\U0001F377 \n'
                                        f'Всего вы выпили - {summ_litres} л глинтвейна </em>\n', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "mulledwine", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres('db/AllLitres.db', user_name, "mulledwine")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л глинтвейна.' + '\U00002615\U0001F377 \n'
                                        f'Всего вы выпили - {summ_litres} л глинтвейна </em>\n', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "mulledwine", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinksake'])
def drinksake(message):
    init_user('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres('db/AllLitres.db', user_name, "sake")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л саке.'+'\U0001F376	\n'
                                        f'Всего вы выпили - {summ_litres} л саке </em>\n', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "sake", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres('db/AllLitres.db', user_name, "sake")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л саке.' + '\U0001F376 \n'
                                        f'Всего вы выпили - {summ_litres} л саке </em>\n', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "sake", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinktequila'])
def drinktequila(message):
    init_user('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres('db/AllLitres.db', user_name, "tequila")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л текилы.'+'\U0001F378\U0001F335\n'
                                        f'Всего вы выпили - {summ_litres} л текилы </em>\n', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "tequila", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres('db/AllLitres.db', user_name, "tequila")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л текилы.'+'\U0001F378\U0001F335\n'
                                        f'Всего вы выпили - {summ_litres} л текилы </em>\n', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "tequila", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinkmojito'])
def drinkmojito(message):
    init_user('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres('db/AllLitres.db', user_name, "mojito")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л мохито.'+'\U0001F378\U0001F335\n'
                                        f'Всего вы выпили - {summ_litres} л мохито </em>\n', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "mojito", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres('db/AllLitres.db', user_name, "mojito")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л мохито.'+'\U0001F378\U0001F335\n'
                                        f'Всего вы выпили - {summ_litres} л мохито </em>\n', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "mojito", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinkpinacolada'])
def drinkpinacolada(message):
    init_user('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres('db/AllLitres.db', user_name, "pinacolada")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л пина колады.'+'\U0001F943\U0001F34D\U0001F965\n'
                                        f'Всего вы выпили - {summ_litres} л пина колады </em>\n', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "pinacolada", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres('db/AllLitres.db', user_name, "pinacolada")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л пина колады.'+'\U0001F943\U0001F34D\U0001F965\n'
                                        f'Всего вы выпили - {summ_litres} л пина колады </em>\n', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "pinacolada", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinkcider'])
def drinkcider(message):
    init_user('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres('db/AllLitres.db', user_name, "cider")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л сидра.'+'\U0001F37A\U0001F34F\n'
                                        f'Всего вы выпили - {summ_litres} л сидра </em>\n', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "cider", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres('db/AllLitres.db', user_name, "cider")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л сидра.'+'\U0001F37A\U0001F34F\n'
                                        f'Всего вы выпили - {summ_litres} л сидра </em>\n', parse_mode='html')
        setLitres('db/AllLitres.db', user_name, "cider", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinktea'])
def drinktea(message):
    init_user1('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres2('db/AllLitres.db', user_name, "tea")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л чая.' + '\U0001F375 \n'
                                          f'Всего вы выпили - {summ_litres} л чая </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "tea", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres2('db/AllLitres.db', user_name, "tea")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л чая.' + '\U0001F375 \n'
                                         f'Всего вы выпили - {summ_litres} л чая </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "tea", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinkcoffe'])
def drinkcoffe(message):
    init_user1('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres2('db/AllLitres.db', user_name, "coffe")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л коффе.' + '\U00002615 \n'
                                          f'Всего вы выпили - {summ_litres} л коффе </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "coffe", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres2('db/AllLitres.db', user_name, "coffe")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л коффе.' + '\U00002615 \n'
                                          f'Всего вы выпили - {summ_litres} л коффе </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "coffe", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinkbubbletea'])
def drinkbubbletea(message):
    init_user1('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres2('db/AllLitres.db', user_name, "bubbletea")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л бабл ти.' + '\U0001F9CB \n'
                                         f'Всего вы выпили - {summ_litres} л бабл ти </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "bubbletea", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres2('db/AllLitres.db', user_name, "bubbletea")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л бабл ти.' + '\U0001F9CB \n'
                                         f'Всего вы выпили - {summ_litres} л бабл ти </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "bubbletea", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinkcocacola'])
def drinkcocacola(message):
    init_user1('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres2('db/AllLitres.db', user_name, "cocacola")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л кока-колы.' + '\U0001F534\U000026AA \n'
                                          f'Всего вы выпили - {summ_litres} л кока-колы </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "cocacola", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres2('db/AllLitres.db', user_name, "cocacola")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л кока-колы.' + '\U0001F534\U000026AA \n'
                                          f'Всего вы выпили - {summ_litres} л кока-колы </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "cocacola", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinkfruitdrink'])
def drinkfruitdrink(message):
    init_user1('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres2('db/AllLitres.db', user_name, "fruitdrink")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л морса.' + '\U0001F379 \n'
                                          f'Всего вы выпили - {summ_litres} л морса </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "fruitdrink", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres2('db/AllLitres.db', user_name, "fruitdrink")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л морса.' + '\U0001F379 \n'
                                          f'Всего вы выпили - {summ_litres} л морса </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "fruitdrink", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinkmilkshake'])
def drinkmilkshake(message):
    init_user1('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres2('db/AllLitres.db', user_name, "milkshake")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л молочного коктейля.' + '\U0001F95B \n'
                                         f'Всего вы выпили - {summ_litres} л молочного коктейля </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "milkshake", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres2('db/AllLitres.db', user_name, "milkshake")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л молочного коктейля.' + '\U0001F95B \n'
                                         f'Всего вы выпили - {summ_litres} л молочного коктейля </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "milkshake", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinksprite'])
def drinksprite(message):
    init_user1('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres2('db/AllLitres.db', user_name, "sprite")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л спрайта.' + '\U0001F7E2 \n'
                                          f'Всего вы выпили - {summ_litres} л спрайта </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "sprite", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres2('db/AllLitres.db', user_name, "sprite")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л спрайта.' + '\U0001F7E2 \n'
                                          f'Всего вы выпили - {summ_litres} л спрайта </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "sprite", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinkfanta'])
def drinkfanta(message):
    init_user1('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres2('db/AllLitres.db', user_name, "fanta")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л фанты.' + '\U0001F7E0	\n'
                                         f'Всего вы выпили - {summ_litres} л фанты </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "fanta", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres2('db/AllLitres.db', user_name, "fanta")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л фанты.' + '\U0001F7E0	\n'
                                          f'Всего вы выпили - {summ_litres} л фанты </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "fanta", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinknonalcoholicbeer'])
def drinknonalcoholicbeer(message):
    init_user1('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres2('db/AllLitres.db', user_name, "nonalcoholicbeer")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л безалкогольного пива.' + '\U0001F37B \n'
                                          f'Всего вы выпили - {summ_litres} л безалкогольного пива </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "nonalcoholicbeer", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres2('db/AllLitres.db', user_name, "nonalcoholicbeer")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л безалкогольного пива.' + '\U0001F37B \n'
                                          f'Всего вы выпили - {summ_litres} л безалкогольного пива </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "nonalcoholicbeer", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinknonalcoholicmojito'])
def drinknonalcoholicmojito(message):
    init_user1('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres2('db/AllLitres.db', user_name, "nonalcoholicmojito")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л безалкогольного мохито.' + '\U0001F378\U0001F335\n'
                                         f'Всего вы выпили - {summ_litres} л безалкогольного мохито </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "nonalcoholicmojito", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres2('db/AllLitres.db', user_name, "nonalcoholicmojito")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л безалкогольного мохито.' + '\U0001F378\U0001F335\n'
                                         f'Всего вы выпили - {summ_litres} л безалкогольного мохито </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "nonalcoholicmojito", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinkwater'])
def drinkwater(message):
    init_user1('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres2('db/AllLitres.db', user_name, "water")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л воды.' + '\U0001F964\n'
                                         f'Всего вы выпили - {summ_litres} л воды. </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "water", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres2('db/AllLitres.db', user_name, "water")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л воды.' + '\U0001F964\n'
                                         f'Всего вы выпили - {summ_litres} л воды </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "water", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

@bot.message_handler(commands=['drinkcreamsoda'])
def drinkcreamsoda(message):
    init_user1('db/AllLitres.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    endTimes = getTime('db/Timer.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if endTimes == None:
        init_user3('db/Timer.db', message.from_user.first_name)
        currentLitres = getLitres2('db/AllLitres.db', user_name, "creamsoda")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л содовой.' + '\U0001f4a7\n'
                                            f'Всего вы выпили - {summ_litres} л содовой </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "creamsoda", summ_litres)
    elif now_time > endTimes:
        currentLitres = getLitres2('db/AllLitres.db', user_name, "creamsoda")
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л содовой ' + '\U0001f4a7\n'
                                        f'Всего вы выпили - {summ_litres} л содовой </em>\n', parse_mode='html')
        setLitres2('db/AllLitres.db', user_name, "creamsoda", summ_litres)
        delTime('db/Timer.db', user_name)
        init_user3('db/Timer.db', message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 2 минуты еще не прошло! </em>' + '\U0001F621\n', parse_mode='html')

bot.polling(none_stop=True)
