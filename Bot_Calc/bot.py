import telebot
from info import token 



# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


# Определяем константы этапов разговора
TYPE_N, ACTION = range(2)

# функция обратного вызова точки входа в разговор
def start(update, _):
    # Список кнопок для ответа
    reply_keyboard = [['RATIONAL', 'COMPLEX']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Меня зовут калькулятор. Я помогу тебе с вычислениями. '
        'Команда /cancel, чтобы прекратить разговор.\n\n'
        'С какими числами будем работать?',
        reply_markup=markup_key,)
    # переходим к этапу `TYPE`, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список 
    # обработчиков, определенных в виде значения ключа `TYPE`
    return TYPE_N


    # Обрабатываем пол пользователя
def type_n(update, _):
    # Список кнопок для ответа
    reply_keyboard = [['ADD', 'SUB', 'MULTI', 'DIV', 'ROOT', 'SQRT']]
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал тип числа:
    logger.info("Тип %s: %s", user.first_name, update.message.text)
    # Следующее сообщение с удалением клавиатуры `ReplyKeyboardRemove`
    update.message.reply_text(
        'Хорошо. Что с ним будем делать?',
        reply_markup=ReplyKeyboardRemove(),
    )
    # переходим к этапу `PHOTO`
    return PHOTO




    if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(token)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher
    # Определяем обработчик разговоров `ConversationHandler` 
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            TYPE_N: [MessageHandler(Filters.regex('^(RATIONAL|COMPLEX)$'), type_n)],
            ACTION: [MessageHandler(Filters.regex('^(PLUS|MINUS|)$'), action)],
            LOCATION: [
                MessageHandler(Filters.location, location),
                CommandHandler('skip', skip_location),
            ],
            QUESTION: [MessageHandler(Filters.regex('^(Yes|No)$'), gender)],
            BIO: [MessageHandler(Filters.text & ~Filters.command, bio)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()
