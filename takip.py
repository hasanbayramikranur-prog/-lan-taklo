import os
import json
import urllib.parse
import urllib.request
import urllib.error

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
if not TOKEN:
    raise SystemExit("TELEGRAM_BOT_TOKEN tanımlı değil")

def telegram(method, data=None):
    url = f"https://api.telegram.org/bot{TOKEN}/{method}"
    encoded = urllib.parse.urlencode(data).encode() if data else None
    try:
        with urllib.request.urlopen(url, data=encoded, timeout=30) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        print("HTTP HATASI:", e.code, e.read().decode())
        raise

print(telegram("getMe"))  # token doğru mu?
print(telegram("getWebhookInfo"))  # webhook var mı?

updates = telegram("getUpdates", {"limit": 10, "timeout": 0})
print("UPDATES:", json.dumps(updates, ensure_ascii=False))

last_id = None
for update in updates.get("result", []):
    last_id = update["update_id"]
    message = update.get("message") or update.get("channel_post")
    if message:
        chat_id = message["chat"]["id"]
        print("CHAT_ID:", chat_id)
        print(telegram("sendMessage", {
            "chat_id": chat_id,
            "text": "✅ İlan takip botu çalışıyor!"
        }))

# işlenen güncellemeleri sil
if last_id is not None:
    telegram("getUpdates", {"offset": last_id + 1})
