from PIL import Image, ImageFilter

imagemOriginal = Image.open('imagens/Ave.jpg')

# O filtro SMOOTH_MORE reduz muito a irregularidade nos traços ou pixels
imagemComFiltro = imagemOriginal.filter(ImageFilter.SMOOTH_MORE)

imagemComFiltro.save('imagens/AveSMOOTH_MORE.jpg')