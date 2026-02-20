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
    return "Bot de Menfis: Plan B Activado"

def run():
    app.run(host='0.0.0.0', port=8080)

# --- FUNCIÓN DE MÚSICA (ESTA NO FALLA) ---
@bot.message_handler(commands=['musica', 'música'])
def enviar_boton_descarga(message):
    partes = message.text.split(' ', 1)
    if len(partes) < 2:
        bot.reply_to(message, "⚠️ Envía el link así: /musica [link de youtube]")
        return

    link_original = partes[1]
    
    # Creamos el botón de descarga externa
    markup = InlineKeyboardMarkup()
    # Usamos un servicio confiable para la conversión
    url_descarga = f"https://dirpy.com/from/{link_original}"
    
    boton = InlineKeyboardButton("⬇️ DESCARGAR MP3 AQUÍ", url=url_descarga)
    markup.add(boton)

    bot.send_message(
        message.chat.id, 
        "✅ ¡Enlace listo! Para evitar el bloqueo de YouTube, toca el botón de abajo para bajar tu música:", 
        reply_markup=markup
    )

# --- INICIO ---
if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    bot.polling()
    
