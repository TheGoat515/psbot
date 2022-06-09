import os
import http

from flask import Flask, request
from werkzeug.wrappers import Response

from telegram import Bot, Update
from telegram.ext import Dispatcher, Filters, MessageHandler, CallbackContext

app = Flask(__name__)


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)
TOKEN="5406891094:AAGyWdXTL_rIVLeoOqjL0NGmU82W1Rj1y7E"
bot = Bot(TOKEN)

dispatcher = Dispatcher(bot=bot, update_queue=None)
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

def webhook(request):
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        # Reply with the same message
        bot.sendMessage(chat_id=chat_id, text=update.message.text)
    return "ok"

@app.post("/")
def index() -> Response:
    dispatcher.process_update(
        Update.de_json(request.get_json(force=True), bot))

    return "", http.HTTPStatus.NO_CONTENT

webhook
