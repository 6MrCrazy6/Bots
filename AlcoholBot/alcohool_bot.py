import random
import telebot
import re
from telebot import types
from datetime import datetime
from dbWorker import *
from dbWorker2 import *
from dbTime import *
from dbCompetitions import *
from dbCompetitors import *

bot = telebot.TeleBot('5969375412:AAGJ3bqPeOfZf8XWgnpfxRsSAIgv4qEVJyU')
prepareDb('db/database.db')
prepareDb2('db/database2.db')
prepareDb3('db/time.db')
prepareDb4('db/competitions.db')
prepareDb5('db/competitors.db')

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
                                      'Безалкогольное мохито - /drinknonalcoholicmojito')


@bot.message_handler(commands=['drinkbeer'])
def drinkbeer(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "beer")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л пива.</em>'+'\U0001F37A \n'
                                          f'Всего вы выпили - {summ_litres} л пива', parse_mode='html')
        setLitres('db/database.db', user_name, "beer", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinkwine'])
def drinkwine(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "wine")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л вина.'+'\U0001F377 \n'
                                        f'Всего вы выпили - {summ_litres} л вина </em>\n', parse_mode='html')
        setLitres('db/database.db', user_name, "wine", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinkvodka'])
def drinkvodka(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "vodka")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л водки.'+'\U0001F376\U0001F321 \n'
                                        f'Всего вы выпили - {summ_litres} л водки </em>\n', parse_mode='html')
        setLitres('db/database.db', user_name, "vodka", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinkwhiskey'])
def drinkwhiskey(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "whiskey")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л виски.'+'\U0001F943 \n'
                                        f'Всего вы выпили - {summ_litres} л виски </em>\n', parse_mode='html')
        setLitres('db/database.db', user_name, "whiskey", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinkcognac'])
def drinkcognac(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "cognac")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л коньяку.'+'\U0001F943\U0001F9CA \n'
                                        f'Всего вы выпили - {summ_litres} л коньяка </em>\n', parse_mode='html')
        setLitres('db/database.db', user_name, "cognac", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinkmulledwine'])
def drinkmulledwine(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "mulledwine")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л глинтвейна.'+'\U00002615\U0001F377 \n'
                                        f'Всего вы выпили - {summ_litres} л глинтвейна </em>\n', parse_mode='html')
        setLitres('db/database.db', user_name, "mulledwine", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinksake'])
def drinksake(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "sake")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л саке.'+'\U0001F376	\n'
                                        f'Всего вы выпили - {summ_litres} л саке </em>\n', parse_mode='html')
        setLitres('db/database.db', user_name, "sake", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinktequila'])
def drinktequila(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "tequila")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л текилы.'+'\U0001F378\U0001F335\n'
                                          f'Всего вы выпили - {summ_litres} л текилы </em>\n', parse_mode='html')
        setLitres('db/database.db', user_name, "tequila", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)


