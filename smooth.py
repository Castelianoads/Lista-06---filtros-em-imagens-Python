from PIL import Image, ImageFilter

imagemOriginal = Image.open('imagens/Ave.jpg')

# O filtro SMOOTH reduz pouco a irregularidade nos traços ou pixels
imagemComFiltro = imagemOriginal.filter(ImageFilter.SMOOTH)

imagemComFiltro.save('imagens/AveSMOOTH.jpg')