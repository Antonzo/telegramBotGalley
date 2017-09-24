import config
import telebot
import time

bot = telebot.TeleBot(config.token)

audio = open('/home/kaptch/Downloads/oceanman.mp3', 'rb')

prevOceanman = time.time()


@bot.message_handler(commands=['oceanman'])
def answer_all_msg(message):
    global prevOceanman
    if time.time() - prevOceanman > 10:
        bot.send_audio(message.chat.id, audio)
        prevOceanman = time.time()


@bot.message_handler(commands=['help'])
def answer_all_msg(message):
    bot.send_message(message.chat.id, '/help - справка\n'
                                      '/oceanman - отправить оушенмена\n'
                                      '/reported - нет\n')


@bot.message_handler(commands=['reported'])
def answer_all_msg(message):
    bot.send_message(message.chat.id, ('Нет @' + message.user.username))
    bot.delete_message(message.chat.id, message)


if __name__ == '__main__':
    bot.polling(none_stop=True)
