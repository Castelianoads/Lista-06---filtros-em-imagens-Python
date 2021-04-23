from PIL import Image, ImageFilter

imagemOriginal = Image.open('imagens/Ave.jpg')

# O filtro SHARPEN acentua os contorno
imagemComFiltro = imagemOriginal.filter(ImageFilter.SHARPEN)

imagemComFiltro.save('imagens/AveSHARPEN.jpg')