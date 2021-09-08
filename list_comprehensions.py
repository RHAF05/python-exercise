def run():
    squares = []
    squaresThree = []
    for i in range(1,101):
        squares.append(i**2)

    #print(squares)

    for i in range(1,101):
        if i % 3 !=0: #que no sean divisibles por 3
            squaresThree.append(i**2)

    #print(squaresThree)

    #hacer el mismo ejercicio de otra forma
    squaresOther = [i**2 for i in range(1,101) if i % 3 !=0]

    #print (squaresOther)

    squaresChallenge = [i for i in range(1,10000) if i % 4==0 and i % 6 ==0 and i % 9 == 0]

    print(squaresChallenge)

if __name__ == '__main__':
    run()