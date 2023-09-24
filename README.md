# Simulación de lo Clásico a lo Cuántico.

Esta librería de Python brinda funciones para llevar a cabo diferentes simulaciones de experimentos cuánticos. Adicionalmente se incluye una libreria de operaciones con numeros complejos, la cual permite manejar los numeros complejos y asi implementar las simulaciones.

## Requisitos
Antes de comenzar con la ejecución del material incluido en este repositorio, es necesario asegurarse de que se tiene instalado Python en su computador, debido a que este es el lenguaje en el cual esta desarrollado este repositorio. 

En caso de no tenerlo lleve a cabo los siguientes pasos:
1. Dirijase a la página https://www.python.org/downloads/
2. De click en la opción de descarga
   ![image](https://github.com/alexandrac1420/CNYT/assets/138069735/03d02dfb-a346-4bc8-8e9c-066816e2f80e)
3. Ejecute el programa que se descarga automáticamente.
4. Complete la instalacion.

## Operaciones Incluidas

La librería consta de las siguientes operaciones para vectores y matrices complejos, los números complejos parte de cada vector o matriz se representan por medio del tipo "complex" de la librería numpy de python, donde la primera componente es la parte real y la segunda, la imaginaria:

1. **Magnitud de una matriz de imaginarios:** `final_matrix(matrix)`
2. **Simulacón de un sistema probabilistico clasico:** `sistema_probabilistico(matrix, vectIni, clicks)`
3. **Simulacón de un sistema probabilistico cuantico:** `sistema_probabilistico_quantico(matrix, vectIni, clicks)`
4. **Simulación del experimento de canicas con coeficientes booleanos:** `canicas_booleanas(clicks, booleanMatrix, vectIni)`
4. **Simulación del experimento de multiples rendijas clásico:** `multiple_rendija_clasico(matrix, vectIni, clicks)`
5. **Simulación del experimento de multiples rendijas cuántico:** `multiple_rendija_cuantico(matrix, vectIni, clicks)`
6. **Graficar un diagrama de barras que muestra las probabilidades en porcentaje de un vector de estado, es posible guardar este diagrama como una imagen en tu computador:** `grafico(vector)`

## Uso
Para hacer uso del material deben llevar a cabo los siguientes pasos:
1. Abra la carpeta en donde desea guardar la librería.
2. De click derecho sobre dicha carpeta y seleccione la opción "Git Bash".
3. Clone el repositorio utilizando el comando "git clone" seguido del link brindado en la pagina principal del repositorio al presionar el boton verde "<>Code". 
2. Abre el proyecto en PyCharm.
3. Importa el módulo de la librería en tus scripts.
4. Utiliza las funciones de para realizar simulaciones de experimentos cuánticos.

## Ejemplo de Uso

```python
import matplotlib.pyplot as plt
import Classical_Quantum as cq

# Experimento canicas booleanas
boolean_Matrix = [[False, False, False, False, False, False], [True, False, False, False, False, True],
                         [True, False, False, False, False, False], [False, False, True, False, False, False],
                         [False, False, False, True, False, False], [False, False, False, False, True, False]]

vect_Ini = [True, False, False, False, False, False]
result = cq.canicas_booleanas(1,boolean_Matrix, vect_Ini)
print("Simulacion :",result)


```
## Autor
**Ing. Juan Sebastian Vasquez Vega**