#Autor: Luis Adrian Carmona Villalobos
#progama que tiene un menu de seleccion
import pygame   # Librería de pygame

def imprimirPiramides():
    contador1 = 0
    contador2 = 0
    suma1 = 0
    mult = 8

    for p1 in range(0,9):
        b1 = 10**p1
        contador1 = contador1+b1
        suma1 += contador1
        piramide1 = suma1*mult + (p1+1)
        print(contador1 ,"*", mult , "+", (p1+1), "=", piramide1)
    print()

    for p2 in range(0,9):
        base2 = 10**p2
        contador2 = contador2+base2
        piramide2 = contador2 * contador2
        print(contador2,"*",contador2,"=", piramide2)
def divisibleEntre37(n):
    return n % 37 == 0

def aproximarPi(n):
    suma = 0 #sum de fraccioes
    for d in range(1,n+1):
        fraccion = 1/d**2
        suma += fraccion

    suma = suma*6
    aproxPI = suma**0.5
    return aproxPI

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul


# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():

    print("Mision 5. Seleccione que desea hacer.\n 1.Dibujar Cuadros y Circulos "
          "\n 2. Dibujar Parabolas \n 3. Dibujar circulos "
          " \n 4. Aproximar PI \n 5. Contar divisibles entre 37"
          "\n 6. Imprimir piramide de numeros \n 0. Salir ")
    accionM = int(input("¿Que desea hacer?: "))

    if accionM == 1:
        dibujar()
    elif accionM == 2:
        pass
    elif accionM == 3:
        pass
    elif accionM == 4:
        n = int(input("Que valor quieres calcular: "))
        PI = aproximarPi(n)
        print(PI)
    elif accionM == 5:
        for n in range(1, 10000):
            if divisibleEntre37(n):
                print(n, " es divisible")
            else:
                pass
    elif accionM == 6:
        imprimirPiramides()
    elif accionM == 0:
        pass


# Llamas a la función principal
main()
