# ==============================================================================
# PROJETO: Análise de Fraude e Risco em Transações
# AUTOR: Ryan Aurélio
# ==============================================================================

lista_transacoes = [
    {"id": 1, "cliente": "Ryan", "valor": 120.00, "cidade": "Goiania"},
    {"id": 2, "cliente": "Lucas", "valor": 9500.00, "cidade": "Sao Paulo"},
    {"id": 3, "cliente": "Beatriz", "valor": 45.00, "cidade": "Brasilia"},
    {"id": 4, "cliente": "Ryan", "valor": 15000.00, "cidade": "Rio de Janeiro"},
    {"id": 5, "cliente": "Lucas", "valor": 80.00, "cidade": "Sao Paulo"},
    {"id": 6, "cliente": "Beatriz", "valor": 12000.00, "cidade": "Brasilia"},
    {"id": 7, "cliente": "Fernando", "valor": 300.00, "cidade": "Goiania"},
]


def processar_lote_transacoes(lista_transacoes, limite_alerta=5000.0):
    quant_cliente = 0
    transacoes_de_risco = []
    cidades = {}
    cliente_unico = set()

    for transacao in lista_transacoes:
        cliente_unico.add(transacao["cliente"])

        # Identifica se a compra foi de alerta (valor maior que o limite)
        if transacao["valor"] > limite_alerta:
            montar_tupla = (transacao["id"], transacao["cliente"], transacao["valor"])
            transacoes_de_risco.append(montar_tupla)

        # Acumula o valor total por cidade
        if transacao["cidade"] not in cidades:
            cidades[transacao["cidade"]] = float(transacao["valor"])
        else:
            cidades[transacao["cidade"]] += float(transacao["valor"])

    return cliente_unico, transacoes_de_risco, cidades


cliente, transacoes, cidades = processar_lote_transacoes(lista_transacoes)

print("-" * 50)
print(f"Clientes únicos: {cliente}")
print(f"Número de clientes únicos: {len(cliente)}")
print(f"Valor de transações de risco: {transacoes}")
print(f"Valor de transações acumuladas por cidade: {cidades}")
print("-" * 50)
