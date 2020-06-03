def indices():
    indice_atualizacao = []
    while True:
        i = float(input('Digite os índices de atualização, do mais antigo ao mais atual, 0 para terminar: '))
        indice_atualizacao.append(i)
        if i ==0:
            break
    return indice_atualizacao
        
        



def main():
    
    print('Bem vindo ao atualizador!')
    operacao = int(input('''Digite:
    1 - para inserir os índices de atualização;
    2 - para cálculo de juros;
    3 - para sair.
    > '''))

    if operacao == 1:
        indices()
        

