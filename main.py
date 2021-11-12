from PIL import Image

if __name__ == '__main__':
    

    image = Image.open('./images/rosa.jpg')

    print(image.size) #Devuelve el ancho y el alto en una tupla

    width, height = image.size

    print(f"ancho: {width}px")
    print(f"alto: {height}px")

    print(image.mode)

    #image.show()