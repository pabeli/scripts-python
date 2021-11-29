def first_bubble_sort(elements: list) -> list:
    for i in range(len(elements) - 1):
        for j in range(len(elements) - i - 1):
            if elements[j] > elements[j+1]:
                aux = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = aux
    
    return elements

def second_bubble_sort(elements: list) -> list:
    # We set the band to false
    band = False
    # Initialize the count
    i = 1
    # Initialize the length
    n = len(elements)

    while (i < n) and band:
        i += 1
        band = True
        for j in range(n-i):
            if elements[j]>elements[j+1]:
                band = False
                aux = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = aux
    
    return elements

if __name__ == '__main__':
    a = [1,3,4,2]

    first_result = first_bubble_sort(a)
    print(f'First bubble sort algorithm result: {first_result}')

    second_result = second_bubble_sort(a)
    print(f'Second bubble sort algorithm result: {second_result}')