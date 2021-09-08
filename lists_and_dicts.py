def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Ricardo", "lastname": "Arias"}

    super_list = [
        {"firstname": "Ricardo", "lastname": "Arias"},
        {"firstname": "Arlen", "lastname": "Barranco"},
        {"firstname": "Kemberlýn", "lastname": "Barranco"},
        {"firstname": "Miguel", "lastname": "Arias"},
        {"firstname": "Saudith", "lastname": "Arias"},
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for values in super_list:
        print(values)
        for key, value in values.items():
            print(key, "-", value)

if __name__ == '__main__':
    run()