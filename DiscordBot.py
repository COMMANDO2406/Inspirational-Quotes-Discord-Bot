import requests
from PIL import Image, ImageDraw, ImageFont
import random
import discord
from discord.ext import commands

BOT_TOKEN = "YOUR_DISCORD_BOT_TOKEN"
# If you want to test out this bot you can read BOT_SETUP.md for instructions on how to run this

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def inspire(ctx):
    # get quote
    URL = "https://api.goprogram.ai/inspiration"
    r = requests.get(URL)
    x = r.json()

    quote = x["quote"]
    author = x["author"]

    # get image
    x = (random.randint(1, 11))
    img_path = "Background-Images/{imagename}.jpg"
    img = Image.open(img_path.format(imagename=x))

    draw = ImageDraw.Draw(img)
    width, height = img.size

    fontsize = 30
    font = ImageFont.truetype("arial.ttf", fontsize)

    max_width = int(0.8 * width)

    # quote text-box positional logic
    quote_bbox = draw.textbbox((0, 0), quote, font=font)
    quote_width = quote_bbox[2] - quote_bbox[0]
    quote_height = quote_bbox[3] - quote_bbox[1]
    quote_x = (width - quote_width) // 2
    quote_y = (height - quote_height) // 2

    # author text-box positional logic
    author_bbox = draw.textbbox((0, 0), author, font=font)
    author_width = author_bbox[2] - author_bbox[0]
    author_height = author_bbox[3] - author_bbox[1]
    author_x = (width - author_width) // 2
    author_y = quote_y + author_height + 20

    # draw onto the image
    draw.text((quote_x, quote_y), quote, font=font, fill='white')
    draw.text((author_x, author_y), "- " + author, font=font, fill='white')

    # Save the image to a file
    img_path = 'Output.png'
    img.save(img_path, format="PNG")

    # Send the image as a file on Discord
    with open(img_path, 'rb') as f:
        image_file = discord.File(f)
        await ctx.send(f'"{quote}" - {author}', file=image_file)

    img.show()

bot.run(BOT_TOKEN)
