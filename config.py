import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7485296857:AAEpfLsEF48O_-8iepYVI_wp2zhVMXaQLR4")
API_ID = int(os.environ.get("API_ID", "21189715"))
API_HASH = os.environ.get("API_HASH", "988a9111105fd2f0c5e21c2c2449edfd")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002231147120"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6798912985,1069898029,7181106700").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://ayanosuvii0925:subhichiku123@cluster0.uw8yxkl.mongodb.net/mydatabase")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
