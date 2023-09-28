from funcoes import desenha_tabuleiro
from funcoes import verifica_posicao_livre
from funcoes import verifica_vitoria
from funcoes import verificar_empate
from funcoes import salvar_placar
from funcoes import printar_placar

placar = [0, 0]  

while True:
    tabuleiro = ['_' for _ in range(9)]

    jogador = 1

    while True:
        simbolo = 'X' if jogador == 1 else 'O'
        jogador_input = input(f'Jogador {jogador} Digite uma posição de 1 a 9 (sendo 1 -> 1x1 e 9 -> 3x3): ')

        try:
            posicao = int(jogador_input) - 1

            if 0 <= posicao <= 8 and verifica_posicao_livre(tabuleiro, posicao):
                tabuleiro[posicao] = simbolo
                print(desenha_tabuleiro(tabuleiro))

                if verifica_vitoria(tabuleiro, simbolo):
                    print(f'Jogador {jogador} ganhou!')
                    placar[jogador - 1] += 1 
                    salvar_placar(jogador, placar) 
                    break
                elif verificar_empate(tabuleiro):
                    print('Empate!')
                    salvar_placar(0, placar) 
                    break
                else:
                    jogador = 3 - jogador  
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
   
