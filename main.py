# main.py
import os
import telegram
token="5406891094:AAGyWdXTL_rIVLeoOqjL0NGmU82W1Rj1y7E"
def webhook(request):
    bot = telegram.Bot(token)
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        # Reply with the same message
        bot.sendMessage(chat_id=chat_id, text=update.message.text)
    return "ok"
