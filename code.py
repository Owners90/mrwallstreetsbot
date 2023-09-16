#!/usr/bin/env python
# coding: utf-8

# # Import libraries

# In[1]:


import telebot
from telebot import types
import json
import time
import schedule
import threading
import os


# # Bot API

# In[2]:


bot = telebot.TeleBot('6259258184:AAGFx2lAKJNcvBch3DDfpYGFagde5xb1WHg')


# # Create admin buttons

# In[3]:


btn1 = telebot.types.KeyboardButton("اضافة عميل")
btn2 = telebot.types.KeyboardButton("تعديل اشتراك عميل")
btn3 = telebot.types.KeyboardButton("تعديل اخر الاخبار")
btn4 = telebot.types.KeyboardButton("تعديل سهم اليوم")
btn5 = telebot.types.KeyboardButton("تعديل AI")
btn6 = telebot.types.KeyboardButton("تعديل جدول الدعم والمقاومة")
btn7 = telebot.types.KeyboardButton("تعديل الزخم")
btn8 = telebot.types.KeyboardButton("تعديل التقرير اليومي")
btn9 = telebot.types.KeyboardButton("ارسال رسالة")
keyboard_admin = telebot.types.ReplyKeyboardMarkup(row_width=3,selective=True ,one_time_keyboard=True)
keyboard_admin.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)


# when admin click on "تعديل سهم اليوم" - "تعديل الدعم والمقاومة" - "تعديل الزخم"
btn1 = telebot.types.KeyboardButton("نص فقط")
btn2 = telebot.types.KeyboardButton("نص وصورة")
btn3 = telebot.types.KeyboardButton("القائمة الرئيسية")
keyboard_admin_text_pic = telebot.types.ReplyKeyboardMarkup(row_width=3,selective=True ,one_time_keyboard=True)
keyboard_admin_text_pic.add(btn1, btn2, btn3)


# when admin click on "ارسال رسالة"
btn1 = telebot.types.KeyboardButton("للعملاء الحالبين")
btn2 = telebot.types.KeyboardButton("لكل العملاء")
btn3 = telebot.types.KeyboardButton("القائمة الرئيسية")
keyboard_admin_send_msg = telebot.types.ReplyKeyboardMarkup(row_width=3,selective=True ,one_time_keyboard=True)
keyboard_admin_send_msg.add(btn1, btn2, btn3)

# when admin click on "تعديل AI"
btn1 = telebot.types.KeyboardButton("SPX")
btn2 = telebot.types.KeyboardButton("QQQ")
btn3 = telebot.types.KeyboardButton("AAPL")
btn4 = telebot.types.KeyboardButton("MSFT")
btn5 = telebot.types.KeyboardButton("TSLA")
btn6 = telebot.types.KeyboardButton("NVDA")
btn7 = telebot.types.KeyboardButton("AMZN")
btn8 = telebot.types.KeyboardButton("META")
btn9 = telebot.types.KeyboardButton("GOOGL")
btn10 = telebot.types.KeyboardButton("AMD")
btn11 = telebot.types.KeyboardButton("SHOP")
btn12 = telebot.types.KeyboardButton("ROKU")
btn13 = telebot.types.KeyboardButton("COIN")
btn14 = telebot.types.KeyboardButton("LICD")
btn15 = telebot.types.KeyboardButton("NIO")
btn16 = telebot.types.KeyboardButton("NFLX")
btn17 = telebot.types.KeyboardButton("DXY")
btn18 = telebot.types.KeyboardButton("DJI")
btn19 = telebot.types.KeyboardButton("GOLD")
btn20 = telebot.types.KeyboardButton("CRUDE_OIL")
btn21 = telebot.types.KeyboardButton("القائمة الرئيسية")
keyboard_admin_stocks = telebot.types.ReplyKeyboardMarkup(row_width=3,selective=True ,one_time_keyboard=True)
keyboard_admin_stocks.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11,
           btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20, btn21)


