import telebot
from telebot import types

# Токен вашего бота
TOKEN = '8053051580:AAFyiRhNzFHWfIf8FdQOGuBwgnJkA6NxKUQ'
bot = telebot.TeleBot(TOKEN)

# Вопросы теста
questions = [
    {
        "text": "<b>1. Как ты планируешь свой рабочий день? 📅</b>\n\n"
                "<b>a)</b> За чашкой кофе, разглядывая потолок. ☕\n"
                "<b>b)</b> Составляю детальный план на неделю. 📝\n"
                "<b>c)</b> Просто иду туда, где пахнет деньгами. 💰\n"
                "<b>d)</b> Открываю календарь и надеюсь, что что-то само собой произойдёт. 🗓️",
        "image": "resources/q1.jpg"  
    },
    {
        "text": "<b>2. Как ты реагируешь на неудачи? 😔</b>\n\n"
                "<b>a)</b> Плачу в подушку. 😭\n"
                "<b>b)</b> Анализирую и ищу способы улучшить. 🤔\n"
                "<b>c)</b> Пытаюсь продать подушку как 'антикризисный товар'. 💡\n"
                "<b>d)</b> Просто игнорирую, ведь завтра новый день! 🌞",
        "image": "resources/q2.jpg"  
    },
    {
        "text": "<b>3. Какой у тебя бизнес-план? 📄</b>\n\n"
                "<b>a)</b> 'Сделаю что-то, а там посмотрим'. 🤷‍♂️\n"
                "<b>b)</b> Подробный документ на 50 страниц. 📚\n"
                "<b>c)</b> 'Пока не поздно, надо искать инвесторов'. 💼\n"
                "<b>d)</b> 'Я просто люблю делать что-то интересное'. 🎯",
        "image": "resources/q3.jpg"  
    },
    {
        "text": "<b>4. Как ты находишь своих клиентов? 👥</b>\n\n"
                "<b>a)</b> Случайно на улице, иногда с помощью флаеров. 🚶‍♂️\n"
                "<b>b)</b> Через соцсети и рекламу. 📱\n"
                "<b>c)</b> Уговариваю друзей рассказать о моём бизнесе. 🤝\n"
                "<b>d)</b> Они сами ко мне приходят. Я же крут! 😎",
        "image": "resources/q4.jpg"  
    },
    {
        "text": "<b>5. Как ты оцениваешь свои риски? 🎲</b>\n\n"
                "<b>a)</b> 'Риск — благородное дело!' 🎯\n"
                "<b>b)</b> Смотрю на цифры и графики. 📊\n"
                "<b>c)</b> Рисую на бумаге и надеюсь на лучшее. 🎨\n"
                "<b>d)</b> Какой риск? Я всё равно не боюсь! 💪",
        "image": "resources/q5.jpg"  
    },
    {
        "text": "<b>6. Что ты думаешь о конкурентах? 🥊</b>\n\n"
                "<b>a)</b> Это мои лучшие друзья. 🤝\n"
                "<b>b)</b> Необходимо следить за ними. 👀\n"
                "<b>c)</b> Конкуренция — это возможность! 💡\n"
                "<b>d)</b> Кто такие конкуренты? Я не слышал. 🙉",
        "image": "resources/q6.jpg"  
    },
    {
        "text": "<b>7. Какой у тебя стиль управления? 👨‍💼</b>\n\n"
                "<b>a)</b> 'Все делают, что хотят!' 🎉\n"
                "<b>b)</b> Строгий, но справедливый. ⚖️\n"
                "<b>c)</b> Как в фильме 'Супермен' – я спасаю всех! 🦸‍♂️\n"
                "<b>d)</b> Я просто надеюсь, что все будут работать. 🤞",
        "image": "resources/q7.jpg"  
    },
    {
        "text": "<b>8. Как ты решаешь проблемы? 🛠️</b>\n\n"
                "<b>a)</b> Отвлекаюсь на мемы в интернете. 😂\n"
                "<b>b)</b> Составляю список действий. 📋\n"
                "<b>c)</b> Придумываю креативные решения. 💡\n"
                "<b>d)</b> Жду, когда проблема решится сама. 🕰️",
        "image": "resources/q8.jpg"  
    },
    {
        "text": "<b>9. Как ты привлекаешь инвестиции? 💸</b>\n\n"
                "<b>a)</b> Обещаю золотые горы и рисую графики. 📈\n"
                "<b>b)</b> Предлагаю чёткий бизнес-план. 📄\n"
                "<b>c)</b> Уговариваю друзей вложить деньги. 🤝\n"
                "<b>d)</b> Просто надеюсь на удачу! 🍀",
        "image": "resources/q9.jpg"  
    },
    {
        "text": "<b>10. Как ты относишься к команде? 👥</b>\n\n"
                "<b>a)</b> Команда? Это просто слово. 🗣️\n"
                "<b>b)</b> Команда — это моя опора! 💪\n"
                "<b>c)</b> Они должны работать как семья. 👨‍👩‍👧‍👦\n"
                "<b>d)</b> Я один – мне не нужна команда! 🚶‍♂️",
        "image": "resources/q10.jpg"  
    },
    {
        "text": "<b>11. Как ты оцениваешь успех? 🏆</b>\n\n"
                "<b>a)</b> По количеству лайков в Instagram. ❤️\n"
                "<b>b)</b> По прибыли и росту бизнеса. 💹\n"
                "<b>c)</b> По количеству друзей и знакомых. 👥\n"
                "<b>d)</b> По количеству чашек кофе, выпитых за день. ☕",
        "image": "resources/q11.jpg"  
    },
    {
        "text": "<b>12. Какой у тебя девиз? 🗣️</b>\n\n"
                "<b>a)</b> 'Кто не рискует, тот не пьет шампанского!' 🍾\n"
                "<b>b)</b> 'Планируй, действуй, анализируй!' 📊\n"
                "<b>c)</b> 'Смех — это лучшее лекарство!' 😂\n"
                "<b>d)</b> 'Главное — не сдаваться!' 💪",
        "image": "resources/q12.jpg"  
    }
]

