"""Módulo para identificação de transações de alto risco (anti-fraude) e métricas geográficas."""

from typing import Dict, List, Set, Tuple
from src.constantes import LIMITE_ALERTA_PADRAO

# Transações de exemplo para homologação de regras anti-fraude
TRANSACOES_EXEMPLO = [
    {"id": 1, "cliente": "Ryan", "valor": 120.00, "cidade": "Goiania"},
    {"id": 2, "cliente": "Lucas", "valor": 9500.00, "cidade": "Sao Paulo"},
    {"id": 3, "cliente": "Beatriz", "valor": 45.00, "cidade": "Brasilia"},
    {"id": 4, "cliente": "Ryan", "valor": 15000.00, "cidade": "Rio de Janeiro"},
    {"id": 5, "cliente": "Lucas", "valor": 80.00, "cidade": "Sao Paulo"},
    {"id": 6, "cliente": "Beatriz", "valor": 12000.00, "cidade": "Brasilia"},
    {"id": 7, "cliente": "Fernando", "valor": 300.00, "cidade": "Goiania"},
]


def processar_lote_transacoes(
    transacoes: List[Dict], limite_alerta: float = LIMITE_ALERTA_PADRAO
) -> Tuple[Set[str], List[Tuple[int, str, float]], Dict[str, float]]:
    """Processa um lote de transações comerciais.
    
    Identifica:
        1. Clientes únicos avaliados no lote (set).
        2. Transações de risco que excedem o teto financeiro seguro (tuplas imutáveis).
        3. Faturamento total consolidado por praça/cidade (dict).
        
    Args:
        transacoes: Lista de dicionários contendo id, cliente, valor e cidade.
        limite_alerta: Valor de corte para classificação de alerta de risco.
        
    Returns:
        Tupla contendo (clientes_unicos, transacoes_de_risco, faturamento_por_cidade).
    """
    clientes_unicos: Set[str] = set()
    transacoes_de_risco: List[Tuple[int, str, float]] = []
    cidades: Dict[str, float] = {}

    for transacao in transacoes:
        clientes_unicos.add(transacao["cliente"])
        valor = float(transacao["valor"])

        # Identificação de transações atípicas
        if valor > limite_alerta:
            montar_tupla = (transacao["id"], transacao["cliente"], valor)
            transacoes_de_risco.append(montar_tupla)

        # Acúmulo por praça regional
        cidade = transacao["cidade"]
        cidades[cidade] = cidades.get(cidade, 0.0) + valor

    return clientes_unicos, transacoes_de_risco, cidades


if __name__ == "__main__":
    clientes, riscos, cidades = processar_lote_transacoes(TRANSACOES_EXEMPLO)

    print("=" * 45)
    print("      RELATÓRIO DE RISCO E AUDITORIA       ")
    print("=" * 45)
    print(f"Clientes Únicos Identificados ({len(clientes)}): {clientes}")
    print(f"\nTransações de Alto Risco (> R$ {LIMITE_ALERTA_PADRAO:.2f}):")
    for id_t, cli, val in riscos:
        print(f"  [ALERTA] ID {id_t:02d} | Cliente: {cli:<10} | Valor: R$ {val:>9.2f}")

    print("\nVolume Financeiro Acumulado por Praça:")
    for cid, val in cidades.items():
        print(f"  - {cid:<15}: R$ {val:>9.2f}")
    print("=" * 45)