btn1 = types.InlineKeyboardButton("SPX", callback_data="SPX_admin_ai")
btn2 = types.InlineKeyboardButton("QQQ", callback_data='QQQ_admin_ai')
btn3 = types.InlineKeyboardButton("AAPL", callback_data='AAPL_admin_ai')
btn4 = types.InlineKeyboardButton("MSFT", callback_data='MSFT_admin_ai')
btn5 = types.InlineKeyboardButton("TSLA", callback_data='TSLA_admin_ai')
btn6 = types.InlineKeyboardButton("NVDA", callback_data='NVDA_admin_ai')
btn7 = types.InlineKeyboardButton("AMZN", callback_data='AMZN_admin_ai')
btn8 = types.InlineKeyboardButton("META", callback_data='META_admin_ai')
btn9 = types.InlineKeyboardButton("GOOGL", callback_data='GOOGL_admin_ai')
btn10 = types.InlineKeyboardButton("AMD", callback_data='AMD_admin_ai')
btn11 = types.InlineKeyboardButton("SHOP", callback_data='SHOP_admin_ai')
btn12 = types.InlineKeyboardButton("ROKU", callback_data='ROKU_admin_ai')
btn13 = types.InlineKeyboardButton("COIN", callback_data='COIN_admin_ai')
btn14 = types.InlineKeyboardButton("LICD", callback_data='LICD_admin_ai')
btn15 = types.InlineKeyboardButton("NIO", callback_data='NIO_admin_ai')
btn16 = types.InlineKeyboardButton("NFLX", callback_data='NFLX_admin_ai')
btn17 = types.InlineKeyboardButton("DXY", callback_data='DXY_admin_ai')
btn18 = types.InlineKeyboardButton("DJI", callback_data='DJI_admin_ai')
btn19 = types.InlineKeyboardButton("GOLD", callback_data='GOLD_admin_ai')
btn20 = types.InlineKeyboardButton("CRUDE OIL", callback_data='CRUDE_OIL_admin_ai')
keyboard_admin_stocks_ai = types.InlineKeyboardMarkup(row_width=4)
keyboard_admin_stocks_ai.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11,
           btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20)


btn1 = types.InlineKeyboardButton("SPX", callback_data="SPX_admin_s")
btn2 = types.InlineKeyboardButton("QQQ", callback_data='QQQ_admin_s')
btn3 = types.InlineKeyboardButton("AAPL", callback_data='AAPL_admin_s')
btn4 = types.InlineKeyboardButton("MSFT", callback_data='MSFT_admin_s')
btn5 = types.InlineKeyboardButton("TSLA", callback_data='TSLA_admin_s')
btn6 = types.InlineKeyboardButton("NVDA", callback_data='NVDA_admin_s')
btn7 = types.InlineKeyboardButton("AMZN", callback_data='AMZN_admin_s')
btn8 = types.InlineKeyboardButton("META", callback_data='META_admin_s')
btn9 = types.InlineKeyboardButton("GOOGL", callback_data='GOOGL_admin_s')
btn10 = types.InlineKeyboardButton("AMD", callback_data='AMD_admin_s')
btn11 = types.InlineKeyboardButton("SHOP", callback_data='SHOP_admin_s')
btn12 = types.InlineKeyboardButton("ROKU", callback_data='ROKU_admin_s')
btn13 = types.InlineKeyboardButton("COIN", callback_data='COIN_admin_s')
btn14 = types.InlineKeyboardButton("LICD", callback_data='LICD_admin_s')
btn15 = types.InlineKeyboardButton("NIO", callback_data='NIO_admin_s')
btn16 = types.InlineKeyboardButton("NFLX", callback_data='NFLX_admin_s')
btn17 = types.InlineKeyboardButton("DXY", callback_data='DXY_admin_s')
btn18 = types.InlineKeyboardButton("DJI", callback_data='DJI_admin_s')
btn19 = types.InlineKeyboardButton("GOLD", callback_data='GOLD_admin_s')
btn20 = types.InlineKeyboardButton("CRUDE OIL", callback_data='CRUDE_OIL_admin_s')
keyboard_admin_support_tables = types.InlineKeyboardMarkup(row_width=4)
keyboard_admin_support_tables.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11,
           btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20)


# # variables

# In[4]:


path = "/home/mrwallstreets/Bot"
recommendation_group_id = -1001622155453
academy_group_id = -1001729868423

ai_stocks_coverter = {'SPX_admin_ai':'SPX', 'QQQ_admin_ai':'QQQ', 'COIN_admin_ai':'COIN', 'ROKU_admin_ai':'ROKU',
             'SHOP_admin_ai':'SHOP', 'AMD_admin_ai':'AMD', 'GOOGL_admin_ai':'GOOGL', 'META_admin_ai':'META',
             'AMZN_admin_ai':'AMZN', 'NVDA_admin_ai':'NVDA', 'TSLA_admin_ai':'TSLA', 'MSFT_admin_ai':'MSFT',
             'AAPL_admin_ai':'AAPL', 'LICD_admin_ai':'LICD', 'NIO_admin_ai':'NIO', 'NFLX_admin_ai':'NFLX',
             'DXY_admin_ai':'DXY', 'DJI_admin_ai':'DJI', 'GOLD_admin_ai':'GOLD', 'CRUDE_OIL_admin_ai':'CRUDE_OIL'}

