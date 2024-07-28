from Models.restaurante import Restaurante

restaurante_praca = Restaurante('praça bistro', 'gourmet')
restaurante_praca.receber_avaliacao('Luuar', 8)
restaurante_praca.receber_avaliacao('Luuar', 5)
restaurante_praca.receber_avaliacao('Luuar', 10)
restaurante_praca.receber_avaliacao('Luuar', 3)
restaurante_praca.receber_avaliacao('Luuar', 3.5)
restaurante_praca.alternar_ativacao()

def main():
    Restaurante.listar_restaurantes()
if __name__ == '__main__':
    main()