from PIL import Image, ImageFilter

image = Image.open("File path")

# image filters
filtered_img1 = image.filter(ImageFilter.BLUR)
filtered_img1.save("blur_img.png", 'png')
filtered_img2 = image.filter(ImageFilter.SHARPEN)
filtered_img2.save("sharpen_img.png", 'png')

# color conversion
conv_image = image.convert('L')  # Grayscale
conv_image.save("grey_img.png", "png")

# rotate
rotated_img = image.rotate(180)
rotated_img.save("temp2.png", "png")

# crop 
regions = (250, 250, 550, 550)
cropped_img = image.crop(regions)
cropped_img.save("crop_img.png", "png")

# thumbnail() - preserves the aspect ratio and compresses the image size 
image.thumbnail((450, 450))
image.save("thumbnail.png")

# resize
resized_img = image.resize((450, 450))
resized_img.save("temp1.png", "png")



