import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()  # Загружаем переменные из .env

TOKEN = os.getenv("TG_BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL", "http://localhost:8000/webapp")

if not TOKEN:
    raise RuntimeError("Отсутствует TG_BOT_TOKEN в переменных окружения!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Открыть мини-приложение", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    await update.message.reply_text("Привет! Вот твоё мини-приложение:", reply_markup=InlineKeyboardMarkup(keyboard))

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен. Нажми Ctrl+C для остановки.")
    app.run_polling()

if __name__ == "__main__":
    main()
