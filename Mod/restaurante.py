from Mod.avaliacao import Avaliacao
class Restaurante:
    restaurantes =[]

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f' {self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes (cls):        
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliações".ljust(25)}{"Status"}')
        for restaurante in cls.restaurantes:
            print (f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.media_avaliacao:<25}{restaurante.ativo}')
    @property 
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def recerber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao (cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return f'Não avaliado'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1) /2
        return media
    

'''
restaurante_praça = Restaurante('praça restaurante', 'popular')
restaurante_praça.alternar_estado()
restaurante_kilino = Restaurante('kilino', 'japonesa')
Restaurante.listar_restaurantes()
'''