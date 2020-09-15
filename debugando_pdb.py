"""

PDB - Python Debugger

"""


def dividir(a, b):
    breakpoint()
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Valor Incorreto: {err}'


print(dividir(4, 7))
