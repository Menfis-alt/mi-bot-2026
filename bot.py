import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- EL PARCHE PARA QUE NO SE DUERMA ---
# Esto crea una página web falsa para que Render crea que el bot es un sitio web.
app_web = Flask('')

@app_web.route('/')
def home():
    return "¡El bot está encendido y trabajando!"

def run():
    # Render usa el puerto 8080 por defecto en muchos casos
    app_web.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- FUNCIONES DEL BOT ---

async def inicio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Qué onda! Estoy funcionando desde la nube. ☁️")

async def eco(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Recibí: {update.message.text}")

# --- ARRANQUE ---
if __name__ == '__main__':
    # 1. Activamos el servidor web primero
    keep_alive()
    
    # 2. Configuramos el bot de Telegram
    TOKEN = "8264125848:AAH_mIyzRB2nR8IwpqePWbyUEFxi6CZhRsE"
    
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", inicio))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, eco))
    
    print("El bot y el servidor web están arrancando...")
    app.run_polling()
