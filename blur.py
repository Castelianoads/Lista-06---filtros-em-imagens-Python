from PIL import Image, ImageFilter

imagemOriginal = Image.open('imagens/Ave.jpg')

# O filtro BLUR embaça a imagem
imagemComFiltro = imagemOriginal.filter(ImageFilter.BLUR)

imagemComFiltro.save('imagens/AveBlur.jpg')