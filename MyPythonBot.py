# coding=utf-8
import telebot
import webbrowser

bot = telebot.TeleBot('7683114432:AAFVvcorMdZ9vRRes8VIhkME0esyXjb8uCk')

# Start
@bot.message_handler(commands=['hello', 'start', 'привет', 'старт']) # можно добавить несколько команд
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nДобро пожаловать в лучшего бота для скачивания контента из интернета. Что ж, начнём?', parse_mode='html')

# Help
@bot.message_handler(commands=['help', 'помощь'])
def help(message):
    bot.send_message(message.chat.id, '<b>Помощь с использованием:</b>\n' +
                    'Список команд\n' +
                    '<i>\start</i> - начать пользоваться ботом\n' +
                    '<i>\site</i> - открыть ссылку на мой сайт (allArticles)\n' +
                    '<i>\help</i> - помощь в навигации по боту', parse_mode='html')

# Перекидывает на мой сайт
@bot.message_handler(commands=['site', 'website', 'сайт', 'вебсайт', 'веб-сайт'])
def site(message):
    webbrowser.open('https://all-articles.onrender.com/')

# Выдаёт айдишник юзера
@bot.message_handler(commands=['id', 'ID', 'Id', 'iD'])
def id(message):
    bot.reply_to(message, f'Твой ID в Telegram: <b>{message.from_user.id}</b>', parse_mode='html')

# @bot.message_handler()
# def info(message):
#     if message.text.lower == 'приветы':
#         bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nДобро пожаловать в лучшего бота для скачивания контента из интернета. Что ж, начнём?', parse_mode='html')
#     else:
#         bot.send_message(message.chat.id, 'Не понял твоего сообщения! Давай лучше общаться командами.')

bot.polling(none_stop=True)