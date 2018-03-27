def main():
    name = str(input("Name: "))

    while len(name)<=1:
        print('Invalid input')
        name = str(input("Name: "))
    print_name(name)

def print_name(name):
    print(name[::2])


def get_name():
    main()


get_name()