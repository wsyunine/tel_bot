from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def Hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

app = ApplicationBuilder().token("7653536587:AAG7Tskt2zfDrRcLNMFjKi33pWGSa51QqSE").build()

app.add_handler(CommandHandler("hello", Hello))

app.run_polling()
