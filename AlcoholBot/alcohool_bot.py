import random
import telebot
from dbWorker import *
from dbWorker2 import *

bot = telebot.TeleBot('TOKEN')
prepareDb('db/database.db')
prepareDb2('db/database2.db')


@bot.message_handler(commands=['start'])
def start(message):
    init_user('db/database.db', message.from_user.first_name)
    init_user1('db/database2.db', message.from_user.first_name)
    bot.send_message(message.chat.id, 'Приветствую в баре! Чего желаете?')
    bot.send_message(message.chat.id, 'Список алкогольных напитков - /listalcoholdrinks \n'
                                      'Список безалкогольных напитков - /listnonalcoholdrinks\n')

@bot.message_handler(commands=['listalcoholdrinks'])
def listalcoholdrink(message):
    init_user('db/database.db', message.from_user.first_name)
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
                                      'Мохито - /drinkmojito \n')

@bot.message_handler(commands=['listnonalcoholdrinks'])
def listnonalcoholdrinks(message):
    init_user1('db/database2.db', message.from_user.first_name)
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
    bot.send_message(message.chat.id, f'<em>{user_name}, минута еще не прошла!', parse_mode='html')
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л пива.</em>'+'\U0001F37A \n'
                                            f'Всего вы выпили - {summ_litres} л пива', parse_mode='html')
    setLitres('db/database.db', user_name, "beer", summ_litres)

@bot.message_handler(commands=['drinkwine'])
def drinkwine(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "wine")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л вина.'+'\U0001F377 \n'
                                    f'Всего вы выпили - {summ_litres} л вина </em>\n', parse_mode='html')
    setLitres('db/database.db', user_name, "wine", summ_litres)

@bot.message_handler(commands=['drinkvodka'])
def drinkvodka(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "vodka")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л водки.'+'\U0001F376\U0001F321 \n'
                                    f'Всего вы выпили - {summ_litres} л водки </em>\n', parse_mode='html')
    setLitres('db/database.db', user_name, "vodka", summ_litres)

@bot.message_handler(commands=['drinkwhiskey'])
def drinkwhiskey(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "whiskey")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л виски.'+'\U0001F943 \n'
                                    f'Всего вы выпили - {summ_litres} л виски </em>\n', parse_mode='html')
    setLitres('db/database.db', user_name, "whiskey", summ_litres)

@bot.message_handler(commands=['drinkcognac'])
def drinkcognac(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "cognac")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л коньяку.'+'\U0001F943\U0001F9CA \n'
                                    f'Всего вы выпили - {summ_litres} л коньяка </em>\n', parse_mode='html')
    setLitres('db/database.db', user_name, "cognac", summ_litres)

@bot.message_handler(commands=['drinkmulledwine'])
def drinkmulledwine(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "mulledwine")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л глинтвейна.'+'\U00002615\U0001F377 \n'
                                    f'Всего вы выпили - {summ_litres} л глинтвейна </em>\n', parse_mode='html')
    setLitres('db/database.db', user_name, "mulledwine", summ_litres)

@bot.message_handler(commands=['drinksake'])
def drinksake(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "sake")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л саке.'+'\U0001F376	\n'
                                    f'Всего вы выпили - {summ_litres} л саке </em>\n', parse_mode='html')
    setLitres('db/database.db', user_name, "sake", summ_litres)

@bot.message_handler(commands=['drinktequila'])
def drinktequila(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "tequila")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л текилы.'+'\U0001F378\U0001F335\n'
                                      f'Всего вы выпили - {summ_litres} л текилы </em>\n', parse_mode='html')
    setLitres('db/database.db', user_name, "tequila", summ_litres)

@bot.message_handler(commands=['drinkmojito'])
def drinkmojito(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "mojito")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л мохито.'+'\U0001F378\U0001F335\n'
                                      f'Всего вы выпили - {summ_litres} л мохито </em>\n', parse_mode='html')
    setLitres('db/database.db', user_name, "mojito", summ_litres)

