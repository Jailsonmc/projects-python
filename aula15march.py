import datetime


class Contacto:
    def __init__(self, nome, email, telefone, aniversario):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.aniversario = aniversario

    def __str__(self):
        return self.aniversario

class Aluno(Contacto):
    def __init__(self, numAluno, curso, ano, turma, notas,nome, email, telefone, aniversario):
        super().__init__(nome, email, telefone, aniversario)
        self.numAluno = numAluno
        self.curso = curso
        self.ano = ano
        self.turma = turma
        self.notas = notas

    def __str__(self):
        return self.nome

    def media(self):
        somatorio = 0
        for i in range(len(self.notas)):
            somatorio = somatorio + self.notas[i]
        return somatorio/len(notas)

class Professor(Contacto):
    def __init__(self, grau, disciplinas):
        super().__init__()
        self.grau = grau
        self.disciplinas = disciplinas


if __name__ == '__main__':

    data = datetime.date(2017,12,3)

    notas = []
    notas.append(14)
    notas.append(12)

    listaAl = []
    contactoJoao = Contacto("João","joao@gmail.com","345 342 235", "3/2/1990")
    listaAl.append(Aluno("2313221", "Eng Inf", "2017", "4", notas, contactoJoao.nome, contactoJoao.email,
                         contactoJoao.telefone, contactoJoao.aniversario))

    print(listaAl[0])
    print(listaAl[0].aniversario)
    print(listaAl[0].media())





