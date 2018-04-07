
import telebot
from telebot import types


token = "531902020:AAEMppKRGhwq0zFfWOT4lG_QrHtj0cOsk2w"
bot = telebot.TeleBot(token)




def log(message, answer):
    print("/n ------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст = {3}".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text))
@bot.message_handler(commands=['start'])
def handle_text(message):
        answer = 'Приветствую!'
        log(message, answer)
        markup = types.ReplyKeyboardMarkup(row_width=1)
        itembtn1 = types.KeyboardButton('Кек')
        itembtn2 = types.KeyboardButton('Лол')
        itembtn3 = types.KeyboardButton('Пойти на хуй')
        markup.add(itembtn1, itembtn2, itembtn3)
        bot.send_message(message.from_user.id, answer, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
 if message.text == "Пойти на хуй":
    answer = "Пидор, иди на хуй!"
    log(message, answer)
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, answer, reply_markup=markup)


 if message.text == "Кек":
    answer = "Лол"
    log(message, answer)
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, answer, reply_markup=markup)

 if message.text == "Лол":
    answer = "Кек"
    log(message, answer)
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, answer, reply_markup=markup)

bot.polling(none_stop=True)