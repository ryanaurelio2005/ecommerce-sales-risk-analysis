# 🛒 E-commerce Sales & Risk Analysis Pipeline

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Code Style: Clean](https://img.shields.io/badge/Code%20Style-PEP8-brightgreen?style=for-the-badge)](https://peps.python.org/pep-0008/)

Pipeline em Python para ingestão de dados transacionais de e-commerce, análise de faturamento por catálogo, recuperação estratégica de vendas recusadas e auditoria automatizada de transações de alto risco financeiro (anti-fraude).

---

## 1. Objetivo

No comércio eletrônico, perdas operacionais decorrentes de falhas em pagamentos e fraudes transacionais impactam diretamente a margem e a saúde financeira das empresas. Este projeto foi desenvolvido com os seguintes objetivos estratégicos:

- **Recuperação de Receita Perdida**: Identificar automaticamente pedidos cancelados/recusados para gerar um relatório analítico (`resgate_urgente.csv`) pronto para acionamento por equipes comerciais e de retenção.
- **Inteligência de Vendas e Catálogo**: Mapear o catálogo de produtos e quantificar a participação de cada item no faturamento bruto utilizando estruturas nativas de alta performance (`set` e `dict`).
- **Prevenção e Auditoria de Risco**: Detectar anomalias e transações que excedem o limiar de segurança financeiro estabelecido (R$ 5.000,00), além de monitorar a distribuição do volume transacionado por polo geográfico.

---

## 2. Demonstração

Ao executar o ponto de entrada principal do projeto (`main.py`), o pipeline realiza o processamento em lote e renderiza o seguinte painel executivo no terminal:

```text
============================================================
      E-COMMERCE SALES & RISK ANALYSIS PIPELINE
============================================================

[ETAPA 1] Ingestao de Dados de Vendas...
-> Total de transacoes carregadas: 7

[ETAPA 2] Agrupamento e Metricas por Produto...
-> Produtos unicos no catalogo (6): Cadeira Gamer, Headset Gamer, Monitor LG, Mouse Sem Fio, Notebook Dell, Teclado Mecanico
-> Faturamento Bruto por Item:
   - Notebook Dell         : R$   9000.00
   - Cadeira Gamer         : R$   1800.00
   - Monitor LG            : R$   1350.00
   - Headset Gamer         : R$    420.00
   - Teclado Mecanico      : R$    350.00
   - Mouse Sem Fio         : R$    120.00

[ETAPA 3] Pipeline de Resgate Comercial de Vendas...
-> Vendas recusadas identificadas : 3
-> Receita total a recuperar      : R$    890.00
-> Relatorio exportado com sucesso: data/processed/resgate_urgente.csv

[ETAPA 4] Auditoria Anti-Fraude (Alerta > R$ 5000.00)...
-> Clientes analisados (4): Beatriz, Fernando, Lucas, Ryan
-> Transacoes em alerta de risco (3):
   [ALERTA] ID 02 | Cliente: Lucas      | Valor: R$   9500.00
   [ALERTA] ID 04 | Cliente: Ryan       | Valor: R$  15000.00
   [ALERTA] ID 06 | Cliente: Beatriz    | Valor: R$  12000.00

-> Distribuicao Financeira por Praca:
   [REGIAO] Rio de Janeiro : R$  15000.00
   [REGIAO] Brasilia       : R$  12045.00
   [REGIAO] Sao Paulo      : R$   9580.00
   [REGIAO] Goiania        : R$    420.00

============================================================
      PIPELINE CONCLUIDO COM SUCESSO! [OK]
============================================================
```

---

## 3. Tecnologias Utilizadas

- **Linguagem:** [Python 3.12](https://www.python.org/)
- **Bibliotecas Nativas:**
  - `csv`: Ingestão, parsing e exportação estruturada de arquivos tabulares.
  - `pathlib`: Manipulação semântica e multiplataforma de caminhos de arquivos.
  - `typing`: Assinaturas estáticas de métodos (*Type Hints* para maior manutenibilidade).
- **Estruturas de Dados:** `set` (operações de unicidade em $O(1)$), `dict` (agregações e contagens) e `tuple` (registros imutáveis de risco).
- **Controle de Versão:** [Git](https://git-scm.com/) e [GitHub](https://github.com/).

---

## 4. Estrutura do Projeto

```bash
ecommerce-sales-risk-analysis/
├── data/
│   ├── raw/
│   │   └── dados_vendas_bruto.csv       # Base bruta de dados transacionais
│   └── processed/
│       └── resgate_urgente.csv          # Relatório gerado de vendas a recuperar
├── src/
│   ├── __init__.py                      # Inicializador do pacote Python
│   ├── constantes.py                    # Tuplas imutáveis e configurações de regras de negócio
│   ├── resgate_vendas.py                # Pipeline de filtragem e exportação de pedidos recusados
│   ├── agrupamento_produtos.py          # Agrupamento e agregação de faturamento por catálogo
│   └── analise_fraude.py                # Detecção de transações de alto risco e métricas regionais
├── main.py                              # Ponto de entrada que orquestra o pipeline completo
├── .gitignore                           # Exclusão de arquivos temporários, caches e ambientes
└── README.md                            # Documentação técnica obrigatória do projeto
```

---

## 5. Como Executar

### Pré-requisitos
- Python 3.10 ou superior instalado.
- Git instalado na máquina.

### Passo a Passo

1. **Clonar o Repositório:**
   ```bash
   git clone https://github.com/ryanaurelio2005/ecommerce-sales-risk-analysis.git
   cd ecommerce-sales-risk-analysis
   ```

2. **(Opcional) Criar e Ativar Ambiente Virtual:**
   ```bash
   # Windows (PowerShell)
   python -m venv venv
   .\venv\Scripts\Activate.ps1

   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Executar o Pipeline Completo:**
   ```bash
   python main.py
   ```

4. **Verificar os Resultados:**
   O arquivo de saída consolidado para a equipe de vendas estará disponível em `data/processed/resgate_urgente.csv`.

---

## 6. Dataset

O dataset utilizado simula o fluxo transacional de um e-commerce de tecnologia, contendo 7 registros representativos de diferentes cenários de pagamento.

### Dicionário de Variáveis

| Variável | Tipo | Descrição | Exemplo |
| :--- | :---: | :--- | :--- |
| `id_transacao` | `Integer` | Identificador único da transação | `101` |
| `cliente` | `String` | Nome do cliente responsável pela compra | `"Marcos Castro"` |
| `produto` | `String` | Descrição do item adquirido | `"Notebook Dell"` |
| `valor` | `Float` | Valor monetário bruto da transação (R$) | `4500.00` |
| `status_pagamento` | `String` | Estado de liquidação do pedido (`aprovado`, `recusado`, `pendente`) | `"aprovado"` |

*Origem:* Dados simulados para homologação de pipelines financeiros e auditoria analítica.

---

## 7. Resultados

A execução do pipeline sobre a base transacional gerou os seguintes insights quantitativos e operacionais:

- **Recuperação de Pedidos:** De 7 transações registradas, **3 pedidos foram recusados** pelas operadoras (taxa de recusa de **42,8%**).
- **Impacto Financeiro Resgatável:** O montante financeiro total retido em pagamentos recusados é de **R$ 890,00**, concentrado em periféricos e acessórios (Headset, Teclado e Mouse). A disponibilização imediata do `resgate_urgente.csv` permite contato ativo com os clientes para recuperação desse montante.
- **Concentração de Faturamento:** O item **Notebook Dell** lidera com folga o volume financeiro bruto, totalizando **R$ 9.000,00** (61,5% do faturamento total analisado).
- **Auditoria de Risco:** 3 transações foram classificadas em nível de alerta crítico (> R$ 5.000,00), totalizando **R$ 36.500,00** em volume sob monitoramento, com forte concentração geográfica no polo do **Rio de Janeiro** (R$ 15.000,00) e **Brasília** (R$ 12.045,00).

---

## 8. Próximas Versões

Roadmap de evolução técnica planejado para as próximas iterações:

- [ ] **Testes Automatizados:** Implementação de suíte de testes unitários com `pytest` cobrindo regras de negócio e validação de schemas CSV.
- [ ] **Persistência Relacional:** Adição de camada de banco de dados com SQLite / SQLAlchemy para histórico contínuo de transações.
- [ ] **Dashboard Interativo:** Construção de painel analítico com `Streamlit` para visualização gráfica das taxas de aprovação e métricas de risco.
- [ ] **Modelagem Preditiva de Fraude:** Integração com modelo de Machine Learning (`Scikit-Learn` / `XGBoost`) para predição probabilística de transações fraudulentas com base em comportamento histórico.

---

## 👨‍💻 Autor

Desenvolvido por **[Ryan Oliveira](https://github.com/ryanaurelio2005)**.  
*Estudante de Ciência de Dados e Inteligência Artificial | Foco em Engenharia de Machine Learning.*
