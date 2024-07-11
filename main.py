import discord
import openai
import dotenv
import datetime
import pytz
import random
import logging
import os

from discord.ext import commands
from discord.ext import tasks
client = discord.Client

dotenv.load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="(%(asctime)s) [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)

openai.api_key = os.getenv("OPENAI_API_KEY")

intents = discord.Intents.default()

intents.presences = True
intents.guilds = True
intents.message_content = True
intents.members = True
intents.reactions = True

bot = discord.Bot(intents=intents)

with open("prompt.txt", "r", encoding="utf-8") as file:
    bot.initial_prompt = file.read()

bot.load_extension("cogs.events")
bot.load_extension("cogs.chat")
bot.load_extension("cogs.admin")

music_counter = 0
np_song = "Đang tải / Loading..."

@tasks.loop(seconds=10)
async def update_status():
    global music_counter, np_song
    songs_list = [ # Tự add tên nhạc vào đây để tạo trình phát ảo 
    ]

    music_counter += 10
    if music_counter >= 3600:
        music_counter = 0
        np_song = random.choice(songs_list)
    
    utc_offset = pytz.timezone('Asia/Ho_Chi_Minh')
    current_time_utc7 = datetime.datetime.now(utc_offset).strftime("%H:%M - %d/%m")
    total_members = sum(guild.member_count for guild in bot.guilds)
    guild_count = len(bot.guilds)
    activity_content = f"🌸 🖥️: {guild_count} ➼ 👥: {total_members} | 🕘 {current_time_utc7} 🌸"
    np = f"/status | 🎧: {np_song}"

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=np, state=activity_content))

@update_status.before_loop
async def before_update_status():
    await bot.wait_until_ready()

@bot.event
async def on_ready():
    update_status.start()

bot.run(os.getenv("DISCORD_TOKEN"))
