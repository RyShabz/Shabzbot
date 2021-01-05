import discord # discord.py
from discord.ext import commands, tasks
from itertools import cycle

class Tasks(commands.Cog):
    def __init__(self, bot): #research __init__
        self.bot = bot

status = cycle(['status 1', 'status 2'])

@commands.Cog.listener() #required for some reason
async def on_ready(self): #self must be passed to all functions in class
    change_status.start()
    print('task cog loaded')

@tasks.loop(seconds = 10)
async def change_status(self, bot):
    await bot.change_presence(activity = discord.Game(next(status)))

def setup(bot):
    bot.add_cog(Tasks(bot))