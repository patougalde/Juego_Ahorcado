import random
class Palabras:
    def __init__(self):
        self.temas = {1:["leon", "vaca", "camello", "grillo", "perro"],
            2:["aczino","lobostepario","rc","potencia","zticma"],
            3:["golovkin", "lomachenco","bivol", "charlo", "benavidez"]}
    
    def palabras_aleatorias(self):
        print("****OPCIONES**** \n Selecciona el numero del tema con el que quieres jugar: \n 1 = Animales, 2 = Nombre de raperos en FMS mexico, 3 = Apellido de buenos boxeadores\n")
        tema_elegido =self.temas[int(input("ingresa el tema que deseas: \n"))]
        palabra_aleatoria = random.choice(tema_elegido)
        return palabra_aleatoria        
        