def run():
    #llenado de un diccionar a partir de un for
    #primero la llave, luego dos puntos
    #luego el valor de la llave
    #y finalmente el for
    dictionary = {i: round(i**3,2) for i in range(1,1000)}

    print(dictionary)

    #la otra forma
    dictionaryOther = {}

    for i in range(1,1000):
        dictionaryOther[i] = i**3

    print(dictionaryOther)

if __name__ == "__main__":
    run()