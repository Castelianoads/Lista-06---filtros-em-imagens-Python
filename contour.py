from PIL import Image, ImageFilter

imagemOriginal = Image.open('imagens/Ave.jpg')

# O filtro CONTOUR faz um contorno aonde tem diferencia de cor entre os pixels
imagemComFiltro = imagemOriginal.filter(ImageFilter.CONTOUR)

imagemComFiltro.save('imagens/AveCONTOUR.jpg')