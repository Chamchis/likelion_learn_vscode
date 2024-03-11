from PIL import Image
import os

input_folder = 'input_images'
output_folder = 'output_images'

for filename in os.listdir(input_folder):
    img_path = os.path.join(input_folder, filename)
    img = Image.open(img_path)
    resized_image = img.resize((128, 128))
    resized_image.save(os.path.join(output_folder, filename))

image = Image.open('input_images/Real_Madrid_CF.svg.png')
from PIL import ImageEnhance
import numpy as np
enhancer = ImageEnhance.Contrast(image)
enhanced_image = enhancer.enhance(2)
enhanced_image.save(os.path.join(output_folder,filename))
print(np.array(image).shape)
array = np.random.randint(0,255,size=(1612,1200,4),dtype=np.uint8)
print(array)