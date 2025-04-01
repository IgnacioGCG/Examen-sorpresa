from Punto import Punto

class Rectangulo:
    def _init_(self, punto_inicial: Punto, punto_final: Punto):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final
        
    def calcular_base(self):
        base = abs(self.punto_final.x - self.punto_inicial.x)
        return base
    
    def calcular_altura(self):
        altura = abs(self.punto_final.y - self.punto_inicial.y)
        return altura

    def calcular_area(self, base, altura):
        return base * altura

    def calcular_perimetro(self):
        """Calcula el perímetro del rectángulo."""
        base = abs(self.punto_final.x - self.punto_inicial.x)
        altura = abs(self.punto_final.y - self.punto_inicial.y)
        return 2 * (base + altura)

    def _str_(self):
        return (f"Rectángulo definido por los puntos "
                f"({self.punto_inicial.x}, {self.punto_inicial.y}) y "
                f"({self.punto_final.x}, {self.punto_final.y})")