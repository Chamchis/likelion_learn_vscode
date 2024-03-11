from PIL import Image

# 이미지 열기
image = Image.open('Real_Madrid_CF.svg.png').convert("RGB")

print(image)

image.save('output.jpg')

# 이미지 회전
rotated_image = image.rotate(180)
rotated_image.save('rotated.jpg')

bw_iamge = image.convert("L")
bw_iamge.save("gray.jpg")

cropped_image = image.crop((100, 100, 400, 400))
cropped_image.save("cropped.jpg")

from PIL import ImageDraw,ImageFont

image_new = Image.open('Real_Madrid_CF.svg.png').convert("RGB")

draw = ImageDraw.Draw(image_new)
font = ImageFont.load_default()

draw.text((10,10), "Python Backend", fill="white", font=font)
image_new.save("text_added.jpg")

from PIL import ImageFilter

image = Image.open('Real_Madrid_CF.svg.png').convert("RGB")
blurred_image = image.filter(ImageFilter.SHARPEN)
blurred_image.save('blurred.jpg')

import os