support_tables_coverter = {'SPX_admin_s':'SPX_s', 'QQQ_admin_s':'QQQ_s', 'COIN_admin_s':'COIN_s', 'ROKU_admin_s':'ROKU_s',
             'SHOP_admin_s':'SHOP_s', 'AMD_admin_s':'AMD_s', 'GOOGL_admin_s':'GOOGL_s', 'META_admin_s':'META_s',
             'AMZN_admin_s':'AMZN_s', 'NVDA_admin_s':'NVDA_s', 'TSLA_admin_s':'TSLA_s', 'MSFT_admin_s':'MSFT_s',
             'AAPL_admin_s':'AAPL_s', 'LICD_admin_s':'LICD_s', 'NIO_admin_s':'NIO_s', 'NFLX_admin_s':'NFLX_s',
             'DXY_admin_s':'DXY_s', 'DJI_admin_s':'DJI_s', 'GOLD_admin_s':'GOLD_s', 'CRUDE_OIL_admin_s':'CRUDE_OIL_s'}


# # check admin
#

# In[5]:


ADMIN_USERS = [1145204670,42094194,1069032545]


def admin_only(func):
    def wrapper(message):
        user_id = message.chat.id
        if message.from_user.id in ADMIN_USERS:
            bot.send_message(message.chat.id, "Hi admin")
            return func(message)

        else:
            bot.send_message(message.chat.id, "مرحباً بك في نظام Mr WallStreet Ai للذكاء الاصطناعي، منظومة متكاملة لخدمة المستثمرين في الاسواق الامريكية" , reply_markup=keyboard_user)


    return wrapper


# # Handel start  (for admin)

# In[6]:


@bot.message_handler(func=lambda message: message.text in ["start"])
@admin_only
def welcome_admin(message):
    bot.send_message(message.chat.id, "مرحبا بك في قائمة الادمن" , reply_markup=keyboard_admin)


# # Function to cancel with "."

# In[7]:


def cancel(msg):
    if str(msg) == "0":
        return True
    else:
        return False


# # Handle اضافة عميل

# In[8]:


@bot.message_handler(func=lambda message: message.text == "اضافة عميل")
@admin_only

def add_customer(message):
    bot.send_message(message.chat.id,"قم بارسال id العميل")
    bot.register_next_step_handler(message, get_customer_id)

def get_customer_id(message):
    customer_id = message.text
    if cancel(customer_id):
        welcome_admin(message)
    else:
        bot.send_message(message.chat.id,"قم بارسال رابط حساب العميل")
        bot.register_next_step_handler(message, get_customer_link, customer_id)


def get_customer_link(message,customer_id):
    customer_link = message.text
    if cancel(customer_link):
        welcome_admin(message)
    else:
        bot.send_message(message.chat.id,"قم بارسال مدة الاشتراك")
        bot.register_next_step_handler(message, save_customer, customer_id, customer_link)

def save_customer(message, customer_id, customer_link):
    try:
        days = int(message.text)
        if cancel(days):
            welcome_admin(message)
        else:
            with open(f'{path}/files/users.json', 'r') as file:
                    data = json.load(file)

            data.setdefault("current users", {})[customer_id] = [days, customer_link]
            data.setdefault("All users", {})[customer_id] = [days, customer_link]

            with open(f'{path}/files/users.json', 'w') as file:
                    json.dump(data, file, indent=4)

            bot.send_message(message.chat.id, "تم اضافة العميل بنجاح")
    except Exception as e:
        bot.send_message(message.chat.id, f"error {e}")
        welcome_admin(message)


# # Handel تعديل اشتراك عميل

# In[9]:


@bot.message_handler(func=lambda message: message.text == "تعديل اشتراك عميل")
@admin_only

def edit_days(message):
    bot.send_message(message.chat.id,"قم بارسال id العميل")
    bot.register_next_step_handler(message, get_new_days)

def get_new_days(message):
    customer_id = message.text
    if cancel(customer_id):
        welcome_admin(message)
    else:
        bot.send_message(message.chat.id,"قم بارسال مدة الاشتراك الجديدة")
        bot.register_next_step_handler(message, save_new_days, customer_id)

def save_new_days(message, customer_id):
    try:
        days = int(message.text)
        if cancel(days):
            welcome_admin(message)
        else:
            with open(f'{path}/files/users.json', 'r') as file:
                    data = json.load(file)
            if customer_id in data["current users"]:
                data["current users"][customer_id][0] = days
                with open(f'{path}/files/users.json', 'w') as file:
                    json.dump(data, file, indent=4)
                bot.send_message(message.chat.id, "تم تعديل مدة الاشتراك بنجاح")
            else:
                bot.send_message(message.chat.id, "العميل غير موجود")

    except Exception as e:
        bot.send_message(message.chat.id, f"error {e}")
        welcome_admin(message)



