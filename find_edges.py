from PIL import Image, ImageFilter

imagemOriginal = Image.open('imagens/Ave.jpg')

# O filtro FIND_EDGES os pixels ficam preto e branco
imagemComFiltro = imagemOriginal.filter(ImageFilter.FIND_EDGES)

imagemComFiltro.save('imagens/AveFIND_EDGES.jpg')