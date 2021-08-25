import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1957412314:AAHCBXi8I1JeSPUsEG1HvW86z5H5410G8eU")

    APP_ID = int(os.environ.get("APP_ID", 6065291))

    API_HASH = os.environ.get("API_HASH", "dc7873c0a5c737af4356d4f245fe696d")
