class Pessoa ():
    def __init__(self, nome, idade, genero):
        self.nome = nome 
        self.idade = idade 
        self.genero = genero 

class Paciente(Pessoa):
    def __init__(self, nome, idade, genero):
        super().__init__(nome, idade, genero)
        self.sintoma = sintoma 

class Medico(Pessoa):
    def __init__(self, nome, idade, genero, especialidade):
        super().__init__(nome, idade, genero, especialidade)
        self.crm = crm

    def imprimir_crm(self):
        return print( 'CRM: ' + self.crm ) 
print ('________PACIENTE________')
paciente = Paciente('Gripe', 'Marcia', 'f')
paciente.imprimir_dados()
paciente.imprimir_sintoma()




