# This is a basic discord bot it can be customized alot for use and there are ton of commands which we can use and assign to increase our discord server members experience.

# Imports
import discord
from discord.ext import commands

# # Intents
# intents = discord.Intents.default()
# intents.message_content = True
#
# # Discord Client
# client = discord.Client(intents=intents)

# Bot commands
# assigning bot command prefix to write commands
bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')
# Discord token
my_dic_token = 'your token'


# Writing first command
@bot.command(name='hello')
async def on_message(message):
    # Hello function
    await  message.channel.send(f'Hello {message.author}')


# Member Join welcome message
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"""Hi {member.name}, welcome to my Discord server.
        I am a bot of ServerName.
        Here to help type "$help" in general chat to get help"""
    )

# !complaint
@bot.command(name='complaint')
async def on_message(message):
    await message.channel.send(
        f'Hey @{message.author} our mod will acknowledge you asap. And for anything else you can check "!command" to list all the commands ')


# !commands
@bot.command(name='commands')
async def on_message(message):
    await message.channel.send(
        f'Here all the commands @{message.author}.')


# call the main bot function to run our bot.
bot.run(my_dic_token)
