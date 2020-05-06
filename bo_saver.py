#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
from telebot import types

bot = telebot.TeleBot('token')
name = ''
surname = ''
age = ''

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hey what's up? Let's type the /reg")
        bot.register_next_step_handler(message, start)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Let's write 'Hi'")
    else:
        bot.send_message(message.from_user.id, "I do not understand u let's try /help.")

# @bot.message_handler(content_types=['text'])
def start (message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "What is ur name, bro?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, "Let's write /reg")
        bot.register_next_step_handler(message, start)
def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'What is ur surname, bro?')
    bot.register_next_step_handler(message, get_sname)
def get_sname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'How old are u?')
    bot.register_next_step_handler(message, get_age)
def get_age(message):
    global age
    if (message.text.isdigit()):
        age = int(message.text)
    else:
        bot.send_message(message.from_user.id, "Let's use the digits, maan") 
        bot.register_next_step_handler(message, get_age)
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Yes', callback_data = 'yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='No', callback_data = 'no')
    keyboard.add(key_no)
    question = 'U are ' + str(age) + ' years old. Can I call u ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global age
    if call.data =='yes':
        bot.send_message(call.message.chat.id, "I'm going to remember")
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Let's type the /reg again")
        age = 0
        
bot.polling(none_stop=True, interval=0)