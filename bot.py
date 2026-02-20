# --- NUEVA FUNCIÓN DE MÚSICA (SIN BLOQUEOS) ---
@bot.message_handler(commands=['musica', 'música'])
def descargar_musica(message):
    partes = message.text.split(' ', 1)
    if len(partes) < 2:
        bot.reply_to(message, "⚠️ Envía el link así: /musica [link de youtube]")
        return

    link_original = partes[1]
    
    # Creamos un botón elegante
    from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
    markup = InlineKeyboardMarkup()
    
    # Este link usa un servicio que salta todos los bloqueos de YouTube
    link_directo = f"https://cobalt.tools/api/json" 
    # Para no complicarte con APIs, usaremos un link de descarga directa web:
    descarga_web = f"https://dirpy.com/from/{link_original}"

    btn = InlineKeyboardButton("⬇️ CLIC AQUÍ PARA DESCARGAR MP3", url=descarga_web)
    markup.add(btn)

    bot.reply_to(message, 
                 "✅ ¡Listo! YouTube no me deja enviarte el archivo directo, pero aquí tienes tu link de descarga rápida sin anuncios:", 
                 reply_markup=markup)
    
    
