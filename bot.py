# Ahora combinamos el archivo precios.py y bot.py para que cada vez que escribamos /precios nos devuelva los datos del dia
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from precios import obtener_precios

bot_token = "tu token"

# Updater se encarga de interpretar los mensajes que le envian al bot
# dispatcher manipula/controla dichos mensajes
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

# Le damos los parametros a seguir al bot
def start(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = obtener_precios()
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        precio = crypto_data[i]["precio"]
        variacion_dia = crypto_data[i]["variacion_dia"]
        variacion_hora = crypto_data[i]["variacion_hora"]
        minimo = crypto_data[i]["minimo"]
        maximo = crypto_data[i]["maximo"]
        message += f"Coin: {coin}\nPrecio: ${precio:,.2f}\nVariacion hora: {variacion_hora:.2f}%\nVariacion dia: {variacion_dia:.2f}%\nMinimo: {minimo:.2f}\nMaximo: {maximo:.2f}\n\n"

    context.bot.send_message(chat_id=chat_id, text=message)

# Bloque de codigo que se activa cuando el usuario escribe "/precios"
dispatcher.add_handler(CommandHandler("precios", start))
updater.start_polling()
