from PIL import Image

def toAscii(img,type,save_as,scale):

    scale = int(scale)
    #open image and get the image size
    image = Image.open(img)
    width, height = image.size

    #resize the image
    image.resize((width//scale,height//scale)).save("resized.%s" % type)

    #open the resized image
    image = Image.open("resized.%s" % type)
    width,height = image.size

    # list to store the pixels with correct length and height of resized image
    grid = []
    for i in range(height):
        grid.append(["X"] * width)

    pixels = image.load()

    for i in range(height):
        for j in range(width):
            if sum(pixels[j,i]) == 0 :
                grid[i][j] = "#"
            elif sum(pixels[j,i]) in range (1,100):
                grid[i][j]="X"
            elif sum (pixels[j,i]) in range (100,200):
                grid[i][j]="&"
            elif sum (pixels[j,i]) in range (200,300):
                grid[i][j]="$"
            elif sum (pixels[j,i]) in range (300,400):
                grid[i][j]="!"
            elif sum (pixels[j,i]) in range (400,500):
                grid[i][j]="?"
            elif sum (pixels[j,i]) in range (500,600):
                grid[i][j]="*"
            elif sum (pixels[j,i])in range (600,700):
                grid[i][j]="/"
            elif sum (pixels[j,i]) in range (700,750):
                grid[i][j]=":"
            else:
                grid[i][j]="."
    file = open(save_as,"w")
    for i in grid:
        file.write("".join(i) + "\n")
    file.close()



if __name__ == "__main__":
    toAscii("image.png","png","ascii.txt","2")  