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

def muneco(strikes):
    template = """
        ||===================
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ==========@          ======== 
        ||                         || 
        ||                         || 
        ||                         || 
        """
    head = (
            (8, 23, '|',),
            (9, 23, '|',),
            (10, 22, '_',),
            (10, 23, '_',),
            (10, 24, '_',),
            (11, 20, '|',),
            (11, 22, '.',),
            (11, 24, '.',),
            (11, 26, '|',),

            (12, 21, '\\',),
            (12, 23, '_',),
            (12, 25, '/',),
        )

    torso = (
        (13, 23, '|',),
        (13, 24, '|',),
        (14, 23, '|',),
        (14, 24, '|',),
        (15, 23, '|',),
        (15, 24, '|',),
        (16, 23, '|',),
        (16, 24, '|',),
    )

    left_arm = (
        (14, 20, '=',),
        (14, 21, '=',),
        (14, 22, '=',),
    )
    right_arm = (
        (14, 25, '=',),
        (14, 26, '=',),
        (14, 27, '=',),
    )

    left_leg = (
        (17, 22, '/',),
        (17, 23, '/',),
        (18, 21, '/',),
        (18, 22, '/',),
    )
    right_leg = (
        (17, 24, '\\',),
        (17, 25, '\\',),
        (18, 25, '\\',),
        (18, 26, '\\',),
    )
    tramp_closed = (
        (19, 19, '=',),
        (19, 20, '=',),
        (19, 21, '=',),
        (19, 22, '=',),
        (19, 23, '=',),
        (19, 24, '=',),
        (19, 25, '=',),
        (19, 26, '=',),
        (19, 27, '=',),
    )
    tramp_opened = (
        (19, 19, '\\',),
        (19, 20, '\\',),
        (20, 20, '\\',),
        (20, 21, '\\',),
        (21, 21, '\\',),
        (21, 22, '\\',),
        (22, 22, '\\',),
        (22, 23, '\\',),
    )

    scene_descriptors = []

    if strikes >= 1:
        scene_descriptors += head
    if strikes >= 2:
        scene_descriptors += torso
    if strikes >= 3:
        scene_descriptors += left_arm
    if strikes >= 4:
        scene_descriptors += right_arm
    if strikes >= 5:
        scene_descriptors += left_leg
    if strikes == 6:
        scene_descriptors += right_leg

    if strikes < 6:
        scene_descriptors += tramp_closed
    else:
        scene_descriptors += tramp_opened

    lines = [list(line) for line in template.splitlines()]
    for descriptor in scene_descriptors:
        lines[descriptor[0]][descriptor[1]] = descriptor[2]

    scene = '\n'.join([''.join(l) for l in lines])
    print(scene)

def run():
    lives = 6
    strikes = 0
    letter = ''
    word = wordChose()
    gues = ["_" for i in range(0,len(word))]
    print('¡Adivina la palabra!')
    muneco(strikes)

    while lives > 0:
        print(f'Vidas restantes: {"❤" * (lives)}')
        muneco(strikes)

        if letter not in gameRun(word,gues,letter):
            lives -= 1
            strikes += 1

        print(gameRun(word,gues,letter))

        if "_" in gameRun(word,gues,letter):
            letter = input("Escribe una letra: ").upper()
            clear()
        else:
            print("¡Ganaste!")
            break
    if lives == 0:
        print(f"Perdiste!!! \nLa palabra era: {word}")






if __name__ == "__main__":
    run()