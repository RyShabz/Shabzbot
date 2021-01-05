# messing around with discord.py
# https://github.com/Rapptz/discord.py
# https://discordpy.readthedocs.io/en/latest/index.html

import discord # discord.py
import os
from discord.ext import commands, tasks

# initialize bot
botprefix = './'
bot = commands.Bot(command_prefix = botprefix)

# Bot signals it is ready
@bot.event
async def on_ready(): # bot is ready for action
    await bot.change_presence(status = discord.Status.idle, activity = discord.Game(f'{botprefix}help for help'))# Bot Status displayed on Discord
    print('Bot is ready.')

# Cogs/extensions
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

# loads all the cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}') #[:-3] removes last 3 chars from filename, the .py

# turn on the bot
bot.run('') # token here as string