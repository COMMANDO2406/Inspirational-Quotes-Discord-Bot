import discord
from discord.ext import commands
import subprocess

BOT_TOKEN = "BOT_TOKEN"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if bot.user in message.mentions:
        await inspire(message)

async def inspire(message):
    # Execute main.py to generate the quote and image
    subprocess.run(['python', './src/image_gen.py'])

    # Send the image as a file on Discord
    with open('Outputs/Output.png', 'rb') as f:
        image_file = discord.File(f)
        await message.channel.send(file=image_file)

bot.run(BOT_TOKEN)