@bot.message_handler(commands=['drinkmojito'])
def drinkmojito(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "mojito")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л мохито.'+'\U0001F378\U0001F335\n'
                                          f'Всего вы выпили - {summ_litres} л мохито </em>\n', parse_mode='html')
        setLitres('db/database.db', user_name, "mojito", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinkpinacolada'])
def drinkpinacolada(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "pinacolada")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л пина колады.'+'\U0001F943\U0001F34D\U0001F965\n'
                                          f'Всего вы выпили - {summ_litres} л пина колады </em>\n', parse_mode='html')
        setLitres('db/database.db', user_name, "pinacolada", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinkcider'])
def drinkcider(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "cider")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л сидра.'+'\U0001F37A\U0001F34F\n'
                                          f'Всего вы выпили - {summ_litres} л сидра </em>\n', parse_mode='html')
        setLitres('db/database.db', user_name, "cider", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinktea'])
def drinktea(message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "tea")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л чая.</em>'+'\U0001F375 \n'
                                        f'Всего вы выпили - {summ_litres} л чаю', parse_mode='html')
        setLitres2('db/database2.db', user_name, "tea", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinkcoffe'])
def drinkcoffe(message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "coffe")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л коффе.</em>'+'\U00002615 \n'
                                        f'Всего вы выпили - {summ_litres} л коффе', parse_mode='html')
        setLitres2('db/database2.db', user_name, "coffe", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinkbubbletea'])
def drinkbubbletea(message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "bubbletea")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л бабл ти.</em>'+'\U0001F9CB \n'
                                        f'Всего вы выпили - {summ_litres} л бабл ти', parse_mode='html')
        setLitres2('db/database2.db', user_name, "bubbletea", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinkcocacola'])
def drinkcocacola(message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "cocacola")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л кока-колы.</em>'+'\U0001F534\U000026AA \n'
                                        f'Всего вы выпили - {summ_litres} л кока-колы', parse_mode='html')
        setLitres2('db/database2.db', user_name, "cocacola", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinkfruitdrink'])
def drinkfruitdrink(message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "fruitdrink")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л морса.</em>'+'\U0001F379	 \n'
                                        f'Всего вы выпили - {summ_litres} л морса', parse_mode='html')
        setLitres2('db/database2.db', user_name, "fruitdrink", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinkmilkshake'])
def drinkmilkshake(message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "milkshake")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л молочного коктейля.</em>'+'\U0001F95B \n'
                                        f'Всего вы выпили - {summ_litres} л молочного коктейля', parse_mode='html')
        setLitres2('db/database2.db', user_name, "milkshake", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinksprite'])
def drinksprite(message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "sprite")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л спрайта.</em>'+'\U0001F7E2 \n'
                                        f'Всего вы выпили - {summ_litres} л спрайта', parse_mode='html')
        setLitres2('db/database2.db', user_name, "sprite", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinkfanta'])
def drinkfanta(message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "fanta")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л фанты.</em>'+'\U0001F7E0	\n'
                                        f'Всего вы выпили - {summ_litres} л фанты', parse_mode='html')
        setLitres2('db/database2.db', user_name, "fanta", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinknonalcoholicbeer'])
def drinknonalcoholicbeer(message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "nonalcoholicbeer")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л безалкогольного пива.</em>'+'\U0001F37B \n'
                                        f'Всего вы выпили - {summ_litres} л безалкогольного пива', parse_mode='html')
        setLitres2('db/database2.db', user_name, "nonalcoholicbeer", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['drinknonalcoholicmojito'])
def drinknonalcoholicmojito(message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "nonalcoholicmojito")
    init_user3('db/time.db', message.from_user.first_name)
    endTimes = getTime('db/time.db', user_name, "end_time")
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time > endTimes:
        randomize = random.randint(1, 16)
        summ_litres = currentLitres + randomize
        bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л безалкогольного мохито.</em>'+'\U0001F378\U0001F335\n'
                                         f'Всего вы выпили - {summ_litres} л безалкогольного мохито', parse_mode='html')
        setLitres2('db/database2.db', user_name, "nonalcoholicmojito", summ_litres)
        delTime('db/time.db', user_name)
    else:
        bot.send_message(message.chat.id, f'<em>{user_name}, 5 минут еще не прошло! </em>'+'\U0001F621\n', parse_mode='html')
    print(endTimes)
    print(now_time)

@bot.message_handler(commands=['CreateTable'])
def createtable(message):
    CreateTable = re.split(r' ', message.text, maxsplit=1)[1]
    name_table = ' '.join(CreateTable)
    init_user4('db/competitions.db', name_table)
    first_name = message.from_user.first_name
    bot.send_message(message.chat.id, f'<em>{first_name}, cтол {CreateTable} cоздан. Приглашайте своих друзей! </em>'+'\U0001F60A\n', parse_mode='html')

@bot.message_handler(commands=['invite'])
def invite(message):
    markup_inline = types.InlineKeyboardMarkup(row_width=2)
    items_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    items_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    markup_inline.add(items_yes, items_no)
    msg = re.split(r' ', message.text, maxsplit=1)
    msg.pop(0)
    bot.send_message(message.chat.id, f'<em>{msg[0]}, вас пригласили к столу! \n'
                                      f'Согласны ли вы поучаствовать? </em>'+'\U0001F60A\n', parse_mode='html', reply_markup=markup_inline)

@bot.callback_query_handler(func=lambda call:True)
def answer(call):
    username = call.message.chat.username
    if call.data == 'yes':
        init_user5('db/competitors.db', username)
        bot.send_message(call.message.chat.id, f'<em> Отлично! Человек был добавлен к столу! </em>'+'\U0001F600\n', parse_mode='html')
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, f'<em> К сожалению, человек отказлся участвовать в данном столе. \n'
                                               f'Выбирете кого-то другого </em>'+'\U0001f61e\n', parse_mode='html')

@bot.message_handler(commands=['stoptable'])
def stoptable(message):
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    table_status = 'Стол был остановлен'
    setTime('db/competitions.db', now_time, "end_time")
    setStatus('db/competitions.db',table_status, "status_table")
    bot.send_message(message.chat.id, f'<em> Стол был остановлен! Пускай ваши печени отдохнут! </em>' + '\U0001F600\n', parse_mode='html', )


bot.polling(none_stop=True)