# # Handle تعديل اخر الاخبار

# In[10]:


@bot.message_handler(func=lambda message: message.text == "تعديل اخر الاخبار")
@admin_only

def edit_news(message):
    bot.send_message(message.chat.id,"ارسل الخبر الجديد")
    bot.register_next_step_handler(message, save_news)

def save_news(message):
    try:
        news = message.text

        with open(f'{path}/files/data.json', 'r') as file:
            data = json.load(file)

        data["news"] = news

        with open(f'{path}/files/data.json', 'w') as file:
            json.dump(data, file, indent=4)
        bot.send_message(message.chat.id,"تم حفظ الخبر بنجاح")

    except Exception as e:
        bot.send_message(message.chat.id,f"Error {e}")


# # Handle تعديل سهم اليوم

# In[11]:


@bot.message_handler(func=lambda message: message.text == "تعديل سهم اليوم")
@admin_only

def edit_stock_day(message):
    bot.send_message(message.chat.id,"قم باختيار نوع التعديل", reply_markup = keyboard_admin_text_pic)
    bot.register_next_step_handler(message, get_stock_day_edit)

def get_stock_day_edit(message):
    edit_type = message.text

    if edit_type == "القائمة الرئيسية":
        bot.send_message(message.chat.id,"القائمة الرئيسية")
        welcome_admin(message)

    elif edit_type in ["نص وصورة", "نص فقط"]:
        bot.send_message(message.chat.id,"قم بارسال محتوي سهم اليوم")
        bot.register_next_step_handler(message, get_stock_day, edit_type)

    else:
        bot.send_message(message.chat.id,"ادخال غير صحيح")
        welcome_admin(message)


def get_stock_day(message, edit_type):
    stock_day = message.text
    with open(f'{path}/files/data.json', 'r') as file:
        data = json.load(file)

    data["stock_day"] = stock_day

    with open(f'{path}/files/data.json', 'w') as file:
        json.dump(data, file, indent=4)

    if edit_type == "نص فقط":
        old_image_path = f'{path}/files/stock_day.jpg'
        if os.path.exists(old_image_path):
            os.remove(old_image_path)
        else:
            pass

        bot.send_message(message.chat.id,"تم حفظ السهم بنجاح")

    elif edit_type == "نص وصورة":
        bot.send_message(message.chat.id,"قم بارسال الصورة")
        bot.register_next_step_handler(message, save_stock_day_image)


def save_stock_day_image(message):
    try:
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file = bot.download_file(file_info.file_path)
        file_name = 'stock_day.jpg'
        folder_path = f'{path}/files/'

        with open(os.path.join(folder_path, file_name), 'wb') as f:
            f.write(file)

        bot.send_message(message.chat.id,"تم حفظ السهم بنجاح")

    except Exception as e:
        bot.send_message(message.chat.id,f"Error {e}")


# # Handle تعديل AI

# In[12]:


@bot.message_handler(func=lambda message: message.text == "تعديل AI")
@admin_only

def edit_ِai(message):
    bot.send_message(message.chat.id,"قم باختيار السهم", reply_markup = keyboard_admin_stocks_ai)

def get_stock_to_edit(message, stock_name):
    bot.send_message(message.chat.id,f"{stock_name} قم بارسال محتوي سهم")
    bot.register_next_step_handler(message, save_ai, stock_name)

def save_ai(message, stock_name):
    try:
        content = message.text
        with open(f'{path}/files/data.json', 'r') as file:
            data = json.load(file)

        data["stocks"][stock_name] = content

        with open(f'{path}/files/data.json', 'w') as file:
            json.dump(data, file, indent=4)
        bot.send_message(message.chat.id,f"تم حفظ محتوي سهم {stock_name} بنجاح")
    except Exception as e:
        bot.send_message(message.chat.id,f"Error {e}")


# # تعديل جدول الدعم والمقاومة

# In[13]:


@bot.message_handler(func=lambda message: message.text == "تعديل جدول الدعم والمقاومة")
@admin_only

def edit_support_and_resistance(message):
    bot.send_message(message.chat.id,"قم باختيار السهم", reply_markup = keyboard_admin_support_tables)

def get_support_and_resistance_edit(message, stock_name):
    bot.send_message(message.chat.id,f"{stock_name} قم بارسال جدول الدعم والمقاومة لسهم")
    bot.register_next_step_handler(message, save_support_and_resistance_pic, stock_name)

