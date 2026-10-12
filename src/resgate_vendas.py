"""Módulo responsável por identificar vendas recusadas e gerar relatórios de resgate comercial."""

import csv
from pathlib import Path
from typing import Dict, List, Tuple
from src.constantes import COLUNAS_VENDAS


def carregar_vendas(caminho_arquivo: Path) -> List[Dict[str, str]]:
    """Lê o arquivo CSV de vendas brutas e retorna uma lista de dicionários."""
    if not caminho_arquivo.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")

    with open(caminho_arquivo, mode="r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        return list(leitor)


def processar_vendas_recusadas(
    vendas: List[Dict[str, str]],
) -> Tuple[List[Dict[str, str]], float]:
    """Filtra as transações com status recusado e calcula a receita total a ser recuperada."""
    vendas_recusadas: List[Dict[str, str]] = []
    valor_total_recusado: float = 0.0

    for venda in vendas:
        status = venda.get("status_pagamento", "").strip().lower()
        if status == "recusado":
            valor_total_recusado += float(venda["valor"])
            vendas_recusadas.append(venda)

    return vendas_recusadas, valor_total_recusado


def exportar_resgate_urgente(
    vendas_recusadas: List[Dict[str, str]], caminho_saida: Path
) -> None:
    """Exporta as vendas recusadas para a planilha de acionamento imediato da equipe comercial."""
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)

    with open(caminho_saida, mode="w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=COLUNAS_VENDAS)
        escritor.writeheader()
        escritor.writerows(vendas_recusadas)


if __name__ == "__main__":
    raiz = Path(__file__).resolve().parent.parent
    caminho_dados = raiz / "data" / "raw" / "dados_vendas_bruto.csv"
    caminho_saida = raiz / "data" / "processed" / "resgate_urgente.csv"

    vendas = carregar_vendas(caminho_dados)
    recusadas, total_perdido = processar_vendas_recusadas(vendas)

    print(f"Total de vendas recusadas : {len(recusadas)}")
    print(f"Receita total a resgatar  : R$ {total_perdido:.2f}")

    exportar_resgate_urgente(recusadas, caminho_saida)
    print(f"Arquivo de resgate exportado em: {caminho_saida}")
