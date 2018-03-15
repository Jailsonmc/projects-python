def durMes(mes,ano):
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    elif mes != 2 :
        return 31
    elif ano % 4 != 0:
        return 28
    elif ano % 100 != 0:
        return 29
    elif ano % 400 == 0:
        return 29
    return 28

def validaData(dia, mes, ano):
    if ano < 1800:
        return('Data inválida')
    elif mes < 1 or mes > 12:
        return('Data inválida')
    elif dia < 1 or dia > durMes(mes,ano):
        return('Data inválida')
    return('Data Válida')

print('\n'*3,'PROGRAMA PARA VALIDAR UMA DATA')

dia = int(input('Dia(2 dígitos):?'))
mes = int(input('Mês(2 dígitos):?'))
ano = int(input('Ano(4 dígitos):?'))

print('\n'*3,'Entradas do ultilizadir:\n','Dia:',dia,'Mês:',mes,'Ano:',ano)
print('Resultado:',validaData(dia,mes,ano))


