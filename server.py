import os
import urllib
import traceback
from flask import Flask, request
import telegram

app = Flask(__name__)
bot = telegram.Bot(os.getenv("BOT_TOKEN", default=None))


def check_auth(username, password):
    return username == os.getenv("AUTH_USERNAME", default=None) and password == os.getenv("AUTH_PASSWORD", default=None)

@app.route(f'/{os.getenv("ENDPOINT", default="alert")}', methods=["POST"])
async def alert(*kargs, **kwargs):
    try:
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return {'message': 'Authentication required'}, 401

        title = request.json['title']
        content = request.json['content']

        for c in ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']:
            content = content.replace(c, f'\\{c}')

        text = "\n".join([f"*{title}*", f"{content}"])

        async with bot:
            for user_id in os.getenv("RECEIVER_ID", default="").split():
                await bot.send_message(text=text, chat_id=user_id, parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)

        return {"status": "OK"}, 200

    except Exception as e:
        print(str(e))
        traceback.print_exc()

        return {'message': 'Internal Server Error'}, 500