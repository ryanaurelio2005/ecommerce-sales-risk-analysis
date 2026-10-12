import csv

with open("dados_vendas_bruto.csv", mode="r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    vendas = list(leitor)

valor_recusado = 0.0
vendas_recusadas_id = []

for venda in vendas:
    if venda["status_pagamento"] == "recusado":
        valor_recusado += float(venda["valor"])
        vendas_recusadas_id.append(venda)

print(f"Total de vendas recusadas: {len(vendas_recusadas_id)}")
print(f"Total de valor recusado: R$ {valor_recusado:.2f}")

with open("resgate_urgente.csv", mode="w", newline="", encoding="utf-8") as arquivo_saida:
    colunas = ["id_transacao", "cliente", "produto", "valor", "status_pagamento"]
    escritor = csv.DictWriter(arquivo_saida, fieldnames=colunas)
    escritor.writeheader()
    escritor.writerows(vendas_recusadas_id)

print("Planilha 'resgate_urgente.csv' gerada com sucesso!")
