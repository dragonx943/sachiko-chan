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

# Chỉnh trạng thái hoạt động bao gồm: Số thành viên, Số máy chủ, Thời gian thực tế UTC+7, Đang nghe nhạc gì (Fake)
music_counter = 0
np_song = "Đang cập nhật / Updating..."

@tasks.loop(seconds=10) # Làm mới dữ liệu sau 15s
async def update_status():
    
    # Thuật toán đơn giản để bot random nhạc trong list
    global music_counter, np_song # Lấy biến bên ngoài
    songs_list = [ # List nhạc của Bot (Fake)
        ""
        ]

    music_counter += 10 # Giá trị được cộng thêm 15s mỗi lần update
    if music_counter >= 3600:  # Nếu đã qua 1 tiếng
        music_counter = 0 # Reset bộ đếm
        np_song = random.choice(songs_list) # Chọn ngẫu nhiên 1 bài trong List
    
    # Đồng hồ thực tế
    utc_offset = pytz.timezone('Asia/Ho_Chi_Minh')
    current_time_utc7 = datetime.datetime.now(utc_offset).strftime("%H:%M - %d/%m")
    
    # Đếm Members + Servers
    total_members = sum(guild.member_count for guild in bot.guilds)
    guild_count = len(bot.guilds)

    # Cuối cùng, gửi kết quả lên status
    activity_content = f"🌸 🖥️: {guild_count} ➼ 👥: {total_members} | 🕘 {current_time_utc7} 🌸"
    np = f"/status | 🎧: {np_song}"

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=np, state=activity_content))

@update_status.before_loop
async def before_update_status():
    await bot.wait_until_ready()

@bot.event
async def on_ready():
    update_status.start()

# Chạy Bot
bot.run(os.getenv("DISCORD_TOKEN"))
