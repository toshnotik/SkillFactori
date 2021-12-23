import telebot

TOKEN = '5054930849:AAElsLloH__O7RiXD74CvBmAP_RW1LSXWAU'
bot = telebot.TeleBot(TOKEN)

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, f'Здороф, {message.chat.username}')

@bot.message_handler(content_types=['photo', ])
def function_mems(message: telebot.types.Message):
    bot.reply_to(message, f'Nice meme XDD')

@bot.message_handler(content_types=['voice', ])
def function_name(message: telebot.types.Message):
    bot.send_message(message.chat.id, f'Эй, {message.chat.username} \n Найс че')


bot.polling(none_stop=True)