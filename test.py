# messing around with discord.py
# https://github.com/Rapptz/discord.py
# https://discordpy.readthedocs.io/en/latest/index.html

import discord # discord.py
import random # for rng
import os
from discord.ext import commands, tasks

# initialize bot
botprefix = './'
bot = commands.Bot(command_prefix = botprefix)

# events. bot detects something happened. does a thing in response
@bot.event
async def on_ready(): # bot is ready for action
    await bot.change_presence(status = discord.Status.idle, activity = discord.Game(f'{botprefix}help for help'))# Bot Status displayed on Discord
    print('Bot is ready.')

@bot.event
async def on_member_join(member): # someone joined server
    print(f'{member} has joined us.')

@bot.event
async def on_member_remove(member): # someone left/kicked/etc server
    print(f'{member} has left us.')

# commands. Reads chat and does a thing in response to chat commands
@bot.command()
async def ping(ctx): # ctx is context. needed for all commands?
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms') # replies to ./ping with latency

@bot.command(aliases = ['8ball']) # any string in the list can be used to invoke _8ball
async def _8ball(ctx, *, question): # * is wildcard used to assume connect text with space as single argument, passed into what follows, in this case, question.
    responses = ['yeeaaaaa boiiiii',
                 'na bro',
                 'maybe baybe']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

# clear command
@bot.command()
async def clear(ctx, amount=1): #=1 is the default value if amount not specified
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Last {amount} messages deleted.')

# kick/ban command
@bot.command()
async def kick(ctx, member : discord.Member, *, reason='not logged'): 
    await member.kick(reason=reason)
    await ctx.send(f'Banned {member.mention} for {reason}.')

@bot.command()
async def ban(ctx, member : discord.Member, *, reason='not logged'): 
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention} for {reason}.')
    

# unban
@bot.command()
async def unban(ctx, *, member):
    banned_members = await ctx.guild.bans() #Get list of banned members, tuple
    member_name, member_discrim = member.split('#') #splits membername into name and discriminator membername#1234

    for ban_entry in banned_members:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discrim):#check if user matches desired unban.
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}.')
            return

# Cogs/extensions
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}') #[:-3] removes last 3 chars from filename, the .py

# turn on the bot
bot.run('') # token here ''