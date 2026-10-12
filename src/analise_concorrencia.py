# ==============================================================================
# PROJETO: Inteligência de Precificação e Análise de Concorrência
# AUTOR: Ryan Aurélio
# ==============================================================================

dados_concorrentes = [
    {"loja": "Magazine Luiza", "preco": 2400.00, "frete_gratis": True, "avaliacao": 4.8},
    {"loja": "Casas Bahia", "preco": 2350.00, "frete_gratis": False, "avaliacao": 4.2},
    {"loja": "Amazon", "preco": 2490.00, "frete_gratis": True, "avaliacao": 4.9},
    {"loja": "Mercado Livre", "preco": 2299.00, "frete_gratis": True, "avaliacao": 4.7},
    {"loja": "Fast Shop", "preco": 2550.00, "frete_gratis": False, "avaliacao": 4.6},
]

preco_da_loja = 2450.0


def calculo_concorrentes(dados_concorrentes, preco_da_loja):
    """Analisa os preços praticados por concorrentes no mercado.
    
    Identifica:
        1. O concorrente mais perigoso (menor preço com frete grátis).
        2. A margem de rebaixamento recomendada para ser competitivo.
        3. A média geral de preços praticados no mercado.
    """
    preco_original = preco_da_loja
    concorrente_perigoso = None
    valor_acumulado = 0

    for concorrente in dados_concorrentes:
        if concorrente["preco"] < preco_da_loja and concorrente["frete_gratis"]:
            preco_da_loja = concorrente["preco"]
            concorrente_perigoso = concorrente

        valor_acumulado += concorrente["preco"]

    if concorrente_perigoso is None:
        concorrente_perigoso = "Já temos o melhor preço"

    valor_para_abaixar = preco_original - preco_da_loja
    media = valor_acumulado / len(dados_concorrentes)

    return concorrente_perigoso, valor_para_abaixar, media


if __name__ == "__main__":
    concorrente, valor_abaixar, media_mercado = calculo_concorrentes(
        dados_concorrentes, preco_da_loja
    )

    print("-" * 55)
    print(f"Concorrente perigoso : {concorrente}")
    print(f"Preço para abaixar   : R$ {valor_abaixar:.2f}")
    print(f"Média das lojas      : R$ {media_mercado:.2f}")
    print("-" * 55)
