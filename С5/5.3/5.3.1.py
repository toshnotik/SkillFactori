import telebot

TOKEN = '5054930849:AAElsLloH__O7RiXD74CvBmAP_RW1LSXWAU'
bot = telebot.TeleBot(TOKEN)

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass


@bot.message_handler(content_types=['voice', ])
def function_name(message: telebot.types.Message):
    bot.send_message(message.chat.id, f'Эй, {message.chat.username} \n Найс че')


bot.polling(none_stop=True)