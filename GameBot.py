import discord
from discord.ext import commands
from env import env

#ARACADE

#Set Up Permissions
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True  # Enable message content intent
intents.dm_messages = True
#https://discordpy.readthedocs.io/en/latest/intents.html

#Create instance of GameBot
bot = commands.Bot(command_prefix='!', intents=intents)

# Server Interaction ##############################################
@bot.event
async def on_ready():
    print('GameBot is ONLINE...')
    print('=======================================')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(env.TOKEN)

