
import os
import urllib.parse
import urllib.request
import json

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

def telegram(method, data):
    url = f"https://api.telegram.org/bot{TOKEN}/{method}"
    encoded = urllib.parse.urlencode(data).encode()

    with urllib.request.urlopen(url, data=encoded) as response:
        return json.loads(response.read().decode())

updates = telegram("getUpdates", {})

for update in updates.get("result", []):
    message = update.get("message")

    if message:
        chat_id = message["chat"]["id"]

        telegram(
            "sendMessage",
            {
                "chat_id": chat_id,
                "text": "✅ İlan takip botu çalışıyor!"
            }
        )
