import os
import telebot
import yt_dlp
from flask import Flask
from threading import Thread

# 1. Tu Token real aquí
TOKEN = '8264125848:AAH_mIyzRB2nR8IwpqePWbyUEFxi6CZhRsE'
bot = telebot.TeleBot(TOKEN)
app = Flask('')

@app.route('/')
def home():
    return "Bot de Menfis funcionando"

def run():
    app.run(host='0.0.0.0', port=8080)

# 2. Función para descargar música
@bot.message_handler(commands=['musica'])
def descargar_musica(message):
    partes = message.text.split(' ', 1)
    if len(partes) < 2:
        bot.reply_to(message, "⚠️ Envía el link así: /musica [link de youtube]")
        return

    link = partes[1]
    msg = bot.reply_to(message, "⏳ Bajando audio... esto tarda un poquito.")

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
        
        os.remove('cancion.mp3') # Limpia la RAM de Render
        bot.delete_message(message.chat.id, msg.message_id)
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {str(e)}")

# 3. Encender el bot
if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    bot.polling()
    
