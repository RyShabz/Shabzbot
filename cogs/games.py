import discord # discord.py
import random # for rng
from discord.ext import commands 

class Games(commands.Cog):
    def __init__(self, bot): #research __init__
        self.bot = bot
    
    # Magic 8 ball
    @commands.command(aliases = ['8ball']) # any string in the list can be used to invoke _8ball
    async def _8ball(self, ctx, *, question): # * is wildcard used to assume connect text with space as single argument, passed into what follows, in this case, question.
        responses = ['yeeaaaaa boiiiii',
                     'na bro',
                     'maybe baybe']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

def setup(bot):
    bot.add_cog(Games(bot))