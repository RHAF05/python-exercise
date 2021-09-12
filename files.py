def read():
    numbers = []
    with open('./files/numbers.txt','r',encoding='UTF-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Mi mujé", "Puto amo", "Kembarquiladiva"]
    with open("./files/names.txt","w", encoding="UTF-(") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    # read()
    write()

if __name__ == "__main__":
    run()