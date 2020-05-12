#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import confuse
import telebot
import urllib.request
from random import randrange
from bs4 import BeautifulSoup

project_root = os.path.dirname(os.path.abspath("config.yaml"))
os.environ["FASHOKDIR"] = project_root

config = confuse.Configuration("FASHOK")

bot = telebot.TeleBot(config["tg"]["key"].get())

stickers_default = [
    'CAACAgIAAxkBAAINYV66o4YQsaPtfqKPstL55hbQ3-6gAAJmAAOYv4AN1IPYVX9YoHYZBA'
]
stickers_cute = [
    'CAACAgIAAxkBAAINKF66oVftc0cFlbqcVyZzdW-DBOHQAALUAgAC8-O-C3RUzl7G7VKUGQQ',
]
stickers_kokoko = [
    'CAACAgIAAxkBAAINIF66kEOid_RSdA50bWtwGg_kCfkUAAKDAAPZvGoaufCQFV46-dEZBA',
    'CAACAgIAAxkBAAINUl66oqRZIPTR1HTMuYsYmJKc-vg1AAJ7AAPZvGoa8cCtoxKmeegZBA',
    'CAACAgIAAxkBAAINVV66oqwQOfwGsFlNPNG0i7SUt9a3AAKOAAPZvGoa0XxPL40T-j0ZBA',
    'CAACAgIAAxkBAAINWF66orNr1yUgIUMHrrQXYF5V89ETAAKTAAPZvGoaBnATSS-CnncZBA',
    'CAACAgIAAxkBAAINW166or7mTEFwzV7ZUAxjfAmry6J6AAKCAAPZvGoaos83cjAej3EZBA',
    'CAACAgIAAxkBAAINXl66osnCl_y4lafLZGyXybPrgbXWAAJ8AAPZvGoaUnAlnI5pxGUZBA',
]
stickers_ziga = [
    'CAACAgIAAxkBAAINI166kQ98cAJyrDtTuClvGwTPdK5TAAIyAgACIe27A7t3RiEkcvv0GQQ',
    'CAACAgIAAxkBAAINLl66ok0FHFWb4YrTclVS7FP523I5AAIsAgACIe27A9EC3YftHgltGQQ',
    'CAACAgIAAxkBAAINNF66ol_JNUTTLXIBjyfXGgeq6UjOAALPAwACIe27A8giYHfiMUXrGQQ',
    'CAACAgIAAxkBAAINN166omupfXqV6-2jyRVJF_ACSOUsAALlAwACIe27A2VQPv6HfysxGQQ',
    'CAACAgIAAxkBAAINSV66ooAH8PF6LzZWo2OtPDDAzA5SAAMIAAIh7bsDAXJf5pCdo1MZBA',
    'CAACAgIAAxkBAAINTF66oodgFNqNc-K7vKv28s12ly8qAAK6BwACIe27A4CI0z4kps-2GQQ',
    'CAACAgIAAxkBAAINT166opBB1eVMdkeR4TSBX1WhJRziAALhAwACIe27A5vZve5nFsFWGQQ',
]


def generate_answer(event, user, message):
    out = []
    if event == "start":
        out = "Привет! Меня зовут Фашок! Я альтер эго Сашка! Давай общаться!"
        return out

    user_id = user.id

    if user_id == 99760649:
        out.append("Сашок!")
        page = urllib.request.urlopen(config["resources"]["quotes"].get()).read().decode("utf-8")
        soup = BeautifulSoup(page, "html.parser")
        out.append(soup.find(id="saying").find("td").text.replace('—', ' — '))
    elif user_id == 493041312:  # Димас
        out.append("Димасик, дорогой!")
        page = urllib.request.urlopen(config["resources"]["quotes"].get()).read().decode("utf-8")
        soup = BeautifulSoup(page, "html.parser")
        out.append(soup.find(id="saying").find("td").text.replace('—', ' — '))
    elif user_id == 430452197:  # Алексей
        out.append("Лешка, милый, хороший мой Лешка!")
        page = urllib.request.urlopen(config["resources"]["quotes"].get()).read().decode("utf-8")
        soup = BeautifulSoup(page, "html.parser")
        out.append(soup.find(id="saying").find("td").text.replace('—', ' — '))
    else:
        out.append("Кажется, я Вас не знаю. Не люблю разговаривать с незнакомцами.")

    return out


def generate_sticker(user):
    sticker = ""

    user_id = user.id
    if user_id == 99760649:
        sticker = stickers_cute[randrange(0, len(stickers_cute))]
    elif user_id == 493041312:  # Димас
        sticker = stickers_kokoko[randrange(0, len(stickers_kokoko))]
    elif user_id == 430452197:  # Алексей
        sticker = stickers_ziga[randrange(0, len(stickers_ziga))]
    else:
        sticker = stickers_default[randrange(0, len(stickers_default))]

    return sticker


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, generate_answer("start", message.from_user, ""))


@bot.message_handler(content_types=["text"])
def send_text(message):
    user_message = message.text.lower().encode("utf-8")
    msgs = generate_answer("chat", message.from_user, user_message)
    for msg in msgs:
        bot.send_message(message.chat.id, msg)

    bot.send_sticker(message.chat.id, generate_sticker(message.from_user))


bot.polling()
