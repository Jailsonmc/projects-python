continuar = True
while continuar:
    print("Digite o ano:")
    ano = int(input())
    if(ano  >= 1800):
        continuar = False
    else:
        print("O ano precisa ser maior ou igual a 1800:")
continuar = True
while continuar:
    print("Digite o mês:")
    mes = int(input())
    if mes > 1 and mes < 12:
        continuar = False
    else:
        print("Mês precisa ser maior que 0 ou menor 13:")
continuar = True
while continuar:
    print("Digite o dia:")
    dia = int(input())
    if dia > 0 and dia < 32:
        if mes > 1 and mes < 30:
            if mes == 2 and dia == 29:
                if (ano % 4 == 0):
                    if (ano % 100 == 0) and (ano % 400 != 0):
                        print("Data inválida, ano não bissexto!")
                    else:
                        print("Data Válida")
                        continuar = False
                else:
                    print("Data inválida, ano não bissexto!")
            elif mes == 2 and dia < 29:
                print("Data Válida")
                continuar = False
            elif mes == 2 and dia > 29:
                print("Data inválida")
            elif dia == 31:
                if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                    print("Data Válida")
                    continuar = False
                else:
                    print("Data inválida")
            else:
                print("Data Válida")
                continuar = False
    else:
        print("O dia precisa ser maior que 0 ou menor 32:")