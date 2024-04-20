import json
from PIL import Image, ImageDraw, ImageFont
import random


"""
# get quote from api
import requests
URL = "https://api.quotable.io/random"
r = requests.get(URL)
x = r.json()
"""

# load quotes from local JSON file
with open("Quotes/inspirational_from_quotable.json", "r") as file:
    quotes_data = json.load(file)

# choose a random quote from the loaded data
quote_data = random.choice(quotes_data)
quote = quote_data["quote"]
author = quote_data["author"]
print(quote)
print("- ", author)

# get image
x = (random.randint(1,14))
img_path = "Background-Images/{imagename}.jpg"
img = Image.open(img_path.format(imagename = x))

draw = ImageDraw.Draw(img)
width, height = img.size

# max quote width
max_quote_width = int(0.85 * width)

# initial font size
fontsize = 100
font = ImageFont.truetype("fonts/JetBrainsMonoNerdFont-Medium.ttf", fontsize)

# reduce font size until the quote fits within the max width
while font.getbbox(quote)[2] > max_quote_width:
    fontsize -= 1
    font = ImageFont.truetype("fonts/JetBrainsMonoNerdFont-Medium.ttf", fontsize)

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

# debug: img.show()
img.save("Outputs/Output.png", format="PNG")
