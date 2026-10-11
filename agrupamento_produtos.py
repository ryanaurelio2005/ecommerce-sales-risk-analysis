import csv

with open("dados_vendas_bruto.csv", mode="r", encoding="utf-8") as arquivo:

    lista = list(csv.DictReader(arquivo))


lista_de_produtos = []

for venda in lista:

    lista_de_produtos.append(venda["produto"])

lista_de_produtos_atual = set(lista_de_produtos)

print(lista_de_produtos_atual)

faturamento_por_produto = {}

for valor in lista:

    if valor["produto"] not in faturamento_por_produto:

        faturamento_por_produto[valor["produto"]] = 0.0
        faturamento_por_produto[valor["produto"]] += float(valor["valor"])

    else: 

        faturamento_por_produto[valor["produto"]] += float(valor["valor"])

print(faturamento_por_produto)




    
    
