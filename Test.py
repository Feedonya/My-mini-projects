import time
import telebot

current_time = time.strftime("%H", time.localtime())
bot = telebot.TeleBot('6492062271:AAE8udSu_wrK1kahYXPKjwkyK6btRjUq1GM')
chat_id = "@+Y7TMoRlHIQgzZjUy"

@bot.message_handler(func= lambda message: message.text == "Доброе утро")
def answer(message):
    bot.send_photo(message.chat=chat_id, photo="https://fussiecat.com/wp-content/uploads/2019/06/friends-1568x1045.jpg", caption="Доброе утро, котеночек")

@bot.message_handler(func= lambda current_time: current_time == "09")
def morning(message):
    bot.send_message(message.chat.id=chat_id, "Доброе утро, котики")

@bot.message_handler(func= lambda current_time: current_time == "22")
def night(message):
    bot.send_message(message.chat.id, "Спокойной ночи, котики")


@bot.message_handler(func= lambda current_time: current_time == "01")
def test(message):
    bot.send_message(message, "Спокойной ночи, котики")


"""
@bot.message_handler()
def time_send(message):
    if current_time == current_time: 
        bot.send_message(message.chat.mIxhpLJ8, 'Доброй ночи, котики!')
    elif current_time == "9:00:":
            bot.send_message(message.chat.mIxhpLJ8, 'Доброе утро, котики!')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
"""

bot.polling()