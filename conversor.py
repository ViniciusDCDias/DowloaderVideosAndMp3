from PIL import Image

img = Image.open("./images/icone.png")

img.save("./images/icone.ico",format="ICO",sizes=[(256,256)])