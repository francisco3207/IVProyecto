'''Producto.py
'''

class Producto:
    '''Clase que representa el Producto

    El producto se define por el tipo de aceituna, el rendimiento base de ese
    tipo, y la fecha en la que se realizo el plantado.
    '''

    def __init__(self, tipo: str, rendimiento_base: float, fecha_plantado):
        '''Initializes the product
        '''
        self.tipo = tipo
        self.rendimiento_base = rendimiento_base
        self.fecha_plantado = fecha_plantado
        self.kgs_recogidos = 0
        self.fecha_recolectado = None

    def recolectar(self, kgs_recogidos: float, fecha_recolectado):
        '''Indicar la cantidad de aceitunas tras su recolección

        kgs_recogidos: cantidad de aceituna recogida
        fecha_recolectado:

        '''
        self.kgs_recogidos = kgs_recogidos
        self.fecha_recolectado = fecha_recolectado

    def predecir_rendimiento(self, fecha) -> float:
        '''Calcular el rendimiento a partir del tipo de aceituna y del tiempo
        que llevará en el olivo y devolverá el porcentaje de rendimiento.
        fecha: momento sobre el que queremos predecir el rendimiento
        '''

    def calcular_aceite(self, fecha) -> float:
        '''Calcular la cantidad de aceite en kgs que se producirá a partir
        de la cantidad de aceitunas recogidas, segun el rendimiento en un
        momento dado.
        fecha: momento sobre el que queremos predecir (o calcular) el aceite
        producido segun el rendimiento
        Devuelve: cantidad de aceite
        '''

    def calcular_beneficio(self, kgs_mercado: float, precio_mercado: float) -> float:
        '''A partir de lo recogido y de los métodos anteriores, podemos saber el
        impacto que realiza nuestra cosecha en el mercado en el momento actual.
        kgs_mercado: kgs totales en el mercado
        precio_mercado: valor del kg de aceite en el mercado actual
        Devuelve el beneficio en euros

        '''
