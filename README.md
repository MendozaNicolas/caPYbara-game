# CaPYbara Game

![Preview](/preview.png)
<br>
<br>

**Juego creado** en **Python** usando la libreria **Pygame**! 


## Tabla de contenidos

- [CaPYbara Game](#capybara-game)
  - [Tabla de contenidos](#tabla-de-contenidos)
  - [Descripción](#descripción)
  - [Sobre el proyecto](#sobre-el-proyecto)
  - [Instalación](#instalación)
  - [Controles](#controles)
  - [Librerias](#librerias)

## Descripción


Esta es la implementacion sencilla de un juego de Python utilizando la libreria Pygame. El juego es basico y tenes que ir esquivando enemigos y obstaculos, cuantos mas puntos tengas, mas dificil será.

## Sobre el proyecto

El proyecto cuenta con el directorio Assets donde estan alojadas todas las imagenes para que el juego funcione correctamente. 
En el archivo main.py es donde el juego cuenta con todas las funcionalidades para funcionar, 
Primero importo las librerias, luego los assets. 
El script cuenta con varias clases que en el juego cuenta como una "entidad", la clase capybara es donde  estan las funciones del jugador, como la de saltar y agacharse (jump, y duck)

## Instalación
Requerimientos: Necesitas tener python instalado

1. Clona el repositorio
2. Abre la terminal, navega al directorio donde el repositorio fue clonado, e.g., `C:\Users\Nico\pythonProyectos\CaPYbara-Game`
3. Instala la libreria:
    ```bash
    pip install pygame 
    ```
4. Ejecuta el juego utilizando el siguiente comando:
    ```bash
    python main.py
    ```

## Controles
- Usa la flecha arriba para saltar.
- Usa la flecha abajo para agacharse
- Presionar cualquier tecla para empezar el juego.

## Librerias

- [pygame](https://www.pygame.org/news): Pygame is a cross-platform set of Python modules designed for writing video games.
