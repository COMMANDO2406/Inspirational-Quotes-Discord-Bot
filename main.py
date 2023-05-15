import requests
from PIL import Image, ImageDraw, ImageFont, ImageColor
import random

# get quote
URL = "https://api.goprogram.ai/inspiration"
r = requests.get(URL)
x = r.json()
# print(x)
quote = x["quote"] 
author = x["author"]
print(quote)
print("- ", author)

# get image
x = (random.randint(1,11))
img_path = "Background-Images/{imagename}.jpg"
img = Image.open(img_path.format(imagename = x))

draw = ImageDraw.Draw(img)
width, height = img.size

fontsize = 30
font = ImageFont.truetype("arial.ttf", fontsize)

max_width = int(0.8 * width)

# quote box spaghetti inefficient code
quote_bbox = draw.textbbox((0, 0), quote, font=font)
quote_width = quote_bbox[2] - quote_bbox[0]
quote_height = quote_bbox[3] - quote_bbox[1]
quote_x = (width - quote_width) // 2
quote_y = (height - quote_height) // 2

# author box spaghetti inefficient code
author_bbox = draw.textbbox((0, 0), author, font=font)
author_width = author_bbox[2] - author_bbox[0]
author_height = author_bbox[3] - author_bbox[1]
author_x = (width - author_width) // 2
author_y = quote_y + author_height + 20

# draw onto the image
draw.text((quote_x, quote_y), quote, font=font, fill='white')
draw.text((author_x, author_y), "- " + author, font=font, fill='white')

img.show()
img.save("Output.png", format="PNG")