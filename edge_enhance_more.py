from PIL import Image, ImageFilter

imagemOriginal = Image.open('imagens/Ave.jpg')

# O filtro EDGE_ENHANCE_MORE realça muito os pixels
imagemComFiltro = imagemOriginal.filter(ImageFilter.EDGE_ENHANCE_MORE)

imagemComFiltro.save('imagens/AveEDGE_ENHANCE_MORE.jpg')