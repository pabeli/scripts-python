def fibonacci(element: int):
    result = [0, 1]
    i = 0
    j = 1
    while result[i] + result[j] < element:
        new_element = result[i] + result[j]
        result.append(new_element)
        i += 1
        j += 1
    
    return result

if __name__ == '__main__':
    number = input('Ingrese el número al que le desea calcular la serie de Fibonacci: ')
    result = fibonacci(int(number))
    print(result)


