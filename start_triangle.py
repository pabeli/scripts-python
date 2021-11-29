def build_triangle(base: int):
    
    triangle=[]
    stars = base
    blank_spaces = 0
    while stars > 1:
        layer = '*' * stars
        layer = (' ' * blank_spaces) + layer + (' ' * blank_spaces)
        blank_spaces += 1 
        stars = stars - 2
        triangle.append(layer)
    
    layer = ' ' * blank_spaces + '*' + ' ' * blank_spaces 
    triangle.append(layer)
    
    return triangle

def draw_triangle(triangle: list):
    for layer in triangle[::-1]:
        print(layer)

if __name__ == '__main__':
    base = input('Ingrese la cantidad de estrellas de la base: ')
    triangle = build_triangle(int(base))
    draw_triangle(triangle)