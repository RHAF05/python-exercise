"""AHORCADO
Author: Ricardo Arias
"""
import os
import random

#limpiar pantalla
def clear():
    os.system("cls")

#Buscamos la palabra a adivinar
def wordChose():
    listWords = []
    with open("./files/data.txt",'r',encoding="UTF-8") as f:
        listWords = [word.strip().upper() for word in f]
    choseWord = listWords[random.randint(0,len(listWords))]
    return choseWord

def gameRun(word,gues,letter):
    if letter in word:
        for i in range(len(word)):
            if letter == word[i]:
                gues[i]=letter
    return ' '.join(gues)

def run():
    lives = 5
    letter = ''
    word = wordChose()
    gues = ["_" for i in range(0,len(word))]
    print('¡Adivina la palabra!')

    while lives > 0:
        print(f'Vidas restantes: {"❤" * (lives)}')

        if letter not in gameRun(word,gues,letter):
            lives -= 1

        print(gameRun(word,gues,letter))

        if "_" in gameRun(word,gues,letter):
            letter = input("Escribe una letra: ").upper()
            clear()
        else:
            print("¡Ganaste!")
            break
    if lives == 0:
        print("Perdiste!!!")





if __name__ == "__main__":
    run()