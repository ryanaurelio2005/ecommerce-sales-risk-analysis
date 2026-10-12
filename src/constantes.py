"""Módulo de constantes e definições imutáveis do sistema."""

# Status de pagamento homologados no pipeline
STATUS_PERMITIDOS = ("aprovado", "recusado", "pendente")

# Configurações padrão de análise de risco e fraudes (em R$)
LIMITE_ALERTA_PADRAO = 5000.0

# Colunas padrão do arquivo de vendas e exportação de resgate
COLUNAS_VENDAS = ["id_transacao", "cliente", "produto", "valor", "status_pagamento"]
