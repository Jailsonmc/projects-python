

A = [ [5,2,3,4], [3,5,1,5] ]
B = [ [5,2], [3,44], [2,3], [3,312] ]

m = len(A)
n = len(A[0])

print(len(A))
print(len(A[0]))

#C[i][j].append()

def addMatrix(a, b):
    C = [[0,0,0],[0,0,0],[0,0,0]]
    C.append([])
    for row in range(len(A)):
        for column in range(len(A[0])):
            C[row][column] = A[row][column] + B[row][column]
    print(C)

def multiplicarMAtrizes(a,b):
    c = []
    m = len(a)
    n = len(a[0])
    p = len(b[0])
    for i in range(m):
        c.append([])
        for j in range(n):
            c[i].append(0)
    for i in range(n):
        for j in range(p):
            sum = 0
            for k in range(m):
                sum = sum + a[i][k]*b[k][j]
            c[i][j] = sum
    return c


def imprimirMatriz(A):
    for linha in A:
        print(linha)

print("A")
imprimirMatriz(A)
print("B")
imprimirMatriz(B)
print("AxB")
print(multiplicarMAtrizes(A,B))