@bot.message_handler(commands=['drinkpinacolada'])
def drinkpinacolada(message):
    init_user('db/database.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres('db/database.db', user_name, "pinacolada")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em> {user_name}, вы выпили - {randomize} л пина колады.'+'\U0001F943\U0001F34D\U0001F965\n'
                                      f'Всего вы выпили - {summ_litres} л пина колады </em>\n', parse_mode='html')
    setLitres('db/database.db', user_name, "pinacolada", summ_litres)

@bot.message_handler(commands=['drinktea'])
def drinktea(message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "tea")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л чая.</em>'+'\U0001F375 \n'
                                    f'Всего вы выпили - {summ_litres} л чаю', parse_mode='html')
    setLitres2('db/database2.db', user_name, "tea", summ_litres)

@bot.message_handler(commands=['drinkcoffe'])
def drinkcoffe(message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "coffe")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л коффе.</em>'+'\U00002615 \n'
                                    f'Всего вы выпили - {summ_litres} л коффе', parse_mode='html')
    setLitres2('db/database2.db', user_name, "coffe", summ_litres)

@bot.message_handler(commands=['drinkbubbletea'])
def drinkbubbletea(message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "bubbletea")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л бабл ти.</em>'+'\U0001F9CB \n'
                                    f'Всего вы выпили - {summ_litres} л бабл ти', parse_mode='html')
    setLitres2('db/database2.db', user_name, "bubbletea", summ_litres)

@bot.message_handler(commands=['drinkcocacola'])
def drinkcocacola (message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "cocacola")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л кока-колы.</em>'+'\U0001F534\U000026AA \n'
                                    f'Всего вы выпили - {summ_litres} л кока-колы', parse_mode='html')
    setLitres2('db/database2.db', user_name, "cocacola", summ_litres)

@bot.message_handler(commands=['drinkfruitdrink'])
def drinkfruitdrink (message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "fruitdrink")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л морса.</em>'+'\U0001F379	 \n'
                                    f'Всего вы выпили - {summ_litres} л морса', parse_mode='html')
    setLitres2('db/database2.db', user_name, "fruitdrink", summ_litres)

@bot.message_handler(commands=['drinkmilkshake'])
def drinkmilkshake (message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "milkshake")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л молочного коктейля.</em>'+'\U0001F95B \n'
                                    f'Всего вы выпили - {summ_litres} л молочного коктейля', parse_mode='html')
    setLitres2('db/database2.db', user_name, "milkshake", summ_litres)

@bot.message_handler(commands=['drinksprite'])
def drinksprite (message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "sprite")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л спрайта.</em>'+'\U0001F7E2 \n'
                                    f'Всего вы выпили - {summ_litres} л спрайта', parse_mode='html')
    setLitres2('db/database2.db', user_name, "sprite", summ_litres)

@bot.message_handler(commands=['drinkfanta'])
def drinkfanta (message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "fanta")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л фанты.</em>'+'\U0001F7E0	\n'
                                    f'Всего вы выпили - {summ_litres} л фанты', parse_mode='html')
    setLitres2('db/database2.db', user_name, "fanta", summ_litres)

@bot.message_handler(commands=['drinknonalcoholicbeer'])
def drinknonalcoholicbeer (message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "nonalcoholicbeer")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л безалкогольного пива.</em>'+'\U0001F37B \n'
                                    f'Всего вы выпили - {summ_litres} л безалкогольного пива', parse_mode='html')
    setLitres2('db/database2.db', user_name, "nonalcoholicbeer", summ_litres)

@bot.message_handler(commands=['drinknonalcoholicmojito'])
def drinknonalcoholicmojito(message):
    init_user1('db/database2.db', message.from_user.first_name)
    user_name = message.from_user.first_name
    currentLitres = getLitres2('db/database2.db', user_name, "nonalcoholicmojito")
    randomize = random.randint(1, 16)
    summ_litres = currentLitres + randomize
    bot.send_message(message.chat.id, f'<em>{user_name}, вы выпили - {randomize} л безалкогольного мохито.</em>'+'\U0001F378\U0001F335\n'
                                    f'Всего вы выпили - {summ_litres} л безалкогольного мохито', parse_mode='html')
    setLitres2('db/database2.db', user_name, "nonalcoholicmojito", summ_litres)

bot.polling(none_stop=True)
