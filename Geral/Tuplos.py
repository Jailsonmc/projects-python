import math

a = (1,434,5)

print(a)
print(a[2])

def dist(x_1, y_1, x_2, y_2):
    #Cálculo da distância euclidiana entre os pontos 1 e 2. #
    return math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

print(str(dist(2,4,5,6)))

b = ("João", "Felipa", "Maria")
print(b[0] + " " +b[1])