def save_support_and_resistance_pic(message, stock_name):
    try:
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file = bot.download_file(file_info.file_path)
        file_name = f'{stock_name}.jpg'
        folder_path = f'{path}/files/'

        with open(os.path.join(folder_path, file_name), 'wb') as f:
            f.write(file)

        bot.send_message(message.chat.id,f"تم حفظ جدول الدعم والمقاومة لسهم {stock_name}")

    except Exception as e:
        bot.send_message(message.chat.id,f"Error {e}")


# # Handle تعديل الزخم

# In[14]:


@bot.message_handler(func=lambda message: message.text == "تعديل الزخم")
@admin_only

def edit_most_momentum_stocks(message):
    bot.send_message(message.chat.id,"قم باختيار نوع التعديل", reply_markup = keyboard_admin_text_pic)
    bot.register_next_step_handler(message, get_most_momentum_stocks_edit)

def get_most_momentum_stocks_edit(message):
    edit_type = message.text

    if edit_type == "القائمة الرئيسية":
        bot.send_message(message.chat.id,"القائمة الرئيسية")
        welcome_admin(message)

    elif edit_type in ["نص وصورة", "نص فقط"]:
        bot.send_message(message.chat.id,"قم بارسال محتوي اكثر الاسهم زخم")
        bot.register_next_step_handler(message, get_most_momentum_stocks, edit_type)

    else:
        bot.send_message(message.chat.id,"ادخال غير صحيح")
        welcome_admin(message)


def get_most_momentum_stocks(message, edit_type):
    Most_momentum_stocks = message.text
    with open(f'{path}/files/data.json', 'r') as file:
        data = json.load(file)

    data["Most_momentum_stocks"] = Most_momentum_stocks

    with open(f'{path}/files/data.json', 'w') as file:
        json.dump(data, file, indent=4)

    if edit_type == "نص فقط":
        old_image_path = f'{path}/files/Most_momentum_stocks.jpg'
        if os.path.exists(old_image_path):
            os.remove(old_image_path)
        else:
            pass

        bot.send_message(message.chat.id,"تم حفظ محتوي اكثر الاسهم زخم بنجاح")

    elif edit_type == "نص وصورة":
        bot.send_message(message.chat.id,"قم بارسال الصورة")
        bot.register_next_step_handler(message, save_most_momentum_stocks_image)


def save_most_momentum_stocks_image(message):
    try:
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file = bot.download_file(file_info.file_path)
        file_name = 'Most_momentum_stocks.jpg'
        folder_path = f'{path}/files/'

        with open(os.path.join(folder_path, file_name), 'wb') as f:
            f.write(file)

        bot.send_message(message.chat.id,"تم حفظ محتوي اكثر الاسهم زخم بنجاح")

    except Exception as e:
        bot.send_message(message.chat.id,f"Error {e}")


# # Handle تعديل التقرير اليومي

# In[15]:


@bot.message_handler(func=lambda message: message.text == "تعديل التقرير اليومي")
@admin_only

def edit_daily_report(message):
    bot.send_message(message.chat.id,"قم بارسال ملف التقرير اليومي")
    bot.register_next_step_handler(message, get_daily_report_edit)

