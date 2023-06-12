from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", 7949855))
API_HASH = getenv("API_HASH", "ea4403a7f9496b9b39fdb6401f32c46b")
BOT_TOKEN = getenv("BOT_TOKEN", "5906095024:AAGlxiXI9cZErchTNL1n9-47pNJFfAzdsSg")
OPENAI_API = getenv("OPENAI_API", "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") # get api key : https://platform.openai.com/account/api-keys
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://sudo:sudo@cluster0.fxka6ep.mongodb.net/?retryWrites=true&w=majority") # required https://mongodb.com
ADMINS = int(getenv("ADMINS", 5329521369))
