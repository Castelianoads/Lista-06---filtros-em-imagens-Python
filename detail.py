from PIL import Image, ImageFilter

imagemOriginal = Image.open('imagens/Ave.jpg')

# O filtro DETAIL aumenta o detalhe na foto
imagemComFiltro = imagemOriginal.filter(ImageFilter.DETAIL)

imagemComFiltro.save('imagens/AveDETAIL.jpg')