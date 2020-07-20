from bot import telegram_chatbot

bot = telegram_chatbot('config.cfg')

update_id = None


while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None

            from_ = item["message"]["from"]["id"]
            first_name = item["message"]["from"]["first_name"]
            reply = bot.make_reply(message, first_name)
            bot.send_msgs(reply, from_)