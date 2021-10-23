#Aluno: Giovanny Generoso
#Exercícios referente a aula 9
#Realizado no dia 22/10/21

#revisao basica de criacao de classes

class Animais: 
 
    def __init__(self, cobertura=None, alimento=None, patas=None, habitat=None, nome=None): 
        self.cobertura = cobertura 
        self.alimento = alimento 
        self.patas = patas 
        self.habitat = habitat 
        self.nome = nome 
 
    def trocar(self, cobertura): 
        self.cobertura = cobertura 
 
class Cachorros(Animais): 
    def trocar(self): 
        self.cobertura = 'crespo'

pet = Cachorros('Liso', 'Ração', 4, 'Domiciliar', 'Pandora')


print(pet.cobertura)
print(pet.trocar())
print(pet.cobertura)
