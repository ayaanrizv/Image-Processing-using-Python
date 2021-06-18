from PIL import Image, ImageFilter
# img = Image.open('.\\pokedex\\4.4 pikachu.jpg')
# print(img) returns image object
# print(img.format)  # returns format of image
# print(img.size)  # returns size
# print(img.mode)  # returns mode for ex RGB etc
# img.show() --> shows the image
# filtered_img = img.filter(ImageFilter.BLUR)  # img is Blur, ImageFilter.SMOOTH makes image smoother, .SHARPEN
# filtered_img.save("blur.png", 'png')
# filtered_img2 = img.convert("L")  # makes image in L color space
# filtered_img2.save("grey.png", 'png')
# box = (100,100,400,400)
# region = filtered_img.crop(box)
# region.save("cropped.png", 'png')
# filtered_img3 = img.filter(ImageFilter.SHARPEN)
# filtered_img3.save("pika.png", 'png')
img2 = Image.open('.\\6.1 astro.jpg')
# print(img2.size) (5611,5339)
img2.thumbnail((400, 400))  # resize doesn't maintain aspect ratio so we use thumbnail which maintains aspect ration
img2.save("resized_astro.png", 'png')
