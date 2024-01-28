import telebot
import types
import time
from photos import *
from texts import *
from buttons import (
FIRST_QUESTION,
SECOND_QUESTION,
THERD_QUESTION,
FORTH_QUESTION,
FIFTH_QUESTION,
SIXTH_QUESTION
)
bot = telebot.TeleBot(token="6553315261:AAGxCUTqGfce74Lsq1omWDTvhq2fCWLeqLM")

all_right = ""

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать, это бот с помощью которого можно закрепить свои знания о планетах")
    time.sleep(0.5)
    bot.send_message(message.chat.id, "Напишите /starting для начала")

@bot.message_handler(commands=["starting"])
def starting(message):
    bot.send_photo(message.chat.id, photo=photo1, caption=text1, reply_markup=FIRST_QUESTION)

@bot.message_handler(commands=["admin"])
def password(message):
    bot.send_message(message.chat.id, "Введите admin-пароль")
    bot.register_next_step_handler(message, hozain)
def hozain(message):
    if message.text == "321":
        bot.send_sticker(message.chat.id, "CAACAgQAAxkBAAELRCRltqz8iQO_zfR_9AsRNSKer4-RlgACTQ4AApY7AAFQaesqqBlP5es0BA")
        bot.send_message(message.chat.id, "К вашим услугам, сер")
    else:
        bot.send_message(message.chat.id, "Эта функция доступна только для администраторов")

@bot.callback_query_handler(func=lambda call: call.data == "wrong")
def text_wrong(call):
    bot.send_message(call.message.chat.id, "Попробуй еще раз, напиши /starting чтобы продолжить")


@bot.callback_query_handler(func=lambda call: call.data.startswith("correct"))
def correct(call):
    bot.send_message(call.message.chat.id, "Моледец правильно")
    time.sleep(0.5)
    _, name = call.data.split("_")
    if name == "earth":
        bot.send_photo(call.message.chat.id, photo=photo2, caption=text1, reply_markup=SECOND_QUESTION)
    elif name == "upiter":
        bot.send_photo(call.message.chat.id, photo=photo3, caption=text1, reply_markup=THERD_QUESTION)
    elif name == "mercury":
        bot.send_photo(call.message.chat.id, photo=photo4, caption=text1, reply_markup=FORTH_QUESTION)
    elif name == "saturn":
        bot.send_photo(call.message.chat.id, photo=photo5, caption=text1, reply_markup=FIFTH_QUESTION)
    elif name == "neptun":
        bot.send_photo(call.message.chat.id, photo=photo6, caption=text1, reply_markup=SIXTH_QUESTION)
    elif name == "mars":
        bot.send_message(call.message.chat.id,
                         "Ты все отгадал верно. Отправь друзьям, чтобы тоже знали название всех планет")


bot.polling(none_stop=True)
