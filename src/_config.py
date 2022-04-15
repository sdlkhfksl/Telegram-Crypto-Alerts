import requests
import os

"""Telegram Preferences:"""
# No-space comma-separated list of Telegram group IDs:
TELEGRAM_GROUP_IDS: list = os.environ.get("TELEGRAM_GROUP_IDS", 'group-id,group-id').split(',')

# No-space comma-separated list of Telegram user IDs:
TELEGRAM_ADMIN_IDS: list = os.environ.get("TELEGRAM_ADMIN_IDS", 'admin-id,admin-id').split(',')


# Telegram bot token string (see https://core.telegram.org/bots/api#authorizing-your-bot):
TELEGRAM_BOT_TOKEN: str = os.environ.get("TELEGRAM_BOT_TOKEN", 'your-bot-token-here')

"""Alerts Preferences:"""
DELETE_ALL_ALERTS = True  # Delete alerts from the database after they have been fulfilled
PRICES_POLLING_PERIOD = 10  # Polling period in seconds to check the pair prices
PERCENT_CHG_ALERT_RESET = 5  # (AS A % ie 5% = 5) Percent change of the ticker to reset the PCTCHG alert

"""CHECKS"""
if TELEGRAM_ADMIN_IDS == ['admin-id', 'admin-id']:
    raise ValueError("TELEGRAM_ADMIN_IDS is not set")
if TELEGRAM_GROUP_IDS == ['group-id', 'group-id']:
    raise ValueError("TELEGRAM_GROUP_IDS is not set")
if TELEGRAM_BOT_TOKEN == 'your-bot-token-here':
    raise ValueError("TELEGRAM_BOT_TOKEN is not set")


"""Used to get available telegram chat IDs:"""
if __name__ == "__main__":
    """to get updates, the chat must be a DM or a /command in a group chat"""
    resp = requests.get(f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates')
    print(resp.text)
