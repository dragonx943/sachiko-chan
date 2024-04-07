from discord.ext.commands import Cog, Context, command
import discord
import requests
import utilities

class Chat(Cog):
    def __init__(self, bot: discord.Bot):
        self.bot: discord.Bot = bot
        self.conversations: dict = {}

    @Cog.listener()
    async def on_message(self, message: discord.Message):
        # ignore messages sent by the bot
        if message.author == self.bot.user:
            return

        # ignore messages that aren't mentioning the bot
        if not utilities.is_mentioned(self.bot.user, message):
            return

        author = str(message.author.id)

        content = message.clean_content.replace(f"@{self.bot.user.name}", "")
        content = content.strip()

        if author not in self.conversations:
            self.conversations[author] = [{"role": "user", "content": self.bot.initial_prompt}]

        self.conversations[author].append({
            "role": "user", "content": content
        })

        with message.channel.typing():
            response = await utilities.chat_request(self.conversations[author])

        content = utilities.filter_markdown(response.content)

        # append the bot's response to the conversation
        self.conversations[author].append(response)

        # send the bot's response
        await message.reply(content, mention_author=False)

    @discord.slash_command(description="Tẩy não Sachiko-chan (Trong trường hợp câu từ của cô ấy mất kiểm soát)")
    async def forget(self, ctx: discord.ApplicationContext):
        author = str(ctx.author.id)

        if author in self.conversations:
            self.conversations[author] = [{"role": "user", "content": self.bot.initial_prompt}]

        await ctx.respond("`Đã dùng phép thuật tẩy não Sachiko-chan thành công thông qua ChatGPT API. Tag cô ấy = Tạo 1 cuộc trò chuyện mới!`")

    @discord.slash_command(description="Kiểm tra trạng thái hoạt động tại nơi Sachiko-chan đang làm việc!")
    async def status(self, ctx: discord.ApplicationContext):
        try:
            response = requests.get("#Trang web cần Ping để lấy status#")
            response.raise_for_status()  # Raise exception for non-200 status codes
            sachiko_status = f"Sachiko-chan vẫn đang làm việc chăm chỉ, cậu yên tâm nhé! **`(Đang hoạt động)`**"
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                sachiko_status = f"Sachiko-chan vẫn đang làm việc chăm chỉ, cậu yên tâm nhé! **`(Đang hoạt động)`**"
            else:
                sachiko_status = f"Sachiko-chan hiện đang vắng mặt ở chỗ làm...Oops! **`(Đang bảo trì)`**"
        except requests.exceptions.RequestException:
            sachiko_status = f"Sachiko-chan hiện đang vắng mặt ở chỗ làm...Oops! **`(Đang bảo trì)`**"
        await ctx.respond(sachiko_status)

    @discord.slash_command(description="Hỏi Sachiko-chan về độ trễ phản hồi (Ping)")
    async def ping(self, ctx: discord.ApplicationContext):
        latency = round(self.bot.latency * 1000)
        ping = f"**🏓 Pong! Sachiko-chan hiện đang phản hồi cậu ở độ trễ** **`{latency}ms`** **đó!**\n"
        await ctx.respond(ping)

def setup(bot: discord.Bot):
    bot.add_cog(Chat(bot))
