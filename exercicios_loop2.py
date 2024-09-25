quantidade_trasacoes = int(input('Informe a quantidade de transações'))
total_transacoes = 0
for n_transacao in range(1, quantidade_trasacoes + 1, 1):
    transacao = float(input(f'Poe favor, informe a transação de numero {n_transacao}'))
    total_transacoes = total_transacoes + transacao

media = total_transacoes / quantidade_trasacoes
print(f'nesta dia foi gasto um total {total_transacoes}, com uma media de R${media} por trasação')