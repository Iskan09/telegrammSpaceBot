import telebot
from telebot import types
from random import randint



FIRST_QUESTION = types.InlineKeyboardMarkup()
button1_1 = types.InlineKeyboardButton("Земля", callback_data = "correct_earth")
button1_2 = types.InlineKeyboardButton("Марс", callback_data = "wrong")
button1_3 = types.InlineKeyboardButton("Нептун", callback_data = "wrong")
FIRST_QUESTION.add(button1_1, button1_2, button1_3)

SECOND_QUESTION = types.InlineKeyboardMarkup()
button2_1 = types.InlineKeyboardButton("Луна", callback_data= "wrong")
button2_2 = types.InlineKeyboardButton("Юпитер", callback_data="correct_upiter")
button2_3 = types.InlineKeyboardButton("Нептун", callback_data="wrong")
SECOND_QUESTION.add(button2_1, button2_2, button2_3)

THERD_QUESTION = types.InlineKeyboardMarkup()
button3_1 = types.InlineKeyboardButton("Уран", callback_data= "wrong")
button3_2 = types.InlineKeyboardButton("Меркурий", callback_data="correct_mercury")
button3_3 = types.InlineKeyboardButton("Венера", callback_data="wrong")
THERD_QUESTION.add(button3_1, button3_2, button3_3)

FORTH_QUESTION = types.InlineKeyboardMarkup()
button4_1 = types.InlineKeyboardButton("Венера", callback_data="wrong")
button4_2 = types.InlineKeyboardButton("Сатурн", callback_data="correct_saturn")
button4_3 = types.InlineKeyboardButton("Нептун", callback_data="wrong")
FORTH_QUESTION.add( button4_2, button4_1, button4_3)

FIFTH_QUESTION = types.InlineKeyboardMarkup()
button5_1 = types.InlineKeyboardButton("Венера", callback_data= "wrong")
button5_2 = types.InlineKeyboardButton("Сатурн", callback_data="wrong")
button5_3 = types.InlineKeyboardButton("Нептун", callback_data="correct_neptun")
FIFTH_QUESTION.add(button5_3, button5_2, button5_1)

SIXTH_QUESTION = types.InlineKeyboardMarkup()
button6_1 = types.InlineKeyboardButton("Венера", callback_data="wrong")
button6_2 = types.InlineKeyboardButton("Плутон", callback_data="wrong")
button6_3 = types.InlineKeyboardButton("Марс", callback_data="correct_mars")
SIXTH_QUESTION.add(button6_2, button6_1, button6_3)
