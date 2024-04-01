from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('''Suas opções de jogada são as seguintes:

1. PEDRA
2. PAPEL
3. TESOURA

''')

jogador = int(input('Digite o número da opção desejada: '))

print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print(f'\nVocê jogou {itens[jogador]}')
sleep(1)
print(f'\nO computador jogou {itens[computador]}\n')

if jogador - computador == 0:
    print('EMPATE!')
elif jogador - computador == 1 or jogador - computador == -2:
    print('JOGADOR VENCE!')
else:
    print('COMPUTADOR VENCE!')