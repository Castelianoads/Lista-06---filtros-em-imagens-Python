from PIL import Image, ImageFilter

imagemOriginal = Image.open('imagens/Ave.jpg')

# O filtro EMBOSS da profundidade nos objetos/ mostra o relevo
imagemComFiltro = imagemOriginal.filter(ImageFilter.EMBOSS)

imagemComFiltro.save('imagens/AveEMBOSS.jpg')