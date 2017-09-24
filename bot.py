import config
import telebot
import time

bot = telebot.TeleBot(config.token)

audio = open('./assets/oceanman.mp3', 'rb')

prevOceanman = time.time()


@bot.message_handler(commands=['oceanman'])
def oceanman_msg(message):
    global prevOceanman
    if time.time() - prevOceanman > 10:
        bot.send_audio(message.chat.id, audio)
        prevOceanman = time.time()


@bot.message_handler(commands=['help'])
def help_msg(message):
    bot.send_message(message.chat.id, '/help - справка\n'
                                      '/oceanman - отправить оушенмена\n'
                                      '/reported - нет\n')


@bot.message_handler(commands=['reported'])
def reported_msg(message):
    bot.send_message(message.chat.id, ('Нет @' + message.user.username))
    bot.delete_message(message.chat.id, message)

@bot.message_handler(commands=['sendreported'])
def send_reported_msg(message):
    bot.send_message(message.chat.id, ('/reported'))
    bot.delete_message(message.chat.id, message)

if __name__ == '__main__':
    bot.polling(none_stop=True)
