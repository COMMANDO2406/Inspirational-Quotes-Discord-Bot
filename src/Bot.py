import discord
from discord.ext import commands
import subprocess
from config import BOT_TOKEN
#import time

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if bot.user in message.mentions:
        #start_time = time.time()  # Record start time
        
        await inspire(message)
        
        # end_time = time.time()  # Record end time
        # elapsed_time = end_time - start_time
        # print(f"Time taken to process message and send image: {elapsed_time} seconds")

async def inspire(message):
    # Send the image as a file on Discord
    with open('Outputs/Output.png', 'rb') as f:
        image_file = discord.File(f)
        await message.channel.send(file=image_file)
        
    # Execute main.py to generate the quote and image
    subprocess.run(['python', './src/image_gen.py'])


bot.run(BOT_TOKEN)
