class Pessoa:
    def cumprimentar(self): # atributo/ metodo()
        return f'Ola {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())


'''
def = atributo
cumprimento = função / metodo sempre esta atrelada a um 
obj(sempre tem que declara um paranmetro a esse obj a ser rebido) (self)
'''