import discord # discord.py
from discord.ext import commands 

class Events(commands.Cog):
    def __init__(self, bot): #research __init__
        self.bot = bot

# When a new member joins the server
    @commands.Cog.listener()
    async def on_member_join(self, member): # someone joined server
        print(f'{member} has joined us.')

# When a member leaves or is removed from the server
    @commands.Cog.listener()
    async def on_member_remove(self, member): # someone left/kicked/etc server
        print(f'{member} has left us.')

# Add the cog
def setup(bot):
    bot.add_cog(Events(bot))