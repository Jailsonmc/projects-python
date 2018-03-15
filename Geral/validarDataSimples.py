def verificarDia(dia, mes, ano):
    if dia < 1 or dia > 31:
        return False
    elif mes == 2 and dia == 29:
        if ano % 4 == 0:
            if(ano % 100 == 0) and (ano % 400 != 0):
                return False
            else:
                return True
    elif dia == 31:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            return True
        else:
            return False
    return True
continuar = True
while continuar:
    while continuar:
        print("Digite o ano:")
        ano = int(input())
        if ano < 1800:
            print("Data inválida:")
        continuar = False
    continuar = True
    while continuar:
        print("Digite o mes:")
        mes = int(input())
        if mes < 1 or mes > 12:
            print("Data inválida:")
        continuar = False
    continuar = True
    while continuar:
        print("Digite o dia:")
        dia = int(input())
        if verificarDia(dia, mes, ano) == False:
            print("Data inválida:")
        print("Data Válida:")
        continuar = False
continuar = True

