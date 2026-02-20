import telebot
from flask import Flask
from threading import Thread
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# TOKEN de Menfis
TOKEN = '8264125848:AAH_mIyzRB2nR8IwpqePWbyUEFxi6CZhRsE'
bot = telebot.TeleBot(TOKEN)
app = Flask('')

@app.route('/')
def home():
    return "Bot de Menfis: Plan B Activado"

def run():
    app.run(host='0.0.0.0', port=8080)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "¡Hola! Para música usa /musica [link]")

@bot.message_handler(commands=['musica', 'música'])
def enviar_boton_descarga(message):
    partes = message.text.split(' ', 1)
    if len(partes) < 2:
        bot.reply_to(message, "⚠️ Envía el link así: /musica [link de youtube]")
        return

    link_original = partes[1]
    markup = InlineKeyboardMarkup()
    # Este link externo es el que salta el bloqueo
    url_descarga = f"https://dirpy.com/from/{link_original}"
    boton = InlineKeyboardButton("⬇️ DESCARGAR MP3 AQUÍ", url=url_descarga)
    markup.add(boton)

    bot.send_message(
        message.chat.id, 
        "✅ ¡Enlace generado! Toca el botón para descargar:", 
        reply_markup=markup
    )

if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    bot.polling()
    
