from PIL import Image

img = Image.open("image_processing/luther.jpg")

pixels = img.load()

for y in range(img.height):
    for x in range(img.width):
        red, green, blue = pixels[x, y]

        # Invert each color channel
        inverted_color = (255 - red, 255 - green, 255 - blue)

        # Set the new inverted color
        pixels[x, y] = inverted_color

img.show()

img.save("image_processing/inverted_luther.jpg")
