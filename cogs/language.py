import discord # discord.py
import numpy as np
import pandas as pd
from discord.ext import commands 

class Example(commands.Cog):
    def __init__(self, bot): #research __init__
        self.bot = bot

# ------ Insert code to run between here ------
# @commands.Cog.listener() for events
# @commands.Command() for commands
    # Create dataframe of known translations


    @commands.Command()
    async def translate(self, ctx, msgid, sourceLang, aliases = ['rule6']): # bot is ready for action
        df = pd.DataFrame(
        ['English', 'Per Rule 6 in #Rules, English is the only language allowed on the server.'],
        index = [0,1],
        columns = ['language', 'text']
        )
        
        for df.column in df['language']:
            if df.item == sourceLang:
                await ctx.send(df.item[1])
            else:
                pass #look up google translate api
            return

    

# --------------- and here --------------------

def setup(bot):
    bot.add_cog(Example(bot))