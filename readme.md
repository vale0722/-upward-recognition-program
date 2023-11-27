# Analizador Sintáctico en Python
## Descripción

Este proyecto consiste en un prototipo de programa de reconocimiento ascendente en Python, utilizando la biblioteca ply. El programa está diseñado para analizar y evaluar expresiones matemáticas, incluyendo la capacidad para manejar asignaciones a variables.

El código utiliza un lexer y un parser para procesar las cadenas de entrada, identificando tokens (como números, operadores, paréntesis) y aplicando reglas gramaticales para entender y evaluar la expresión.

## Objetivo
El objetivo principal de este proyecto es demostrar el análisis sintáctico de expresiones matemáticas y asignaciones de variables en Python, ofreciendo un ejemplo práctico de cómo se pueden implementar reconocedores sintácticos ascendentes.

## Alcance
El programa puede manejar:

- Números enteros y flotantes.
- Operaciones básicas: suma, resta multiplicación y división.
- Agrupación de operaciones mediante paréntesis.
- Asignación de valores a variables identificadas por nombres.
- Impresión del resultado final de la expresión o asignación.

## ¿Cómo Ejecutar?
Para ejecutar este programa, necesitarás Python y la biblioteca ply. Asegúrate de que ambos estén instalados en tu sistema.

### Instalación de ply:
Puedes instalar ply utilizando pip:
```
 pip install ply
```
### Ejecución:
Descarga el repositorio o copia y pega el código en un archivo .py y ejecútalo en tu entorno Python preferido.

```
 python main.py
```

## Uso:
Una vez ejecutado, el programa pedirá al usuario que ingrese una expresión matemática. Después de la entrada, el programa analizará la expresión y mostrará el resultado.

En el archivo parser.out podrás ver un ejemplo de tabla Go to generada

## Conclusiones

Este proyecto demuestra cómo se puede implementar un analizador sintáctico ascendente en Python para procesar expresiones matemáticas y asignaciones de variables. A través de la biblioteca ply, se facilita la creación de lexers y parsers, permitiendo una interpretación efectiva de las cadenas de entrada. El proyecto ofrece una base sólida para explorar conceptos más avanzados en el análisis sintáctico y puede ser extendido para manejar casos más complejos.