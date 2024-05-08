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
        file = discord.File(stream, filename="conversations.json")

        await ctx.respond(file=file)

    @discord.slash_command(description="Xóa hết dữ liệu của Sachiko-chan / Clear all Sachiko-chan's data (chỉ Dev dùng / Dev only!)")
    async def clear(self, ctx: discord.ApplicationContext):
        if not await self.bot.is_owner(ctx.author):
            return await ctx.respond("Bạn không có quyền để dùng lệnh này! / You do not have permission to use this command!")

        # get the "Chat" cog
        cog = self.bot.cogs["Chat"]

        # clear the `conversations` dictionary
        cog.conversations = {}

        # respond to the admin
        await ctx.respond("`Đã dọn sạch lịch sử cuộc trò chuyện giữa bạn và Sachiko-chan!` / `Successfully cleared the conversation history.`")

def setup(bot: discord.Bot):
    bot.add_cog(Admin(bot))