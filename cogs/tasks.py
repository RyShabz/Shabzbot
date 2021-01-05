import discord # discord.py
from discord.ext import commands, tasks
from itertools import cycle

class Tasks(commands.Cog):
    def __init__(self, bot): #research __init__
        self.bot = bot

status = cycle(['./help for help', 'hank says hank'])

@commands.Cog.listener()
async def on_ready(self):
    change_status.start()

@tasks.loop(seconds = 10)
async def change_status(self, bot):
    await bot.change_presence(activity = discord.Game(next(status)))

def setup(bot):
    bot.add_cog(Tasks(bot))