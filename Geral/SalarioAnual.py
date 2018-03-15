
salarioAnual = input("Digite o salário anual")
imposto = 0.78
meses = 14

salarioMensal = float(salarioAnual) / meses * imposto

#print(salarioMensal)
print('\n'*3,'Salário mensal: \n',round(salarioMensal,2))