from PIL import Image
import os


def crop_img(img: Image, left:int, upper:int, right:int, lower: int):
    cropped_img = img.crop((left, upper, right, lower))
    return cropped_img


original_path = "../frontend/assets/login/bg_en2.jpg"
img_original = Image.open(original_path)
img_cropped = crop_img(img_original, 100, 0, 2000, img_original.height)

new_path = os.path.split(original_path)[:-1]
# new_path.append("smart_phone_bg.jpg")
img_cropped.save(os.path.join(*new_path, "smart_phone_bg_en2.jpg"))
