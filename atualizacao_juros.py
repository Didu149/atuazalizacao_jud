def indices():
    indice_atualizacao = []
    while True:
        i = float(input('Digite os índices de atualização, do mais antigo ao mais atual, 0 para terminar: '))
        if i == 0:
            break
        indice_atualizacao.append(i)

    return indice_atualizacao
        
        



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


main()