def get_daily_report_edit(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        file_path = file_info.file_path
        downloaded_file = bot.download_file(file_path)

        save_path = f'{path}/files/daily_report.pdf'

        with open(save_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.send_message(message.chat.id,"تم حفظ التقرير اليومي بنجاح")
    except Exception as e:
        bot.send_message(message.chat.id,f"Error {e}")


# # Handel ارسال رسالة

# In[16]:


@bot.message_handler(func=lambda message: message.text == "ارسال رسالة")
@admin_only

def choose_audience(message):
    bot.send_message(message.chat.id, "لاي عملاء تود ارسال الرسالة", reply_markup = keyboard_admin_send_msg)
    bot.register_next_step_handler(message, get_content)


def get_content(message):
    audience = message.text
    if audience == "القائمة الرئيسية":
        bot.send_message(message.chat.id,"القائمة الرئيسية")
        welcome_admin(message)

    elif audience in ['للعملاء الحالبين','لكل العملاء']:
        bot.send_message(message.chat.id, "قم بارسال المحتوي")
        bot.register_next_step_handler(message, forward_content, audience)
    else:
        welcome_admin(message)

def forward_content(message, audience):
    with open(f'{path}/files/users.json', 'r') as file:
        data = json.load(file)

    if audience == 'للعملاء الحالبين':
        counter = 0
        users = data["current users"]
        for user_id in users:
            try:
                bot.forward_message(user_id, message.chat.id, message.message_id)
                counter += 1
            except Exception as e:
                pass
        bot.send_message(message.chat.id, f"تم الارسال بنجاح الي {counter} مستخدم")

    elif audience == 'لكل العملاء':
        counter = 0
        users = data["All users"]
        for user_id in users:
            try:
                bot.forward_message(user_id, message.chat.id, message.message_id)
                counter += 1
            except Exception as e:
                pass
        bot.send_message(message.chat.id, f"تم الارسال بنجاح الي {counter} مستخدم")



# # Handle callback for admin

# In[17]:


@bot.callback_query_handler(func=lambda call: call.data in ai_stocks_coverter.keys() or call.data in support_tables_coverter.keys() or call.data == "main_menu")
def handle_callback_query(call):
    stock = call.data
    if stock in ai_stocks_coverter:
        stock_name = ai_stocks_coverter[stock]
        get_stock_to_edit(call.message, stock_name)

    elif stock in support_tables_coverter:
        stock_name = support_tables_coverter[stock]
        get_support_and_resistance_edit(call.message,stock_name)

    else:
        back_to_main(call.message)



# # Handle القائمة الرئيسية

# In[18]:


@bot.message_handler(func=lambda message: message.text == "القائمة الرئيسية")
def back_to_main(message):
    bot.send_message(message.chat.id, "القائمة الرئيسية", reply_markup=keyboard_admin)


# # Create user buttons

# In[19]:


# first layer buttons
btn1 = telebot.types.KeyboardButton("💰مستر وول ستريت")
btn2 = telebot.types.KeyboardButton("❓طريقة الاستخدام")
btn3 = telebot.types.KeyboardButton("☎️الدعم الفني")
btn4 = telebot.types.KeyboardButton("💻الموقع الالكتروني")
btn5 = telebot.types.KeyboardButton("✅اقتراحتكم")
keyboard_user = telebot.types.ReplyKeyboardMarkup(row_width=2,selective=True ,one_time_keyboard=True)
keyboard_user.add(btn1, btn2, btn3, btn4, btn5)


# when user click on 'خدمات مستر ول ستريت'
btn1 = types.InlineKeyboardButton("مدونة✍️", url="https://mrwallstreets.com/blog")
btn2 = types.InlineKeyboardButton("خدمات مستر وول ستريت Ai 💰", callback_data='stocks')
btn3 = types.InlineKeyboardButton("اخر الاخبار🚨", callback_data='news')
btn4 = types.InlineKeyboardButton("سهم اليوم🥇", callback_data='stock_day')
btn5 = types.InlineKeyboardButton("اكثر الاسهم زخم🚀", callback_data='Most_momentum_stocks')
btn6 = types.InlineKeyboardButton("جدول الدعم والمقاومة🔻🔺", callback_data='Support_and_resistance')
btn7 = types.InlineKeyboardButton("التقرير اليومي📊", callback_data='daily_report')
keyboard_mr_wall_street = types.InlineKeyboardMarkup(row_width=2)
keyboard_mr_wall_street.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)


btn1 = types.InlineKeyboardButton("SPX", callback_data="SPX")
btn2 = types.InlineKeyboardButton("QQQ", callback_data='QQQ')
btn3 = types.InlineKeyboardButton("AAPL", callback_data='AAPL')
btn4 = types.InlineKeyboardButton("MSFT", callback_data='MSFT')
btn5 = types.InlineKeyboardButton("TSLA", callback_data='TSLA')
btn6 = types.InlineKeyboardButton("NVDA", callback_data='NVDA')
btn7 = types.InlineKeyboardButton("AMZN", callback_data='AMZN')
btn8 = types.InlineKeyboardButton("META", callback_data='META')
btn9 = types.InlineKeyboardButton("GOOGL", callback_data='GOOGL')
btn10 = types.InlineKeyboardButton("AMD", callback_data='AMD')
btn11 = types.InlineKeyboardButton("SHOP", callback_data='SHOP')
btn12 = types.InlineKeyboardButton("ROKU", callback_data='ROKU')
btn13 = types.InlineKeyboardButton("COIN", callback_data='COIN')
btn14 = types.InlineKeyboardButton("LICD", callback_data='LICD')
btn15 = types.InlineKeyboardButton("NIO", callback_data='NIO')
btn16 = types.InlineKeyboardButton("NFLX", callback_data='NFLX')
btn17 = types.InlineKeyboardButton("DXY", callback_data='DXY')
btn18 = types.InlineKeyboardButton("DJI", callback_data='DJI')
btn19 = types.InlineKeyboardButton("GOLD", callback_data='GOLD')
btn20 = types.InlineKeyboardButton("CRUDE OIL", callback_data='CRUDE_OIL')
keyboard_stocks = types.InlineKeyboardMarkup(row_width=4)
keyboard_stocks.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11,
           btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20)



