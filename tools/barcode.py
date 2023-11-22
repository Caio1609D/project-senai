# 987412563210
# pip instal python-barcode

import barcode
from barcode.writer import ImageWriter 



number = input("Digite aqui seu codigo ")

barcode_formato = barcode.get_barcode_class ('upc')

meu_codigo_bar = barcode_formato (number , writer=ImageWriter())

# Salvando imagem

meu_codigo_bar.save('meu_primeiro_bar_code')