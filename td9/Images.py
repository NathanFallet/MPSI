from PIL import Image

def brighten(img: Image.Image, value: int) -> Image.Image:
    pixels = img.load()
    c, d = img.size
    output = Image.new("L", img.size)
    newPixels = output.load()
    for i in range(c):
        for j in range(d):
            newPixels[i,j] = pixels[i,j] + value
    return output

def contrast(img: Image.Image, limit: int, value: int) -> Image.Image:
    pixels = img.load()
    c, d = img.size
    output = Image.new("L", img.size)
    newPixels = output.load()
    for i in range(c):
        for j in range(d):
            newPixels[i,j] = pixels[i,j] + (-value if pixels[i,j]<limit else value)
    return output

def blur(img: Image.Image, size: int) -> Image.Image:
    pixels = img.load()
    c, d = img.size
    output = Image.new("L", img.size)
    newPixels = output.load()
    for i in range(c):
        for j in range(d):
            neighborsList = [pixels[a+i,b+j] for b in range(-size,size+1) for a in range(-size,size+1) if (a+i>=size and a+i<c-size and b+j>=size and b+j<d-size)]
            total = len(neighborsList)
            newPixels[i,j] = sum(neighborsList)//total
    return output

def outline(img: Image.Image, size: int) -> Image.Image:
    pixels = img.load()
    c, d = img.size
    output = Image.new("L", img.size)
    newPixels = output.load()
    for i in range(c):
        for j in range(d):
            neighborsList = [pixels[a+i,b+j] for b in range(-size,size+1) for a in range(-size,size+1) if (abs(a)+abs(b)!=0) and (a+i>=size and a+i<c-size and b+j>=size and b+j<d-size)]
            total = len(neighborsList)
            newPixels[i,j] = (total+1) * pixels[i,j] - sum(neighborsList)
    return output


toOpen = input("Which file do you want to open ? ")
image = Image.open("td9/" + toOpen + ".bmp")
newImage = brighten(image, 50)
newImage2 = contrast(image, 128, 30)
newImage3 = blur(image, 1)
newImage4 = outline(image, 1)
newImage.save("td9/" + toOpen + "_L.bmp")
newImage2.save("td9/" + toOpen + "_C.bmp")
newImage3.save("td9/" + toOpen + "_B.bmp")
newImage4.save("td9/" + toOpen + "_O.bmp")