from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./images/"
pathOut = "edited_images/"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert("RGB")

    factor = 1.2  # Example factor for brightness
    enhancer = ImageEnhance.Brightness(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f".{pathOut}/{clean_name}_edited.jpg", "JPEG")