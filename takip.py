import os
import urllib.parse
import urllib.request

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

print("Bot testi başladı")

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

with urllib.request.urlopen(url) as response:
    print(response.read().decode())
