from ezgraphics import GraphicsImage

def TransformaBW(in_file, out_file):
    origin = GraphicsImage(in_file)

    width = origin.width()
    height = origin.height()

    print(width, height)

    image_bw = GraphicsImage(width, height) #creo una nuova immagine con dei valori "scelti da me"

    #vedo tutti i pixel presenti nell'immagine
    for row in range(height):
        for col in range(width):
            pixel = origin.getPixel(row, col)
            print(pixel)
            #ricreo l'immagine
            media = (pixel[0] + pixel[1] + pixel[2]) // 3
            pixel_bw = (media,media,media)
            image_bw.setPixel(row,col,pixel_bw) 

    image_bw.save(out_file)

TransformaBW("criticita.png","Immagine di prova.png")