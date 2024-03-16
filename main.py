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

intents.presences = True
intents.guilds = True
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

# Cập nhật trạng thái hoạt động của Sachiko-chan bao gồm số Servers đang tham gia và tổng số thành viên của tất cả Servers mà Sachiko-chan có mặt...
async def update_status():
    total_members = sum(guild.member_count for guild in bot.guilds)
    guild_count = len(bot.guilds)
    await bot.change_presence(activity=discord.Game(name=f"Số máy chủ: {guild_count} | Số thành viên: {total_members}"))

@bot.event
async def on_ready():
    await update_status()

# Chạy Bot
bot.run(os.getenv("DISCORD_TOKEN"))
