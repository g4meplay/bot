from sys import stdout
from nextcord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        username = self.bot.user.name
        stdout.write(f"{self.bot.user.name}\n"); stdout.flush()


def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))
