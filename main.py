import telebot
import random
    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("3SUPER3RARE3TOKEN3")

from telebot import types
my_bg = types.BackgroundFillSolid(type='solid', color='#FF0000')

@bot.message_handler(commands=['Рассказ'])
def story_start(message):
    msg = bot.reply_to(message, "Как зовут героя?")
    bot.register_next_step_handler(msg, get_hero_name)

def get_hero_name(message):
    hero = message.text
    msg = bot.reply_to(message, "Как называется рассказ?")
    bot.register_next_step_handler(msg, get_story_name, hero)

def get_story_name(message, hero):
    name = message.text
    story = f"{name} давным давно жил {hero}, конец"
    bot.reply_to(message, story)

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
bot.polling()   
