from PIL import Image



def resize_img(img: Image, size: int):
    resized_img = img.resize((size, size))
    return resized_img



img_512 = Image.open("pwa-512x512.png")
img_192 = resize_img(img_512, 192)
img_144 = resize_img(img_512, 144)
img_64 = resize_img(img_512, 64)

img_192.save("pwa-192x192.png")
img_144.save("pwa-144x144.png")
img_64.save("pwa-64x64.png")