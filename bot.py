import telebot
from telebot import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import re


bot = telebot.TeleBot('TOKEN')
YOOTOKEN = "YOOTOKEN"
amount = 200
pay_person = 0



@bot.message_handler(commands=['start'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Привет! Я бот легорона и сейчас ты узнаешь зачем ты здесь")
    bot.send_message(message.from_user.id, "Ты хочешь купить билет и получить шанс выиграть крутой набор! (Подробности и дата проведения розыгрыша в моем основном телеграмм канале: https://t.me/Legoron")

    bot.send_message(message.from_user.id, "Дело в том что я с подаркомИменно с розыгрышом И ты можешь принять участие")
    bot.send_message(message.from_user.id, "Напиши: /surprise). И я всё раскажу")
    
@bot.message_handler(commands=['surprise'])
def surprise(message):
    bot.send_message(message.from_user.id, "Цена одного билета: 200₽")
    bot.send_message(message.from_user.id, "❗️После того как ты оплатишь билет, тебе выдадут твой спец номер, он будет виден в общей таблице в моем основном телеграмм канале, и мне")
    bot.send_message(message.from_user.id, "Только учитывай, что розыгрыш производится только по России, если тебе нужна будет доставка в другую страну, то пожалуйста закрой этого бота. В случае если ты в другой стране и купил билет, то доставка тебе осуществлена не будет ❗️")
    bot.send_message(message.from_user.id, "Я выберу победителя на прямом эфире в своём Инстаграмм канале ( https://instagram.com/lego_rons?utm_medium=copy_link ) — ——— в —:— Там можешь быть и ты")
    bot.send_message(message.from_user.id, "P.s в этот раз я буду использовать систему доставки, по этому не будет ситуации как с моим самым первым бесплатным розыгрышем")
    bot.send_message(message.from_user.id, "Напиши « /cherished_ticket » и ты сможешь купить билет!")




'''@bot.message_handler(commands=['cherished_ticket'])
def cherished_ticket(message : types.Message):
    menu1 = telebot.types.InlineKeyboardMarkup()
    menu1.add(telebot.types.InlineKeyboardButton(text = 'Купить билет', callback_data ='pay'))
    bot.send_message(message.from_user.id, "Купить Билет", reply_markup = 'pay')'''


@bot.message_handler(commands=['cherished_ticket'])
def step1(message):
    menu1 = telebot.types.InlineKeyboardMarkup()
    menu1.add(telebot.types.InlineKeyboardButton(text = 'Купить Билет', callback_data ='pay'))
    bot.send_message(message.chat.id, text ='Купить Билет', reply_markup = menu1)
    
    

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
  if call.data == 'pay':
    
    bot.send_invoice(call.from_user.id, title='Working Time Machine',
                     description='Нажми на кнопку и поолучи свой билетик!',
                     provider_token=YOOTOKEN,
                     currency='RUB',
                     is_flexible=False,  # True If you need to set up Shipping Fee
                     prices = [types.LabeledPrice(label='Покупка билетов', amount=15000), 
                     types.LabeledPrice('Покупка билетов', 000)],
                     start_parameter='time-machine-example',
                     invoice_payload='HAPPY FRIDAYS COUPON')
  
                     
                    


@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message="Похоже что то пошло не так, попробуй снова и поешь твикса;)🍫")

@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    global  pay_person 
    bot.send_message(message.chat.id, 'Вот твой Билетик:')
    k = 0
    while True:
        numG = random.randint(100000, 999999)
        numQ = random.randint(100000, 999999)

        k += 1
        if numQ == numG:
            print("Номер заказа {} ".format(k, numG, numQ))
            print(message.chat.first_name, ', ', message.chat.last_name, ', ', 'ID пользывателя: ', message.chat.id)
            pay_person=pay_person+1
            print("Получили билеты: ", pay_person)
            break

    
    bot.send_message(message.chat.id, "Номер заказа {} ".format(k, numG, numQ))
    bot.send_message(message.chat.id, 'Спасибо тебе! Если захочешь купить снова напиши эту каманду снова(/cherished_ticket)')
                                       
                     
 


   
    
     
    







    
bot.infinity_polling(skip_pending = True)