btn1 = types.InlineKeyboardButton("SPX", callback_data="SPX_s")
btn2 = types.InlineKeyboardButton("QQQ", callback_data='QQQ_s')
btn3 = types.InlineKeyboardButton("AAPL", callback_data='AAPL_s')
btn4 = types.InlineKeyboardButton("MSFT", callback_data='MSFT_s')
btn5 = types.InlineKeyboardButton("TSLA", callback_data='TSLA_s')
btn6 = types.InlineKeyboardButton("NVDA", callback_data='NVDA_s')
btn7 = types.InlineKeyboardButton("AMZN", callback_data='AMZN_s')
btn8 = types.InlineKeyboardButton("META", callback_data='META_s')
btn9 = types.InlineKeyboardButton("GOOGL", callback_data='GOOGL_s')
btn10 = types.InlineKeyboardButton("AMD", callback_data='AMD_s')
btn11 = types.InlineKeyboardButton("SHOP", callback_data='SHOP_s')
btn12 = types.InlineKeyboardButton("ROKU", callback_data='ROKU_s')
btn13 = types.InlineKeyboardButton("COIN", callback_data='COIN_s')
btn14 = types.InlineKeyboardButton("LICD", callback_data='LICD_s')
btn15 = types.InlineKeyboardButton("NIO", callback_data='NIO_s')
btn16 = types.InlineKeyboardButton("NFLX", callback_data='NFLX_s')
btn17 = types.InlineKeyboardButton("DXY", callback_data='DXY_s')
btn18 = types.InlineKeyboardButton("DJI", callback_data='DJI_s')
btn19 = types.InlineKeyboardButton("GOLD", callback_data='GOLD_s')
btn20 = types.InlineKeyboardButton("CRUDE OIL", callback_data='CRUDE_OIL_s')
keyboard_support_stocks = types.InlineKeyboardMarkup(row_width=4)
keyboard_support_stocks.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11,
           btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20)


# # check subscriber

# In[20]:


#for function
def subscriber_only(func):
    def wrapper_subscriber(message):
        try:
            user_id = str(message.chat.id)
            with open(f'{path}/files/users.json', 'r') as file:
                data = json.load(file)
            if user_id in data["current users"]:
                return func(message)
            else:
                bot.send_message(message.chat.id, "عذرا ، لست مشترك في القناه الذهبيه \n"
                             "للأشتراك : mrwallstreets.com")
                welcome_user(message)

        except Exception as e:
            print(e)


    return wrapper_subscriber


# for callback
def check_subscriber(message):
    try:
        user_id = str(message.chat.id)
        with open(f'{path}/files/users.json', 'r') as file:
            data = json.load(file)
        if user_id in data["current users"]:
            return True
        else:
            bot.send_message(message.chat.id, "عذرا ، لست مشترك في القناه الذهبيه \n"
                         "للأشتراك : mrwallstreets.com")
            welcome_user(message)

    except Exception as e:
        pass


# # Handel /start  (for users)

# In[21]:


@bot.message_handler(commands=['start'])
def welcome_user(message):
    bot.send_message(message.chat.id, "مرحباً بك في نظام Mr WallStreet Ai للذكاء الاصطناعي، منظومة متكاملة لخدمة المستثمرين في الاسواق الامريكية" ,
                     reply_markup=keyboard_user)


# # Handle 💰مستر وول ستريت

# In[22]:


@bot.message_handler(func=lambda message: message.text == "💰مستر وول ستريت")
@subscriber_only
def handel_academy_services(message):
    bot.send_message(message.chat.id, "خدمات مستر وول ستريت 💰" , reply_markup=keyboard_mr_wall_street)


# # Handle callback

