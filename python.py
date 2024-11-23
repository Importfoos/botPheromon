from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram import Update

# Команда /start
async def start(update: Update, context: CallbackContext) -> None:
    # Создаем кнопку "💎 Сдать товар 💎"
    keyboard = [[InlineKeyboardButton("💎 Сдать товар 💎", callback_data="surrender_item")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с кнопкой
    await update.message.reply_text(
        """
– Не хватает на депозит?  
– Срочно нужны деньги?  
– Никто не даёт в долг?  

Приму под залог твои NFT, физ. номера и многое другое.  

Быстрая выдача денег после осмотра, проверки и получения товара.  

Писать — @otrisovkin  
        """,
        reply_markup=reply_markup
    )

# Обработка нажатий на кнопку
async def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()  # Подтверждаем нажатие кнопки

    # Проверяем, какая кнопка нажата
    if query.data == "surrender_item":
        await query.edit_message_text(
            "💎 По поводу сдачи/выкупа товара обращаться к —> @otrisovkin 💎"
        )

def main():
    # Вставьте ваш токен
    TOKEN = "7879294195:AAFpD2kDI--oLPWFKTvUsHuNN7jEpLGbgrs"

    # Создание объекта приложения
    application = Application.builder().token(TOKEN).build()

    # Обработчики команд и кнопок
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()