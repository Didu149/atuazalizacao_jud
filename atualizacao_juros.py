def indices():
    indice_atualizacao = []
    while True:
        i = float(input('Digite os índices de atualização, do mais antigo ao mais atual, 0 para terminar: '))
        if i == 0:
            break
        indice_atualizacao.append(i)

    return indice_atualizacao
        
def juros():
    meses = int(input('Quantos meses em atraso? '))
    valor = float(input('Qual o valor do débito? '))
    contador = 0
    juros = meses
    valor_jurado = 0
    while contador <= meses:
        jurado = valor * (juros/100)
        juros -= 1
        valor_jurado += jurado
        contador += 1
    return valor_jurado


def main():
    
    print('Bem vindo ao atualizador!')
    operacao = int(input('''Digite:
    1 - para inserir os índices de atualização;
    2 - para cálculo de juros;
    3 - para sair.
    > '''))

    if operacao == 1:

        tabela_indices = indices()
        valor_atualizar = float(input('Digite o valor a atualizar: '))
        valor_atualizado = (valor_atualizar/tabela_indices[0]) * tabela_indices[-1]
        print(f'O valor atualizado é de R${valor_atualizado}.')
    if operacao == 2:
        valor_juros = juros()
        print(f'O valor dos juros é R${juros}.')


main()