# In[23]:


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if check_subscriber(call.message):
        if call.data == "stocks":
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
            bot.send_message(call.message.chat.id, "قم باختيار السهم الذي تريده",reply_markup=keyboard_stocks)


        elif call.data in ["SPX","QQQ","AAPL","MSFT","TSLA","NVDA","AMZN","META","GOOGL","AMD","SHOP","ROKU","COIN",
        "LICD","NIO","NFLX","DXY","DJI","GOLD","CRUDE_OIL"]:
            stock = call.data
            with open(f'{path}/files/data.json', 'r') as file:
                data = json.load(file)
            msg = data["stocks"][stock]
            bot.send_message(call.message.chat.id, f"{msg}")


        elif call.data == "daily_report":
            file_path = f'{path}/files/daily_report.pdf'

            # Check if the file exists
            if os.path.exists(file_path):
                with open(file_path, 'rb') as file:
                    bot.send_document(call.message.chat.id, file, caption="التقرير اليومي")
            else:
                bot.send_message(call.message.chat.id, f"عذرا التقرير اليومي ليس موجود حاليا")


        elif call.data == "Support_and_resistance":
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
            bot.send_message(call.message.chat.id, "قم باختيار السهم الذي تريده",reply_markup=keyboard_support_stocks)


        elif call.data in ["SPX_s","QQQ_s","AAPL_s","MSFT_s","TSLA_s","NVDA_s","AMZN_s","META_s","GOOGL_s","AMD_s","SHOP_s",
                           "ROKU_s","COIN_s", "LICD_s","NIO_s","NFLX_s","DXY_s","DJI_s","GOLD_s","CRUDE_OIL_s"]:
            stock = call.data
            file_path = f'{path}/files/{stock}.jpg'

            # Check if the file exists
            if os.path.exists(file_path):
                with open(file_path, 'rb') as photo:
                    bot.send_photo(call.message.chat.id, photo)
            else:
                bot.send_message(call.message.chat.id, f"الجدول غير متوفر الان")


        else:
            call_data = call.data
            with open(f'{path}/files/data.json', 'r') as file:
                data = json.load(file)
            msg = data[call_data]
            file_path = f'{path}/files/{call_data}.jpg'

            # Check if the file exists
            if os.path.exists(file_path):
                with open(file_path, 'rb') as photo:
                    bot.send_photo(call.message.chat.id, photo, caption=msg)
            else:
                bot.send_message(call.message.chat.id, f"{msg}")





# # Handle ❓طريقة الاستخدام

# In[24]:


@bot.message_handler(func=lambda message: message.text == "❓طريقة الاستخدام")
def handel_how_to_use(message):
    bot.send_message(message.chat.id, "فيديو شرح البوت \n"
                                      "https://t.me/MrWallStreets/2155")


# # Handle ☎️الدعم الفني

# In[25]:


@bot.message_handler(func=lambda message: message.text == "☎️الدعم الفني")
def handel_support(message):
    bot.send_message(message.chat.id, "الحساب الخاص بالدعم الفني \n"
                                      "https://t.me/MrOption")


# # Handle 💻الموقع الالكتروني

# In[26]:


@bot.message_handler(func=lambda message: message.text == "💻الموقع الالكتروني")
def handel_website(message):
    bot.send_message(message.chat.id, "الموقع الالكتروني الخاص بنا \n"
                                      "https://mrwallstreets.com/")


# # Handle ✅اقتراحتكم

# In[27]:


@bot.message_handler(func=lambda message: message.text == "✅اقتراحتكم")
def handel_recommend(message):
    bot.send_message(message.chat.id, "برجاء ارسال اقتراحك في رسالة واحدة")
    bot.register_next_step_handler(message, send_to_group)

def send_to_group(message):
    msg = message.text
    bot.forward_message(recommendation_group_id, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "تم ارسال اقتراحك بنجاح")


# # Threads

# ## check users

# In[28]:


def check_users():
    try:
        with open(f'{path}/files/users.json', 'r') as file:
            data = json.load(file)

        users_to_remove = []
        users = data["current users"]
        for user_id in users:
            if data["current users"][user_id][0] == 0:
                users_to_remove.append(user_id)

        for user_id in users_to_remove:
            del data["current users"][user_id]

        # remove from group
        bot.kick_chat_member(academy_group_id, user_id)
        time.sleep(10)
        bot.unban_chat_member(academy_group_id, user_id)

        with open(f'{path}/files/users.json', 'w') as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        pass


# ## update days

# In[29]:


def update_days():
    with open(f'{path}/files/users.json', 'r') as file:
        data = json.load(file)

    for user in data["current users"]:
        data["current users"][user][0] -= 1

    with open(f'{path}/files/users.json', 'w') as file:
        json.dump(data, file, indent=4)


# # run parallel functions

# In[30]:


def run():
    schedule.every().day.at("21:00").do(check_users)
    schedule.every().day.at("21:05").do(update_days)


    while True:
        # Run the scheduled tasks
        schedule.run_pending()
        time.sleep(60)

check_thread = threading.Thread(target=run)
check_thread.start()


# In[ ]:

bot.infinity_polling(timeout=10, long_polling_timeout = 5)
#bot._TeleBot__retrieve_updates(timeout=60)
#bot.polling(none_stop=True)

