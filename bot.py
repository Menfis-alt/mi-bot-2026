import os
import telebot
import yt_dlp
from flask import Flask
from threading import Thread

# 1. CONFIGURACIÓN - Pon tu Token de BotFather aquí
TOKEN = '8264125848:AAH_mIyzRB2nR8IwpqePWbyUEFxi6CZhRsE'
bot = telebot.TeleBot(TOKEN)

# 2. EL PARCHE PARA QUE RENDER NO SE DUERMA
app_web = Flask('')
@app_web.route('/')
def home():
    return "¡El bot está encendido y trabajando!"

def run():
    app_web.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 3. FUNCIÓN PARA DESCARGAR MÚSICA
@bot.message_handler(commands=['musica'])
def descargar_musica(message):
    partes = message.text.split(' ', 1)
    if len(partes) < 2:
        bot.reply_to(message, "⚠️ Envía el link así: /musica https://www.youtube.com/...")
        return

    link = partes[1]
    msg = bot.reply_to(message, "⏳ Procesando audio... esto tarda un poquito.")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'cancion.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        
        with open('cancion.mp3', 'rb') as audio:
            bot.send_audio(message.chat.id, audio)
        
        # Limpiamos la memoria de 512MB
        if os.path.exists('cancion.mp3'):
            os.remove('cancion.mp3')
            
        bot.delete_message(message.chat.id, msg.message_id)
        
    except Exception as e:
        bot.edit_message_text(f"❌ Error: {str(e)}", message.chat.id, msg.message_id)

# 4. INICIO DEL BOT
if __name__ == "__main__":
    keep_alive() # Inicia la web de Flask
    print("Bot encendido correctamente")
    bot.polling()
    
