import discord
import emoji
from discord.ext import commands
client = discord.Client()
bot = commands.Bot(command_prefix = "!")
class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.Command()
    async def Kill_Server():
def setup(bot):
    bot.add_cog(events(bot))
