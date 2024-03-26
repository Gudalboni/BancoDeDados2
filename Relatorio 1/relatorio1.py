class Professor:
    def __init__(self, nome):
        self.nome = nome
    def ministrar_aula(self, assunto):
        return f"O professor {self.nome} esta ministrando uma aula sobre {assunto}\n"

class Aluno:
    def __init__(self, nome):
        self.nome = nome
    def presenca(self):
        return f"O aluno {self.nome} esta presente\n"
        

class Aula:
    def __init__(self, professor, assunto, alunos):
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    def listar_presenca(self):
        presenca = f"\nPresenca na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n"
        for i in self.alunos:
            presenca += f"O aluno {i.nome} esta presente.\n"
        return presenca