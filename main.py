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

# Cập nhật trạng thái hoạt động của Sachiko-chan bao gồm số Servers đang tham gia và tổng số thành viên của tất cả Servers mà Sachiko-chan có mặt...
music_counter = 0
np_song = "Đang cập nhật..."

@tasks.loop(seconds=15) # Làm mới dữ liệu sau 15s
async def update_status():
    
    # Thuật toán đơn giản để bot random nhạc trong list
    global music_counter, np_song # Lấy biến bên ngoài
    songs_list = [ # List nhạc của Bot (Fake)
        "bài 1", "bài 2", "bài 3"
        ]

    music_counter += 15 # Giá trị được cộng thêm 15s mỗi lần update
    if music_counter >= 240:  # Nếu đã qua 4 phút
        music_counter = 0 # Reset bộ đếm
        np_song = random.choice(songs_list) # Chọn ngẫu nhiên 1 bài trong List
    
    # Đồng hồ thực tế
    utc_offset = pytz.timezone('Asia/Ho_Chi_Minh')
    current_time_utc7 = datetime.datetime.now(utc_offset).strftime("%H:%M")
    
    # Đếm Members + Servers
    total_members = sum(guild.member_count for guild in bot.guilds)
    guild_count = len(bot.guilds)

    # Cuối cùng, gửi kết quả lên status
    activity_content = f"🌸🌸 💻: {guild_count} máy chủ | 👥: {total_members} người 🌸🌸  🌸🌸 🕘 GMT+7: {current_time_utc7} | 🎧: {np_song}"
    await bot.change_presence(activity=discord.Game(name=activity_content))

@update_status.before_loop
async def before_update_status():
    await bot.wait_until_ready()

@bot.event
async def on_ready():
    update_status.start()

# Chạy Bot
bot.run(os.getenv("DISCORD_TOKEN"))
