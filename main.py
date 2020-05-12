#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import confuse
import telebot

project_root = os.path.dirname(os.path.abspath("config.yaml"))
os.environ["FASHOKDIR"] = project_root

config = confuse.Configuration("FASHOK")

bot = telebot.TeleBot(config["tg"]["key"].get())


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Меня зовут Фашок! Я альтер эго Сашка! Давай общаться!")

    user_id = message.from_user.id

    if user_id == 99760649:
        bot.send_message(message.chat.id, "Привет, создатель!")
    elif user_id == 493041312:
        bot.send_message(message.chat.id, "ДИМОООН!")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAINIF66kEOid_RSdA50bWtwGg_kCfkUAAKDAAPZvGoaufCQFV46-dEZBA')
    elif user_id == 430452197:
        bot.send_message(message.chat.id, "Рад видеть тебя, Лешка!")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAINI166kQ98cAJyrDtTuClvGwTPdK5TAAIyAgACIe27A7t3RiEkcvv0GQQ')
    else:
        bot.send_message(message.chat.id, "Кажется, мы с Вами еще не знакомы? А я не говорю с незнакомцами.")


@bot.message_handler(content_types=["text"])
def send_text(message):
    username = message.from_user.username.lower()
    user_id = message.from_user.id
    user_message = message.text.lower().encode("utf-8")

    if user_id == 99760649:
        bot.send_message(message.chat.id, "Привет, создатель!")
    elif user_id == 493041312:
        bot.send_message(message.chat.id, "ДИМОООН!")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAINIF66kEOid_RSdA50bWtwGg_kCfkUAAKDAAPZvGoaufCQFV46-dEZBA')
    elif user_id == 430452197:
        bot.send_message(message.chat.id, "Рад видеть тебя, Лешка!")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAINI166kQ98cAJyrDtTuClvGwTPdK5TAAIyAgACIe27A7t3RiEkcvv0GQQ')
    else:
        bot.send_message(message.chat.id, "Кажется, мы с Вами еще не знакомы? А я не говорю с незнакомцами.")


bot.polling()