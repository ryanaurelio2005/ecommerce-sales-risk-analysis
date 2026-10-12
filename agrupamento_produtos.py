import csv

with open("dados_vendas_bruto.csv", mode="r", encoding="utf-8") as arquivo:
    lista = list(csv.DictReader(arquivo))

lista_de_produtos = []
for venda in lista:
    lista_de_produtos.append(venda["produto"])

lista_de_produtos_atual = set(lista_de_produtos)
print("Produtos únicos encontrados:")
print(lista_de_produtos_atual)

faturamento_por_produto = {}
for valor in lista:
    produto = valor["produto"]
    preco = float(valor["valor"])
    if produto not in faturamento_por_produto:
        faturamento_por_produto[produto] = 0.0
    faturamento_por_produto[produto] += preco

print("\nFaturamento acumulado por produto:")
print(faturamento_por_produto)
