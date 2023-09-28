def desenha_tabuleiro(tabuleiro):
    """Desenha o tabuleiro do jogo da velha."""
    jogo_da_velha = ''
    for i in range(len(tabuleiro)):
        if i in [2, 5, 8]:
            jogo_da_velha += " " + tabuleiro[i] + " \n"
        else:
            jogo_da_velha += " " + tabuleiro[i] + " |"
    return jogo_da_velha

def verifica_posicao_livre(tabuleiro, posicao):
    """Verifica se uma posição no tabuleiro está livre."""
    return tabuleiro[posicao] == '_'

def verifica_vitoria(tabuleiro, simbolo):
    """Verifica se o jogador com o símbolo fornecido ganhou."""
    for linha in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if all(tabuleiro[i] == simbolo for i in linha):
            return True
    return False

def verificar_empate(tabuleiro):
    """Verifica se o jogo terminou em empate."""
    return '_' not in tabuleiro

def salvar_placar(jogador_vencedor, placar):
    """Salva o resultado da partida no arquivo de placar."""
    with open("placar.txt", "a") as arquivo:
        if jogador_vencedor == 1:
            arquivo.write("Jogador X venceu!\n")
        elif jogador_vencedor == 2:
            arquivo.write("Jogador O venceu!\n")
        else:
            arquivo.write("Empate!\n")
        arquivo.write(f"Placar: X {placar[0]} - {placar[1]} O\n")
        arquivo.write("=" * 30 + "\n")

def printar_placar():
    with open('placar.txt', 'r') as file:
        x = file.read()
        return x