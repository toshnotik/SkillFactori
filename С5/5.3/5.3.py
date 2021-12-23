import telebot

TOKEN = '5054930849:AAElsLloH__O7RiXD74CvBmAP_RW1LSXWAU'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['voice', ])
def function_name(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Найс че')


bot.polling(none_stop=True)