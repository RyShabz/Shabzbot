import discord # discord.py
from discord.ext import commands 

class Example(commands.Cog):
    def __init__(self, bot): #research __init__
        self.bot = bot

    @commands.Cog.listener()
# ------ Insert code to run between here ------
# @commands.Cog.listener() for events
# @commands.Command() for commands
  
    @commands.Cog.listener()
    # Example code. Always pass 'self' as first argument. Indent.    
    async def on_ready(self): # bot is ready for action
        print('Bot is ready.')

# --------------- and here --------------------

def setup(bot):
    bot.add_cog(Example(bot))