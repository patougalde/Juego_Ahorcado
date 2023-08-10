class Dibujos:
    def __init__(self):
        self.dibujo_ahorcado = [
    """
        +---+
            |
            |
            |
            |
           ===
    """,
    """
        +---+
        O   |
            |
            |
            |
           ===
    """,
    """
        +---+
        O   |
        |   |
            |
            |
           ===
    """,
    """
        +---+
        O   |
       /|   |
            |
            |
           ===
    """,
    """
        +---+
        O   |
       /|\  |
            |
            |
           ===
    """,
    """
        +---+
        O   |
       /|\  |
       /    |
            |
           ===
    """,
    """
        +---+
        O   |
       /|\  |
       / \  |
            |
           ===
    """
]
    def mostrar_dibujo(self, errores):
        if errores < len(self.dibujo_ahorcado):
            print(self.dibujo_ahorcado[errores])
        else:
            print("no hay dibujo para mostrar")
        
      
            
        
