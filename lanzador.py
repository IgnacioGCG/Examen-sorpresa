from Punto import Punto
from Rectangulo import Rectangulo
class Lanzador:
    
    def __init__(self):
        # Crear los puntos
        A, B, C, D, O = crear_puntos()

        # Imprimir los puntos
        imprimir_puntos(A, B, C, D)

        # Consultar cuadrantes
        consultar_cuadrante(A, C, D)

        # Consultar vectores
        consultar_vectores(A, B)

        # Consultar distancias al origen
        consultar_distancias(A, B, C, O)

        # Crear el rectángulo y mostrar información
        crear_rectangulo(A, B)
        
def crear_puntos():
        # Crear los puntos
        A = Punto(2, 3)
        B = Punto(5, 5)
        C = Punto(-3, -1)
        D = Punto(0, 0)
        O = Punto(0, 0)
        return A, B, C, D, O

def imprimir_puntos(A, B, C, D):
        # Imprimir los puntos
        print("Punto A:", A)
        print("Punto B:", B)
        print("Punto C:", C)
        print("Punto D:", D)

def consultar_cuadrante(A, C, D):
        # Consultar y mostrar el cuadrante de los puntos
        print("El punto A pertenece al:", A.cuadrante())
        print("El punto B pertenece al:", B.cuadrante())
        print("El punto C pertenece al:", C.cuadrante())
        print("El punto D pertenece al:", D.cuadrante())

def consultar_vectores(A, B):
        # Consultar y mostrar los vectores AB y BA
        print("El vector AB es:", A.vector(B))
        print("El vector BA es:", B.vector(A))

def consultar_distancias(A, B, C, O):
        # Calcular distancias al origen
        distancia_A = A.distancia(O)
        distancia_B = B.distancia(O)
        distancia_C = C.distancia(O)

        # Determinar el punto más lejano
        if distancia_A > distancia_B and distancia_A > distancia_C:
            print("El punto A está más lejos del origen.")
        elif distancia_B > distancia_A and distancia_B > distancia_C:
            print("El punto B está más lejos del origen.")
        else:
            print("El punto C está más lejos del origen.")

def crear_rectangulo(A, B):
        
        rectangulo = Rectangulo(A, B)

        # Imprimir información del rectángulo
        print(rectangulo)
        print("Base del rectángulo:", rectangulo.calcular_base())
        print("Altura del rectángulo:", rectangulo.calcular_altura())
        print("Área del rectángulo:", rectangulo.calcular_area(rectangulo.calcular_base(), rectangulo.calcular_altura()))
        print("Perímetro del rectángulo:", rectangulo.calcular_perimetro())
        
if __name__ == "__main__":
    A, B, C, D, O = crear_puntos()
    imprimir_puntos(A, B, C, D)
    consultar_cuadrante(A, C, D)
    consultar_vectores(A, B)
    consultar_distancias(A, B, C, O)
    crear_rectangulo(A, B)
    
