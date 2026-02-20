import os
import telebot
from flask import Flask
from threading import Thread
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- CONFIGURACIÓN ---
TOKEN = '8264125848:AAH_mTy7R82mR8TwuqcPkbyUEXx6C7zhksE'
bot = telebot.TeleBot(TOKEN)
app = Flask('')

@app.route('/')
def home():
    return "Bot de Menfis funcionando con Plan B"

def run():
    app.run(host='0.0.0.0', port=8080)

# --- FUNCIÓN DE MÚSICA (PLAN B: SIN BLOQUEOS) ---
@bot.message_handler(commands=['musica', 'música'])
def enviar_link_descarga(message):
    partes = message.text.split(' ', 1)
    if len(partes) < 2:
        bot.reply_to(message, "⚠️ Envía el link así: /musica [link de youtube]")
        return

    link_original = partes[1]
    
    # Creamos un botón elegante para descargar fuera de YouTube
    markup = InlineKeyboardMarkup()
    # Usamos Dirpy que es excelente para bajar MP3 rápido
    link_directo = f"https://dirpy.com/from/{link_original}"
    
    btn = InlineKeyboardButton("⬇️ CLIC AQUÍ PARA DESCARGAR MP3", url=link_directo)
    markup.add(btn)

    bot.send_message(
        message.chat.id, 
        "✅ ¡Listo! Para evitar el bloqueo de YouTube, usa este convertidor rápido y seguro:", 
        reply_markup=markup
    )

# --- INICIO ---
if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    bot.polling()
    
