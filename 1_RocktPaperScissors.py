'''
Rock Paper Scissors Python Game
> Pedra Papel e Tesoura
> Acumular Pontos
> Se acertar 10 ganha uma dica
'''
from random import choice
from time import sleep

jogo = ['PEDRA', 'PAPEL', 'TESOURA']
d = v = e = 0
while True:
    maquina = choice(jogo)
    jogador = input(f'Escolha sua opção: {jogo}: ').upper()
    print('Computador está escolhendo uma opção',end='')
    for n in range(0,5):
        sleep(0.6)
        print('.', end='')
    print('\n')
    if jogador == maquina:
        print(f'Empate | Você: {jogador} x Máquina: {maquina}')
        e += 1
    elif jogador == 'PEDRA':
        if maquina == 'TESOURA':
            print(f'Vitória | Você: {jogador} x Máquina: {maquina}')
            v += 1
        elif maquina == 'PAPEL':
            print(f'Derrota | Você: {jogador} x Máquina: {maquina}')
            d += 1
    elif jogador == 'PAPEL':
        if maquina == 'TESOURA':
            print(f'Derrota | Você: {jogador} x Máquina: {maquina}')
            d += 1
        elif maquina == 'PEDRA':
            print(f'Vitória | Você: {jogador} x Máquina: {maquina}')
            v += 1
    elif jogador == 'TESOURA':
        if maquina == 'PAPEL':
            print(f'Vitória | Você: {jogador} x Máquina: {maquina}')
            v += 1
        elif maquina == 'PEDRA':
            print(f'Derrota | Você: {jogador} x Máquina: {maquina}')
            d += 1
    else:
        print(f'Opção inválida!')
    frase = f'PLACAR (V/D/E): {v}|{d}|{e} '
    print('-'*len(frase))
    print(frase)
    while True:
        opc = input('Mais uma partida? [S/N] ').upper().strip()[0]
        if opc in 'SN':
            break
    if opc == 'N':
        print('Obrigado por jogar!')
        try:
            resultados = open('resultados_jogo.txt','a')
            resultados.write(frase)
        except Exception as erro:
            print(f'Erro! {erro}')
        break