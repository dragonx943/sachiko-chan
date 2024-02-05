from discord.ext.commands import Cog
import discord

from io import StringIO
import json
import os

class Admin(Cog):
    def __init__(self, bot: discord.Bot):
        self.bot: discord.Bot = bot

    @discord.slash_command(description="Lệnh kêu gọi python lấy dữ liệu Chat mới nhất của bạn và Sachiko-chan")
    async def conversations(self, ctx: discord.ApplicationContext):
        if not await self.bot.is_owner(ctx.author):
            return await ctx.respond("`Bạn không có quyền để dùng lệnh này!`")

        cog = self.bot.cogs["Chat"]

        stream = StringIO(json.dumps(cog.conversations, indent=4))
        file = discord.File(stream, filename="conversations.json")

        await ctx.respond(file=file)

    @discord.slash_command(description="Dọn sạch cuộc trò chuyện giữa bạn và Sachiko-chan")
    async def clear(self, ctx: discord.ApplicationContext):
        if not await self.bot.is_owner(ctx.author):
            return await ctx.respond("`Bạn không có quyền để dùng lệnh này!`")

        # get the "Chat" cog
        cog = self.bot.cogs["Chat"]

        # clear the `conversations` dictionary
        cog.conversations = {}

        # respond to the admin
        await ctx.respond("`Đã dọn sạch lịch sử cuộc trò chuyện giữa bạn và Sachiko-chan!`")

def setup(bot: discord.Bot):
    bot.add_cog(Admin(bot))