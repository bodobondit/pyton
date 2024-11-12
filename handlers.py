from telebot import TeleBot
from telebot import types
# from bot.bitrix24 import send_to_bitrix24

# Словарь для хранения данных от пользователя
user_data = {}



def register_handlers(bot: TeleBot):
    # Приветствие
    @bot.message_handler(content_types=['text'])
    def hello(message):
        bot.send_message(message.chat.id, "Здравствуйте! На связи заботливый"
                                               "бот SIHCKAR GROUP. Чтобы наши менеджеры"
                                               "лучше поняли ваш запрос я попрошу вас ответить"
                                               "на несколько вопросов пока мы ожидаем подключения"
                                               "менеджера ")
        bot.send_message(message.chat.id, "Как мы можем к вам обращаться?")
        bot.register_next_step_handler(message, get_name)
    def get_name(message):
        user_data['name'] = message.text
        bot.send_message(message.chat.id, "Чтобы мы могли с вами связаться в не"
                                          "мессенджера, поделитесь, пожалуйста, вашим номером телефона")
        bot.register_next_step_handler(message, get_phone)
    def get_phone(message):
        user_data['phone'] = message.text
        bot.send_message(message.chat.id, "Напишите, пожалуйста, вашу почту")
        bot.register_next_step_handler(message, get_email)
    def get_email(message):
        user_data['email'] = message.text
        bot.send_message(message.chat.id, "Укажите название вашей компании")
        bot.register_next_step_handler(message, get_company)
    def get_company(message):
        user_data['company'] = message.text
        question = "Какое направление задачи вас интересует?"
        # наша клавиатура
        keyboard = types.InlineKeyboardMarkup()
        key_km = types.InlineKeyboardButton(text='Корпоративные мероприятия', callback_data='km')
        keyboard.add(key_km)
        key_brand = types.InlineKeyboardButton(text='Брендинг', callback_data='brand')
        keyboard.add(key_brand)
        key_hr = types.InlineKeyboardButton(text='HR задачи', callback_data='hr')
        keyboard.add(key_hr)
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)




        @bot.callback_query_handler(func=lambda call: call.data == 'km')
        def start(call):
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
            bot.send_message(call.message.chat.id, 'дата мероприятия?')
            bot.register_next_step_handler(call.message, get_date)
        def get_date(message):
            user_data['date'] = message.text
            bot.send_message(message.chat.id, 'количество человек?')
            bot.register_next_step_handler(message, get_quantity)
        def get_quantity(message):
            user_data['quantity'] = message.text
            bot.send_message(message.chat.id, 'город проведения?')
            bot.register_next_step_handler(message, get_city)
        def get_city(message):
            user_data['city'] = message.text
            bot.send_message(message.chat.id, 'формат мероприятия?')
            bot.register_next_step_handler(message, get_style)
        def get_style(message):
            user_data['style'] = message.text
            question = 'бюджет?'
            keyboard = types.InlineKeyboardMarkup()
            key_f = types.InlineKeyboardButton(text='1500000 - 2000000 р', callback_data='f')
            keyboard.add(key_f)
            key_s = types.InlineKeyboardButton(text='2000000 - 5000000 р', callback_data='s')
            keyboard.add(key_s)
            key_t = types.InlineKeyboardButton(text='свыше 5000000 р', callback_data='t')
            keyboard.add(key_t)
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

            @bot.callback_query_handler(func=lambda call: call.data in ['f','s','t'])
            def get_price(call):
                user_data['price'] = call.message.text
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
                bot.register_next_step_handler(call.message, get_last_q)

        @bot.callback_query_handler(func=lambda call: call.data == 'brand')
        def start(call):
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
            question = 'Подскажите какой формат задачи стоит перед вами?'
            keyboard = types.InlineKeyboardMarkup()
            key_bk = types.InlineKeyboardButton(text='Брендинг компании', callback_data='bk')
            keyboard.add(key_bk)
            key_fmcg = types.InlineKeyboardButton(text='Брендинг FMCG', callback_data='fmcg')
            keyboard.add(key_fmcg)
            key_cs = types.InlineKeyboardButton(text='Коммуникационная стратегия бренда', callback_data='cs')
            keyboard.add(key_cs)
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

            @bot.callback_query_handler(func=lambda call: call.data in ['bk','fmcg','cs'])
            def get_format_task(call):
                user_data['format_task'] = call.message.text
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
                bot.send_message(call.message.chat.id, "Какой бюджет, примерно, вы закладыеаете на проект?")
                bot.register_next_step_handler(call.message, get_price_brand)

            def get_price_brand(message):
                user_data['price'] = message.text
                bot.register_next_step_handler(call.message, get_last_q)

        @bot.callback_query_handler(func=lambda call: call.data == 'hr')
        def sart(call):
            question = 'Какой вариант?'
            keyboard = types.InlineKeyboardMarkup()
            key_hrb = types.InlineKeyboardButton(text='HR брендинг', callback_data='hrb')
            key_hrm = types.InlineKeyboardButton(text='HR мероприятие', callback_data='hrm')
            keyboard.add(key_hrb,key_hrm)
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

            @bot.callback_query_handler(func=lambda call: call.data in ['hrb','hrm'])
            def get_source(call):
                user_data['hr variant'] = call.data
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
                bot.send_message(call.message.chat.id, "Какой бюджет, примерно, вы закладыеаете на проект?")
                bot.register_next_step_handler(call.message, get_price_hr)
            def get_price_hr(message):
                user_data['price'] = message.text
                bot.register_next_step_handler(call.message, get_last_q)

        def get_last_q(message):
            question = "У нас остался всего один вопрос. Откуда вы о нас узнали? Для нас это очень важно"
            keyboard = types.InlineKeyboardMarkup()
            key_yandex = types.InlineKeyboardButton(text='Реклама в яндексе', callback_data='yandex')
            key_radio = types.InlineKeyboardButton(text='Реклама на радио', callback_data='radio')
            keyboard.add(key_yandex, key_radio)
            key_social = types.InlineKeyboardButton(text='Соц сети', callback_data='social')
            key_replay = types.InlineKeyboardButton(text='Нас вам посоветовали', callback_data='replay')
            keyboard.add(key_social, key_replay)
            key_kon = types.InlineKeyboardButton(text='Видели на конкурсе', callback_data='kon')
            key_internet = types.InlineKeyboardButton(text='Нашли в интернете', callback_data='internet')
            keyboard.add(key_kon, key_internet)
            key_other = types.InlineKeyboardButton(text='другое', callback_data='other')
            keyboard.add(key_other)
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

            @bot.callback_query_handler(func=lambda call: call.data in
                                                          ['yandex', 'radio', 'social', 'replay', 'kon',
                                                           'internet',
                                                           'other'])
            def good_by(call):
                user_data['source'] = call.data
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
                bot.send_message(call.message.chat.id, "Спасибо, ваш заказ принят!")
                bot.send_message(call.message.chat.id, str(user_data))

    def process_phone_step(message):
        user_data['phone'] = message.text
        # Отправка данных в Bitrix24
        send_to_bitrix24(user_data)
        bot.send_message(message.chat.id, "Спасибо!")