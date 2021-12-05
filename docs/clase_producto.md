# Clase producto

Para representar los cultivos, se ha creado una clase _producto_.
Se ha llamado _producto_, ya que es la palabra que mejor define al cultivo tanto durante su crecimiento como después de su recogida. 

En este caso, _producto_ será un objeto-valor, no tienen una identidad (pueden existir 2 productos/cosechas/cultivos con los mismos atributos), sino que son representados completamente por sus atributos, que, una vez asignados, son inmutables. 

Esta clase, respaldará la [HU1](https://github.com/francisco3207/IVProyecto/issues/7), porque contendrá valores necesarios para poder calcular el valor de la cosecha.

Mediante el uso de una clase _Producto_, que contenga información sobre el tipo de aceituna plantada y sobre la cosecha, podremos almacenar los datos que definan una cosecha.
- tipo
- rendimiento_base
- fecha_plantado
- kgs_recogidos
- fecha_recogida

Además a partir de esos datos y otros datos, ajenos a una cosecha en concreto (fecha sobre la que predecir, mercado actual) podremos calcular los valores necesarios que servirán para realizar las predicciones. Hablo de los métodos:
- predecir_rendimiento, a partir de los datos de nuestra cosecha y el momento sobre el que predecir
- calcular_aceite
- calcular_beneficio, a partir de los datos de la cosecha y del mercado, es el objetivo de [M1](https://github.com/francisco3207/IVProyecto/milestone/2)
