import discord # discord.py
from discord.ext import commands 

class Admin(commands.Cog):
    def __init__(self, bot): #research __init__
        self.bot = bot

    @commands.Cog.listener()

    # Pings bot and displays latency
    @commands.command()
    async def ping(self, ctx): 
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms') #how to reference top level bot from cog? is it self.bot?

    # Clear Command
    @commands.command()
    async def clear(self, ctx, amount = 1): #=1 is the default value if amount not specified
        await ctx.channel.purge(limit = amount)
        await ctx.send(f'Last {amount} messages deleted.')

    # Kick Command
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason='not logged'): 
        await member.kick(reason = reason)
        await ctx.send(f'Banned {member.mention} for {reason}.')

    # Ban Command
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason='not logged'): 
        await member.ban(reason = reason)
        await ctx.send(f'Banned {member.mention} for {reason}.')

    # unban
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_members = await ctx.guild.bans() #Get list of banned members, tuple
        member_name, member_discrim = member.split('#') #splits membername into name and discriminator membername#1234

        for ban_entry in banned_members:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discrim):#check if user matches desired unban.
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}.')
                return

def setup(bot):
    bot.add_cog(Admin(bot))



