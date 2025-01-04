# coding=utf-8
import telebot

bot = telebot.TeleBot('7683114432:AAFVvcorMdZ9vRRes8VIhkME0esyXjb8uCk')

@bot.message_handler(commands=['привет', 'старт']) # можно добавить несколько команд
def main(message):
    bot.send_message(message.chat.id, 'Hello', parse_mode='html')

@bot.message_handler(commands=['помощь'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')

bot.polling(none_stop=True)