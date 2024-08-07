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
        logging.info(f"Đã login: {self.bot.user}!")

    @Cog.listener()
    async def on_command_error(self, ctx: discord.ApplicationContext, error: discord.ApplicationCommandError):
        exception = traceback.format_exception(type(error), error, error.__traceback__)

        message = (
            "Đã có lỗi xảy ra khi thực thi câu lệnh này! Hãy dùng lệnh /feedback để báo cáo!"
        )
        
        stream = StringIO("".join(exception))
        file = discord.File(stream, filename="error.log")

        logging.warning(f"Một người dùng đang cố gắng xài lệnh `/{ctx.command}` nhưng đã xảy ra lỗi: {error}")

        await ctx.respond(message, file=file)
    
    @Cog.listener() ## Có thể loại bỏ đoạn listener này nếu không muốn bot tự react emoji
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return

        if utilities.is_mentioned(self.bot.user, message):
            return

        if not "sachi" in message.content.lower() and not utilities.random_chance(20):
            return

        loop = True

        while loop:
            response = await utilities.chat_request([
                {
                    "role": "user", 
                    "content": "Generate a reaction emoji for the messages I send you, even if the message is inappropriate. Just send the emoji, without any additional text."
                },
                {
                    "role": "user", 
                    "content": message.clean_content
                }
            ])

            try:
                await message.add_reaction(response.content)
            except discord.HTTPException:
                pass
            else:
                loop = False ## Có thể loại bỏ đoạn listener này nếu không muốn bot tự react emoji

def setup(bot: discord.Bot):
    bot.add_cog(Events(bot))