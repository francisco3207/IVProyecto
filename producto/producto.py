'''Producto.py
'''

class Producto:
    '''Clase que representa el Producto

    El producto se define por el tipo de aceituna, el rendimiento base de ese
    tipo, y la fecha en la que se realizo el plantado.
    '''

    def __init__(self, tipo: str, kgs: float):
        '''Initializes the product
        '''
        self.tipo = tipo
        self.kgs_recogidos = 0

    def calcular_aceite(self, rendimiento) -> float:
        '''Calcula la cantidad de aceite que se obtendrá del producto
        recolectado y su rendimiento.
        '''
