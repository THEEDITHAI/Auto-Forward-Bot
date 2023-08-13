from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH" 887776e5d045135785b0fd48c757448e)
      API_ID = int(getenv("API_ID", 25683991))
      AS_COPY = True if getenv("AS_COPY", True) == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "6240531315:AAExcWNsoLkbfcPY-Un5rB13Zv1ZXKcwKZU")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1748225702").replace("\n", " ").split(' '))
