from PIL import Image, ImageFilter

imagemOriginal = Image.open('imagens/Ave.jpg')

# O filtro EDGE_ENHANCE realça um pouco os pixels
imagemComFiltro = imagemOriginal.filter(ImageFilter.EDGE_ENHANCE)

imagemComFiltro.save('imagens/AveEDGE_ENHANCE.jpg')