# Результаты теста
results = {
    "a": {"text": "<b>Твой результат: Предприниматель-Ленивец! 🦥</b>\nТы веришь, что удача — это результат случайных событий, и поэтому стараешься не сильно напрягаться.",
          "image": "resources/result1.jpg"},  
    "b": {"text": "<b>Твой результат: Предприниматель-Стратег! 🧠</b>\nТы всегда на шаг впереди и любишь планировать. Возможно, ты даже слишком много планируешь!",
          "image": "resources/result2.jpg"},  
    "c": {"text": "<b>Твой результат: Предприниматель-Креативщик! 🎨</b>\nТы находишь необычные решения и всегда готов к приключениям. Главное, чтобы было весело!",
          "image": "resources/result3.jpg"},  
    "d": {"text": "<b>Твой результат: Предприниматель-Оптимист! 🌈</b>\nТы веришь в лучшее и надеешься, что всё само собой уладится. Главное — не терять позитивный настрой!",
          "image": "resources/result4.jpg"}   
}

# Хранение ответов пользователей и ID сообщений
user_data = {}

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_test(message):
    user_data[message.chat.id] = {"answers": [], "message_ids": []}
    with open("resources/Hello.jpg", "rb") as photo:
        sent_message = bot.send_photo(message.chat.id, photo, caption="<b>Привет! Давай узнаем, какой ты предприниматель. 😊</b>", parse_mode="HTML")
        user_data[message.chat.id]["message_ids"].append(sent_message.message_id)
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Начать тест", callback_data="start_test"))
    sent_message = bot.send_message(message.chat.id, "Нажми на кнопку, чтобы начать тест.", reply_markup=markup)
    user_data[message.chat.id]["message_ids"].append(sent_message.message_id)

# Функция для отправки вопроса
def ask_question(chat_id, question_index):
    if question_index < len(questions):
        question = questions[question_index]
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("a", callback_data="a"),
                   types.InlineKeyboardButton("b", callback_data="b"),
                   types.InlineKeyboardButton("c", callback_data="c"),
                   types.InlineKeyboardButton("d", callback_data="d"))
        if question_index > 0:
            markup.add(types.InlineKeyboardButton("Назад", callback_data="back"))
        
        # Удаляем предыдущее сообщение с вопросом
        if user_data[chat_id]["message_ids"]:
            for msg_id in user_data[chat_id]["message_ids"]:
                try:
                    bot.delete_message(chat_id, msg_id)
                except:
                    pass
            user_data[chat_id]["message_ids"] = []
        
        with open(question["image"], "rb") as photo:
            sent_message = bot.send_photo(chat_id, photo, caption=question["text"], reply_markup=markup, parse_mode="HTML")
            user_data[chat_id]["message_ids"].append(sent_message.message_id)
    else:
        calculate_result(chat_id)

# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    chat_id = call.message.chat.id
    if call.data == "start_test":
        ask_question(chat_id, 0)
    elif call.data == "back":
        if len(user_data[chat_id]["answers"]) > 0:
            user_data[chat_id]["answers"].pop()
        ask_question(chat_id, len(user_data[chat_id]["answers"]))
    elif call.data in ['a', 'b', 'c', 'd']:
        user_data[chat_id]["answers"].append(call.data)
        ask_question(chat_id, len(user_data[chat_id]["answers"]))
    elif call.data == "restart":
        user_data[chat_id] = {"answers": [], "message_ids": []}  # Сбрасываем данные
        ask_question(chat_id, 0)  # Начинаем тест с первого вопроса

# Функция для подсчета результатов
def calculate_result(chat_id):
    answers = user_data[chat_id]["answers"]
    if not answers:
        bot.send_message(chat_id, "Ты не ответил ни на один вопрос. Попробуй снова!", parse_mode="HTML")
        return

    # Подсчет количества ответов
    count_a = answers.count('a')
    count_b = answers.count('b')
    count_c = answers.count('c')
    count_d = answers.count('d')

    # Определение результата
    max_count = max(count_a, count_b, count_c, count_d)
    if max_count == count_a:
        result = results["a"]
    elif max_count == count_b:
        result = results["b"]
    elif max_count == count_c:
        result = results["c"]
    else:
        result = results["d"]

    # Удаляем предыдущее сообщение с вопросом
    if user_data[chat_id]["message_ids"]:
        for msg_id in user_data[chat_id]["message_ids"]:
            try:
                bot.delete_message(chat_id, msg_id)
            except:
                pass
        user_data[chat_id]["message_ids"] = []

    # Отправка результата
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Начать тест сначала", callback_data="restart"))
    with open(result["image"], "rb") as photo:
        bot.send_photo(chat_id, photo, caption=result["text"], reply_markup=markup, parse_mode="HTML")

# Запуск бота
bot.polling()