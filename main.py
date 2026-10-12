"""Pipeline Principal: E-commerce Sales & Risk Analysis Pipeline.

Executa o fluxo consolidado de dados:
1. Ingestão de vendas brutas.
2. Agrupamento de catálogo e faturamento por produto.
3. Filtro e exportação de vendas recusadas para resgate comercial.
4. Auditoria de transações atípicas e volume financeiro regional.
"""

from pathlib import Path
from src.agrupamento_produtos import (
    calcular_faturamento_por_produto,
    obter_catalogo_produtos,
)
from src.analise_fraude import TRANSACOES_EXEMPLO, processar_lote_transacoes
from src.constantes import LIMITE_ALERTA_PADRAO
from src.resgate_vendas import (
    carregar_vendas,
    exportar_resgate_urgente,
    processar_vendas_recusadas,
)


def executar_pipeline():
    raiz = Path(__file__).resolve().parent
    caminho_dados = raiz / "data" / "raw" / "dados_vendas_bruto.csv"
    caminho_saida = raiz / "data" / "processed" / "resgate_urgente.csv"

    print("\n" + "=" * 60)
    print("      E-COMMERCE SALES & RISK ANALYSIS PIPELINE")
    print("=" * 60)

    # 1. Ingestão
    print("\n[ETAPA 1] Ingestao de Dados de Vendas...")
    vendas = carregar_vendas(caminho_dados)
    print(f"-> Total de transacoes carregadas: {len(vendas)}")

    # 2. Catálogo e Faturamento
    print("\n[ETAPA 2] Agrupamento e Metricas por Produto...")
    catalogo = obter_catalogo_produtos(vendas)
    faturamento_produtos = calcular_faturamento_por_produto(vendas)

    print(f"-> Produtos unicos no catalogo ({len(catalogo)}): {', '.join(sorted(catalogo))}")
    print("-> Faturamento Bruto por Item:")
    for prod, valor in sorted(faturamento_produtos.items(), key=lambda x: x[1], reverse=True):
        print(f"   - {prod:<22}: R$ {valor:>9.2f}")

    # 3. Recuperação de Vendas Recusadas
    print("\n[ETAPA 3] Pipeline de Resgate Comercial de Vendas...")
    vendas_recusadas, receita_recusada = processar_vendas_recusadas(vendas)
    exportar_resgate_urgente(vendas_recusadas, caminho_saida)

    print(f"-> Vendas recusadas identificadas : {len(vendas_recusadas)}")
    print(f"-> Receita total a recuperar      : R$ {receita_recusada:>9.2f}")
    print(f"-> Relatorio exportado com sucesso: {caminho_saida.relative_to(raiz)}")

    # 4. Auditoria de Risco e Fraude
    print(f"\n[ETAPA 4] Auditoria Anti-Fraude (Alerta > R$ {LIMITE_ALERTA_PADRAO:.2f})...")
    clientes, transacoes_risco, volume_cidades = processar_lote_transacoes(
        TRANSACOES_EXEMPLO, limite_alerta=LIMITE_ALERTA_PADRAO
    )

    print(f"-> Clientes analisados ({len(clientes)}): {', '.join(sorted(clientes))}")
    print(f"-> Transacoes em alerta de risco ({len(transacoes_risco)}):")
    for id_t, cli, val in transacoes_risco:
        print(f"   [ALERTA] ID {id_t:02d} | Cliente: {cli:<10} | Valor: R$ {val:>9.2f}")

    print("\n-> Distribuicao Financeira por Praca:")
    for cidade, volume in sorted(volume_cidades.items(), key=lambda x: x[1], reverse=True):
        print(f"   [REGIAO] {cidade:<15}: R$ {volume:>9.2f}")

    print("\n" + "=" * 60)
    print("      PIPELINE CONCLUIDO COM SUCESSO! [OK]")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    executar_pipeline()
