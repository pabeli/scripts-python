def check_prime(number: int):
    prime = True
    for element in range(number):
        if element != 0 and element != 1:
            if number % element == 0:
                prime = False
    
    return prime


if __name__ == '__main__':
    number = input('Ingrese el número que desea saber si es o no primo: ')
    prime = check_prime(int(number))
    if prime:
        print('El número es primo')
    else:
        print('El número no es primo')