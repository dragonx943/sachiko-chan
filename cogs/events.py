from discord.ext.commands import Cog
import discord

from io import StringIO
import traceback
import logging

import utilities

class Events(Cog):
    def __init__(self, bot: discord.Bot):
        self.bot: discord.Bot = bot
    
    @Cog.listener()
    async def on_ready(self):
        logging.info(f"Đã login dưới cái tên Acc Discord: {self.bot.user}!")

    @Cog.listener()
    async def on_command_error(self, ctx: discord.ApplicationContext, error: discord.ApplicationCommandError):
        exception = traceback.format_exception(type(error), error, error.__traceback__)

        message = (
            "Đã có lỗi xảy ra khi thực thi câu lệnh này!\n"
            "Hãy gửi file dưới đây cho người tạo ra Bot để báo cáo lỗi:\n"
        )
        
        stream = StringIO("".join(exception))
        file = discord.File(stream, filename="error.log")

        logging.warning(f"Một người dùng đang cố gắng xài lệnh `/{ctx.command}` nhưng đã xảy ra lỗi: {error}")

        await ctx.respond(message, file=file)

def setup(bot: discord.Bot):
    bot.add_cog(Events(bot))