import sys
import os
from PIL import Image

path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(path):
    new_image = os.path.splitext(filename)[0]
    img = Image.open(f'{path}{filename}')
    img.save(f'{directory}/{new_image}.png', 'png')
    print('Done with converting !')
    
"""
To run this script in console:
   > python imgConverter_cli.py 'img dir/' 'new dir/' 
"""
