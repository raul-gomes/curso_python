"""

colorama - utilizado para permitir impressçao de textos coloridos no terminal

Pacotes achador no site ""https://pypi.og

from colorama import (init,
                      Fore,
                      Back,
                      Style)
init()

print(Fore.BLUE + 'some red text')
print(Back.BLACK + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
"""

import pydf

pdf = pydf.generate_pdf('<h1>Estudar Python </h1> <br/><h2><strong>by Geek University</strong></h2')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)

