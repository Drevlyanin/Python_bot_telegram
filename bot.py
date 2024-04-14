import telebot
import webbrowser

bot = telebot.TeleBot('')

@bot.message_handler(comands=['site', 'website'])
def site(message):
    webbrowser.open('https://github.com/Drevlyanin/Drevlyanin')


@bot.message_handler(commands=['start', 'main', 'hello',])
def main(message):
    bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)

bot = telebot.TeleBot('6003923785:AAFqVJaZnBSNoTPLNUzXZZqb_mQ6Z1kEv5o')


@bot.message_handler(comands=['site', 'website'])
def site(message):
    webbrowser.open('https://github.com/Drevlyanin/Drevlyanin')


@bot.message_handler(commands=['start', 'main', 'hello',])
def main(message):
    bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)
