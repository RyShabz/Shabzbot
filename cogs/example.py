import discord # discord.py
from discord.ext import commands 

class Example(commands.Cog):
    def __init__(self, client): #research __init__
        self.client = client
    
    # Events
    @commands.Cog.listener() #required for some reason
    async def on_ready(self): #self must be passed to all functions in class
        print('Bot is ready.')

    # Commands
    @commands.Command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

def setup(client):
    client.add_cog(Example(client))