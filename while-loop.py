# El siguiente cod es un juego de adivinar que numero escoje la maquina
print("welcome to Guess the number!")
print("the rules are simple, I will think of a number, and you try to guess it.")
# random escoje un numero aleatorio infinito
import random
# cargamos una variable en "number" solicitando que sea un numero entre 1 y 10 para ello usamos el .randint
number = random.randint(1,10)
isGuessRigth = False
#creamos una condicional While
while isGuessRigth !=True:
    # guess es una variable que carga el numero ingresado por medio de la funcion input.
    guess = input("Guess a number between 1 and 10: ")
    # si int compara el valor ingresado cargado en la variable con el numero de maquina
    if int(guess) == number:
        #si el numero es igual imprime has ganado
        print("You guessed {}. thant is correct! you win!".format(guess))
        isGuessRigth = True
    else:
        #si el numero es incorrecto imprimira has perdido vuelva a ingresar numero
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))
        
