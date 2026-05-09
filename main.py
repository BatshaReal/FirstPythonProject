import telebot
import random
    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("3SUPER3RARE3TOKEN3")

from telebot import types
my_bg = types.BackgroundFillSolid(type='solid', color='#FF0000')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
        
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['monetka'])
def send_monetka(message):
    side = random.randint(0,1)
    if side == 0:
        result = "Орел"
    else:
        result = "Решка"
    answer = f"Привет!,{result}"
    bot.reply_to(message, answer)

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
        
bot.polling()   
