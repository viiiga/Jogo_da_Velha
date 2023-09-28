from funcoes import desenha_tabuleiro
from funcoes import verifica_posicao_livre
from funcoes import verifica_vitoria
from funcoes import verificar_empate
from funcoes import salvar_placar
from funcoes import printar_placar

placar = [0, 0]  # Inicialização do placar (X: placar[0], O: placar[1])

while True:
    # Inicialização do tabuleiro
    tabuleiro = ['_' for _ in range(9)]

    # Variáveis do jogo
    jogador = 1

    while True:
        # Verifica de quem é a vez
        simbolo = 'X' if jogador == 1 else 'O'
        jogador_input = input(f'Jogador {jogador} Digite uma posição de 1 a 9: ')

        try:
            posicao = int(jogador_input) - 1

            if 0 <= posicao <= 8 and verifica_posicao_livre(tabuleiro, posicao):
                tabuleiro[posicao] = simbolo
                print(desenha_tabuleiro(tabuleiro))

                if verifica_vitoria(tabuleiro, simbolo):
                    print(f'Jogador {jogador} ganhou!')
                    placar[jogador - 1] += 1  # Atualiza o placar
                    salvar_placar(jogador, placar)  # Salva o resultado da partida no arquivo
                    break
                elif verificar_empate(tabuleiro):
                    print('Empate!')
                    salvar_placar(0, placar)  # Salva o resultado da partida no arquivo (empate)
                    break
                else:
                    jogador = 3 - jogador  # Alternar entre jogador 1 e 2
            else:
                print(desenha_tabuleiro(tabuleiro))
                print('Posicao invalida ou ocupada.')
        except ValueError:
            print(desenha_tabuleiro(tabuleiro))
            print('Entrada invalida. Digite um número de 1 a 9.')

    resposta = input('Deseja recomeçar uma nova partida? (s/n): ')
    if resposta.lower() == 's':
        True
    else: 
        pl = printar_placar()
        print(pl)
        break
   