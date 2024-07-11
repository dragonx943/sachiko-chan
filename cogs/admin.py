from discord.ext.commands import Cog
import discord

from io import StringIO
import json
import os

class Admin(Cog):
    def __init__(self, bot: discord.Bot):
        self.bot: discord.Bot = bot

    @discord.slash_command(description="Trích xuất dữ liệu từ Sachiko-chan / Extract data from Sachiko-chan (chỉ Dev dùng / Dev only!)")
    async def conversations(self, ctx: discord.ApplicationContext):
        if not await self.bot.is_owner(ctx.author):
            return await ctx.respond("Bạn không có quyền để dùng lệnh này! / You do not have permission to use this command!")

        cog = self.bot.cogs["Chat"]

        stream = StringIO(json.dumps(cog.conversations, indent=4))
        file = discord.File(stream, filename="logschat.json")

        await ctx.respond(file=file)

    @discord.slash_command(description="Xóa hết dữ liệu của Sachiko-chan / Clear all Sachiko-chan's data (chỉ Dev dùng / Dev only!)")
    async def clear(self, ctx: discord.ApplicationContext):
        if not await self.bot.is_owner(ctx.author):
            return await ctx.respond("Bạn không có quyền để dùng lệnh này! / You do not have permission to use this command!")

        cog = self.bot.cogs["Chat"]
        cog.conversations = {}

        await ctx.respond("`Đã dọn sạch lịch sử cuộc trò chuyện giữa bạn và Sachiko-chan!` / `Successfully cleared the conversation history.`")

    @discord.slash_command(description="Gửi tin nhắn đến tất cả các máy chủ / Send a message to all servers (chỉ Dev dùng / Dev only!)")
    async def note(self, ctx: discord.ApplicationContext):
        if not await self.bot.is_owner(ctx.author):
            return await ctx.respond("Bạn không có quyền để dùng lệnh này! / You do not have permission to use this command!")

        await ctx.respond("Vui lòng tải lên file note.txt chứa nội dung bạn muốn gửi cùng với ảnh nếu có.")

        def check(m):
            return m.author == ctx.author and len(m.attachments) > 0 and any(att.filename == 'note.txt' for att in m.attachments)

        msg = await self.bot.wait_for('message', check=check)
    
        note_attachment = next(att for att in msg.attachments if att.filename == 'note.txt')
        file_content = await note_attachment.read()
        message_content = file_content.decode('utf-8')
    
        image_attachment = None
        for att in msg.attachments:
            if att.filename != 'note.txt' and att.content_type.startswith('image/'):
                image_attachment = att
                break

        await ctx.send("Đang gửi tin nhắn đến tất cả các máy chủ... / Sending message to all servers...")

        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                try:
                    if image_attachment:
                        file = await image_attachment.to_file()
                        await channel.send(content=message_content, file=file)
                    else:
                        await channel.send(message_content)
                    break
                except discord.Forbidden:
                    continue

        await ctx.send("Tin nhắn đã được gửi đến tất cả các máy chủ! / Message sent to all servers!")

def setup(bot: discord.Bot):
    bot.add_cog(Admin(bot))