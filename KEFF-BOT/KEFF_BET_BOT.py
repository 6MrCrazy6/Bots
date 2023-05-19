import telebot

bot = telebot.TeleBot('5422750153:AAFv8JyVkdl_NGISRhHecBV7T5qkdokeaqU')

@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, f'Вас приветсвует KEFF-BET! {user_name}, здесь вы можете выбрать одну из услуг!')
    bot.send_message(message.chat.id, f'Какая услуга вас интересует?  \n'
                                      f'Fast - 50грн \n'
                                      f'Individual - 100грн \n'
                                      f'Individual PRO - 150грн \n')

@bot.message_handler(content_types=["text"])
def text(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if message.text == 'Fast':
            bot.send_message(chat_id, "Заявка отправлена!")
            bot.register_next_step_handler(message,send_message)
        if message.text == 'Individual':
            bot.send_message(chat_id, "Заявка отправлена!")
            bot.register_next_step_handler(message,send_message)
        if message.text == 'Individual PRO':
            bot.send_message(chat_id, "Заявка отправлена!")
            bot.register_next_step_handler(message,send_message)


def send_message(message):
    first_name = message.chat.first_name
    username = message.chat.username
    user_text = message.text
    admin_id = 983005240
    app_text = []
    app_name = []
    app_username = []
    app_name.append(first_name)
    app_username.append(username)
    app_text.append(user_text)
    bot.send_message(admin_id, f"Поступила заявка от {app_name[0]} \n"
                               f"Его username = @{username} \n"
                               f"Его текст: \n"
                               f"{app_text[0]}")
    app_text.clear()
    app_username.clear()
    app_name.clear()


bot.polling(none_stop=True)
