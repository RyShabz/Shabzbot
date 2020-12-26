# messing around with discord.py
# https://github.com/Rapptz/discord.py
# https://discordpy.readthedocs.io/en/latest/index.html

import discord # discord.py
import random # for rng
from discord.ext import commands 

# initialize bot
bot = commands.Bot(command_prefix = './')

# events. bot detects something happened. does a thing in response
@bot.event
async def on_ready(): # bit is ready for action
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
    await ctx.send(f'last {amount} messages deleted')

# kick/ban command
@bot.command()
async def kick(ctx, user : discord.Member, *, reason='not logged'): 
    await user.kick(reason=reason)

@bot.command()
async def ban(ctx, user : discord.Member, *, reason='not logged'): 
    await user.ban(reason=reason)

# turn on the bots
bot.run('') # token here