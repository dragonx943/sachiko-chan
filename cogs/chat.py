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
        user = message.author.name
        if message.author == self.bot.user:
            return

        if not utilities.is_mentioned(self.bot.user, message):
            return

        author = str(message.author.id)

        content = message.clean_content.replace(f"@{self.bot.user.name}", "")
        content = content.strip()

        if author not in self.conversations:
            edited = self.bot.initial_prompt.replace("${user}", user)

            self.conversations[author] = [{"role": "user", "content": edited}]

        self.conversations[author].append({
            "role": "user", "content": content
        })

        with message.channel.typing():
            response = await utilities.chat_request(self.conversations[author])

        content = utilities.filter_markdown(response.content)
        self.conversations[author].append(response)
        await message.reply(content, mention_author=True)

    @discord.slash_command(description="Tẩy não Sachiko-chan / Delete your old chats with Sachiko-chan")
    async def forget(self, ctx: discord.ApplicationContext):
        author = str(ctx.author.id)

        if author in self.conversations:
            self.conversations[author] = [{"role": "user", "content": self.bot.initial_prompt}]

        await ctx.respond("`Đã xóa thành công!` / `Deleted successfully!`")

    @discord.slash_command(description="Kiểm tra trạng thái của Sachiko-chan / Check Sachiko-chan's status!")
    async def status(self, ctx: discord.ApplicationContext):
        status = f"**Chi tiết trạng thái / Status: **" # Đoạn này tự add
        await ctx.respond(status)

    @discord.slash_command(description="Hỏi Sachiko-chan về độ trễ phản hồi / Ask Sachiko-chan about her response delay (Ping)")
    async def ping(self, ctx: discord.ApplicationContext):
        latency = round(self.bot.latency * 1000)
        ping = f"**🏓 Pong! Độ trễ hiện tại / Delay messages output:** **`{latency}ms`**"
        await ctx.respond(ping)

    @discord.slash_command(description="Đóng góp ý kiến của bạn về Dev của Sachiko-chan / Send your feedback to Sachiko-chan's Dev!")
    async def feedback(self, ctx: discord.ApplicationContext, content: discord.Option(str, description="Hãy nhập tin nhắn mà bạn muốn gửi cho Dev! / Enter the message you want to send to Dev!")):
        with open('commit.txt', 'a', encoding='utf-8') as f:
            f.write(f'{ctx.author.name} - {ctx.author.id} - {content}\n')

        await ctx.respond('**`Đã gửi thành công!`** / **`Your message has been sent successfully!`**')

def setup(bot: discord.Bot):
    bot.add_cog(Chat(bot))