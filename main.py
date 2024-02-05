import discord
import openai
import dotenv

import logging
import os

from discord.ext import commands
client = discord.Client

# Tải file .env
dotenv.load_dotenv()

# Setup Output của Console
logging.basicConfig(
    level=logging.INFO,
    format="(%(asctime)s) [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    
    handlers=[
        logging.FileHandler(filename="discord.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# Lấy key OPENAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Khởi tạo Bot
intents = discord.Intents.default()

intents.message_content = True
intents.members = True

bot = discord.Bot(intents=intents)

# Lấy Prompt ChatGPT + Đặt biến
with open("prompt.txt", "r", encoding="utf-8") as file:
    bot.initial_prompt = file.read()

# Tải 3 lệnh của bot
bot.load_extension("cogs.events")
bot.load_extension("cogs.chat")
bot.load_extension("cogs.admin")

# Chỉnh trạng thái hoạt động của Bot dựa theo pycord: https://stackoverflow.com/questions/59126137/how-to-change-activity-of-a-discord-py-bot
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Tớ là Sachiko-chan, hiện giờ tớ cũng đang là bạn gái của cậu đó~~~"))
# Chạy Bot
bot.run(os.getenv("DISCORD_TOKEN"))