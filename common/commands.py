import nextcord
from nextcord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @nextcord.slash_command(name="ping", description="Mostra o ping do bot")
    async def ping(self, interaction: nextcord.Interaction):
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! {latency}ms")


def setup(bot: commands.Bot):
    bot.add_cog(Commands(bot))
