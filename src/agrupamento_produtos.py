"""Módulo para agrupamento de vendas e consolidação de faturamento por produto."""

from pathlib import Path
from typing import Dict, List, Set
from src.resgate_vendas import carregar_vendas


def obter_catalogo_produtos(vendas: List[Dict[str, str]]) -> Set[str]:
    """Extrai e retorna o conjunto (set) único de produtos comercializados."""
    return {venda["produto"] for venda in vendas}


def calcular_faturamento_por_produto(
    vendas: List[Dict[str, str]], apenas_aprovados: bool = False
) -> Dict[str, float]:
    """Calcula o faturamento total acumulado por produto.
    
    Args:
        vendas: Lista de dicionários representando as transações.
        apenas_aprovados: Se True, soma apenas vendas com status 'aprovado'.
    """
    faturamento_por_produto: Dict[str, float] = {}

    for venda in vendas:
        status = venda.get("status_pagamento", "").strip().lower()
        if apenas_aprovados and status != "aprovado":
            continue

        produto = venda["produto"]
        valor = float(venda["valor"])

        if produto not in faturamento_por_produto:
            faturamento_por_produto[produto] = 0.0
        faturamento_por_produto[produto] += valor

    return faturamento_por_produto


if __name__ == "__main__":
    raiz = Path(__file__).resolve().parent.parent
    caminho_dados = raiz / "data" / "raw" / "dados_vendas_bruto.csv"

    vendas = carregar_vendas(caminho_dados)
    produtos = obter_catalogo_produtos(vendas)
    faturamento = calcular_faturamento_por_produto(vendas)

    print("Catálogo de Produtos Identificados:")
    print(produtos)
    print("\nFaturamento Acumulado por Produto:")
    for prod, valor in faturamento.items():
        print(f"- {prod:<20}: R$ {valor:>8.2f}")
