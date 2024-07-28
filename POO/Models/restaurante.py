import os
from Models.avaliacao import Avaliacao
class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria
        self._ativo = False #O underline antes de ativo é uma convenção para informar que esse atributo não deve ser acessado pelo usuário, estamos protegendo ele, e não definindo como privado.
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    def __str__(cls):
        return f'{cls.nome} | {cls.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        os.system('cls')
        print('\nListando restaurantes...\n\n')
        print(f'{'Nome do restaurante:'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)}| {'Ativação'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)}| {restaurante.ativo}')
    @property
    def ativo(self):
        return '✔️' if self._ativo else '❌'

    def alternar_ativacao(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_de_notas, 1)
        return media