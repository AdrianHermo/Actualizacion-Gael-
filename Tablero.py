class Tablero:
    """Clase que representa el tablero del juego."""

    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.celdas = [["~" for _ in range(columnas)] for _ in range(filas)]

    def mostrar(self):
        """Muestra el tablero por pantalla."""
        for fila in self.celdas:
            print(" ".join(fila))

    def colocar_barco(self, barco):
        """Coloca un barco en el tablero."""
        for (fila, columna) in barco.unidades:
            self.celdas[fila][columna] = "B"

# "Barco U2: Optimización de armamento y alcance."
