           
import palabras
import dibujo
class Jugador:
    def __init__(self):
        self.errores = 0

    def incrementar_errores(self):
        self.errores += 1

class Juego:
    def __init__(self, jugador, palabra, dibujo):
        self.palabra = palabra
        self.jugador= jugador
        self.dibujo = dibujo
    def jugar(self):
        #print(palabra)
        guiones = "_" * len(self.palabra)
        lista_palabra = list(guiones)
        letras_ingresadas  =[]
        #**********dibujo_ahorcado****************
        print("Palabra a adivinar:", " ".join(lista_palabra))

        while self.jugador.errores < 7:
            i = 0
            letra_adivinar = input("Ingresa una letra que creas que contenga la palabra secreta: \n")

            #mensaje de en caso de que se ingrese una letra que ya se habia ingresado anteriormente *** no cuenta como error ***
            if letra_adivinar in letras_ingresadas:
                print("Ya habías ingresado esa letra antes")
                continue

            letras_ingresadas.append(letra_adivinar)

            if letra_adivinar in self.palabra:
                for letra in self.palabra:
                    if letra == letra_adivinar:
                        lista_palabra[i] = letra
                    i += 1
                print("Acierto: la letra está en la palabra")
            else:
               
                self.jugador.incrementar_errores()
                print("Error: la letra no está en la palabra")
                #****************for de dibujo***********************
                self.dibujo.mostrar_dibujo(self.jugador.errores)
            print("La palabra a adivinar es:", " ".join(lista_palabra))

            if "_" not in lista_palabra:
                print("¡¡¡¡¡¡¡¡¡¡¡¡Ganaste!!!!!!!!!!!!")
                break
            else:
                print("Errores:", self.jugador.errores)

        else:
            print("¡¡¡¡¡Perdiste!!!!! la palabra era:",self.palabra)
            
 
from jugador import Jugador, Juego
jugador1 = Jugador()
objeto_palabra = palabras.Palabras()
palabra = objeto_palabra.palabras_aleatorias()
dibujo1 =dibujo.Dibujos()
juego1 = Juego(jugador1, palabra,dibujo1)
juego1.jugar()