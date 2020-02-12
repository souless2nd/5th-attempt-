import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import datetime
import emoji
import os
import random
client = discord.Client()
bot = commands.Bot(command_prefix = "!")
bot.remove_command("help")
@bot.event
async def on_ready():
    print("Im online")
    Bot.wait_until_ready
    client.wait_until_ready
    game = discord.Game("with your feelings")
    guild = bot.get_guild(37559707194392603)
    await bot.change_presence(status=discord.Status.online, activity=game)
extenstions = []
if __name__ == '__main__':
    for extension in extenstions:
        try:
            bot.load_extension(extension)
            print(extension)
        except Exception as error:
            print(error)
bot.run(os.environ['token'])
