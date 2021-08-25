"""Meme_Engine Module.

The Meme Engine Module is responsible for manipulating and drawing
text onto images. It will reinforce your understanding of object-oriented
thinking while demonstrating your skill using a more advanced third party
library for image manipulation.

References:
https://knowledge.udacity.com/questions/637910
https://knowledge.udacity.com/questions/617136
https://knowledge.udacity.com/questions/562765
https://knowledge.udacity.com/questions/440307
https://knowledge.udacity.com/questions/634015
https://stackoverflow.com/questions/37901716/
flask-uploads-ioerror-errno-2-no-such-file-or-directory#:~:text=2%20Answers&text=Both%20%2
"""
from PIL import Image, ImageFont, ImageDraw
import random
import os

class MemeEngine:
        #class for generating meme
        def __init__(self, output_dir: str):
                #Initiate meme object
                os.makedirs(output_dir, exist_ok = True)
                self.output_dir = output_dir


        def make_meme(self, img_path, text, author, width=500):
                #Create Meme - Image
                img = Image.open(img_path)
                output = os.path.join(self.output_dir, f"{random.randint(0,1000000)}.jpg")
                ratio = img.size[1] / img.size[0]
                height = int(width * ratio)
                img = img.resize((width, height)

                #Create Meme - Text
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("arial.ttf", 20)
                draw.text((x_loc, y_loc), text, font = font, fill=(0, 0, 0))
                draw.text((int(x_loc*1.2), y_loc+font_size), " - "+author, font = font)
                img.save(output, 'jpeg')

                return output
