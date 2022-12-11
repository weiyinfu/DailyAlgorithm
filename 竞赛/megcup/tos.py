from PIL import Image

img = Image.open("bugpp_logo_2000.png")
data = img.getdata()
a = ['1' if i[0] else '0' for i in data]
open("bugpp.txt","w").write(''.join(a))
