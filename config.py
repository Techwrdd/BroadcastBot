import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5307169830:AAGQx5NwBq2gTobDh3rE1N6hKmVY1F9NU78")
API_ID = int(os.environ.get("API_ID", "14013342"))
API_HASH = os.environ.get("API_HASH", "c3e1d740fd207c7ae1b373a7546e8a62")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001892447203"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1128389435").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://akshatsg:AqI00eDwlRTekDvK@cluster0.1xyompx.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
