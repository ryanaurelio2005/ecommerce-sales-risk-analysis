# 🛒 E-commerce Sales & Risk Analysis Pipeline

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Code Style: Clean](https://img.shields.io/badge/Code%20Style-PEP8-brightgreen?style=for-the-badge)](https://peps.python.org/pep-0008/)

Pipeline em Python para ingestão de dados transacionais de e-commerce, análise de faturamento por catálogo, recuperação estratégica de vendas recusadas, auditoria anti-fraude e inteligência de benchmark de preços com concorrentes.

---

## 1. Objetivo

No comércio eletrônico, perdas operacionais decorrentes de falhas em pagamentos, fraudes transacionais e precificação descalibrada frente à concorrência impactam diretamente a margem e a competitividade da operação. Este projeto foi desenvolvido com quatro metas estratégicas:

- **Recuperação de Receita Perdida**: Identificar automaticamente pedidos recusados e gerar um relatório analítico (`resgate_urgente.csv`) para acionamento imediato por equipes de retenção comercial.
- **Inteligência de Vendas e Catálogo**: Mapear o catálogo de produtos e quantificar a participação de cada item no faturamento bruto utilizando estruturas nativas de alta performance (`set` e `dict`).
- **Prevenção e Auditoria de Risco**: Detectar anomalias e transações que excedem o teto financeiro seguro (R$ 5.000,00), além de monitorar a distribuição de volume por polo geográfico.
- **Inteligência de Precificação e Concorrência**: Mapear a média de preços do mercado e identificar os concorrentes mais agressivos (cruzando menor preço e frete grátis) para calcular a margem de corte necessária para manter a loja competitiva.

---

## 2. Demonstração

Ao executar o ponto de entrada principal do projeto (`main.py`) ou os scripts analíticos individuais, o pipeline renderiza o seguinte painel executivo:

```text
==============================================================
      E-COMMERCE SALES & RISK ANALYSIS PIPELINE
==============================================================

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
   [REGIAO] Rio de Janeiro  : R$  15000.00
   [REGIAO] Brasilia        : R$  12045.00
   [REGIAO] Sao Paulo       : R$   9580.00
   [REGIAO] Goiania         : R$    420.00

[ETAPA 5] Inteligencia de Precos e Analise de Concorrencia...
-> Preco atual da nossa loja       : R$   2450.00
-> Concorrente mais perigoso       : Mercado Livre (R$ 2299.00 | Frete Gratis: True | Avaliacao: 4.7)
-> Reducao recomendada para cobrir : R$    151.00
-> Media geral de precos do mercado: R$   2417.80

==============================================================
      PIPELINE CONCLUIDO COM SUCESSO! [OK]
==============================================================
```

---

## 3. Tecnologias Utilizadas

- **Linguagem:** [Python 3.12](https://www.python.org/)
- **Módulos Nativos:**
  - `csv`: Leitura, processamento e exportação de dados tabulares.
  - `pathlib`: Resolução de diretórios e caminhos de arquivos multiplataforma.
  - `typing`: Assinaturas estáticas de métodos para documentação e legibilidade.
- **Estruturas de Dados:** `set` (operações de unicidade em $O(1)$), `dict` (agregações e contagens) e `tuple` (registros imutáveis de transações).
- **Versionamento:** [Git](https://git-scm.com/) e [GitHub](https://github.com/).

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
│   ├── analise_concorrencia.py          # Módulo de inteligência competitiva e benchmark
│   ├── analise_fraude.py                # Módulo de auditoria de risco e métricas regionais
│   ├── agrupamento_produtos.py          # Módulo de catálogo e faturamento consolidado
│   ├── constantes.py                    # Tuplas imutáveis e configurações de negócio
│   └── resgate_vendas.py                # Módulo de recuperação de vendas recusadas
├── analise_concorrencia.py              # Script executável direto de inteligência de concorrência
├── analise_fraude.py                    # Script executável direto de auditoria de compras
├── agrupamento_produtos.py              # Script executável direto de catálogo e vendas
├── solucao.py                           # Script executável direto de resgate de vendas
├── main.py                              # Orquestrador do pipeline completo (Etapas 1 a 5)
├── requirements.txt                     # Especificação de dependências e ambiente
├── .gitignore                           # Exclusão de arquivos temporários e caches
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

2. **Executar o Pipeline Completo:**
   ```bash
   python main.py
   ```

3. **Ou Executar Módulos Individuais:**
   ```bash
   # Benchmark de preços e concorrentes
   python analise_concorrencia.py

   # Auditoria de risco e fraudes
   python analise_fraude.py

   # Recuperação de vendas recusadas
   python solucao.py
   ```

4. **Verificar os Relatórios:**
   O arquivo de saída consolidado para a equipe de vendas estará disponível em `data/processed/resgate_urgente.csv`.

---

## 6. Dataset

O projeto opera com duas bases de dados estratégicas:

### Base de Vendas (`dados_vendas_bruto.csv`)
| Variável | Tipo | Descrição | Exemplo |
| :--- | :---: | :--- | :--- |
| `id_transacao` | `Integer` | Identificador único da transação | `101` |
| `cliente` | `String` | Nome do cliente responsável pela compra | `"Marcos Castro"` |
| `produto` | `String` | Descrição do item adquirido | `"Notebook Dell"` |
| `valor` | `Float` | Valor monetário bruto da transação (R$) | `4500.00` |
| `status_pagamento` | `String` | Estado de liquidação (`aprovado`, `recusado`, `pendente`) | `"aprovado"` |

### Base de Concorrência (Benchmark de Mercado)
Contém dados de 5 grandes redes varejistas (Magazine Luiza, Casas Bahia, Amazon, Mercado Livre e Fast Shop) monitorando `loja`, `preco`, `frete_gratis` e `avaliacao`.

---

## 7. Resultados

A execução do pipeline analítico consolidou os seguintes insights quantitativos e operacionais:

- **Recuperação de Pedidos:** De 7 transações registradas, **3 pedidos foram recusados** (taxa de recusa de **42,8%**), totalizando **R$ 890,00** em receita resgatável imediata.
- **Concentração de Faturamento:** O item **Notebook Dell** lidera o volume financeiro bruto com **R$ 9.000,00** (61,5% do total).
- **Auditoria de Risco:** 3 transações foram classificadas em nível de alerta crítico (> R$ 5.000,00), totalizando **R$ 36.500,00** em volume sob monitoramento, com forte concentração no polo do **Rio de Janeiro** (R$ 15.000,00) e **Brasília** (R$ 12.045,00).
- **Inteligência de Concorrência:** O preço da nossa loja (R$ 2.450,00) está acima da média de mercado (R$ 2.417,80). O concorrente mais agressivo identificado é o **Mercado Livre** (R$ 2.299,00 com Frete Grátis e avaliação 4.7), exigindo uma redução recomendada de **R$ 151,00** para liderar a conversão de vendas.

---

## 8. Próximas Versões

Roadmap de evolução técnica planejado para as próximas iterações:

- [ ] **Testes Automatizados:** Implementação de suíte de testes unitários com `pytest` cobrindo regras de negócio e validação de schemas CSV.
- [ ] **Persistência Relacional:** Adição de camada de banco de dados com SQLite / SQLAlchemy para histórico contínuo de transações.
- [ ] **Dashboard Interativo:** Construção de painel analítico com `Streamlit` para visualização gráfica das taxas de aprovação e métricas de risco.
- [ ] **Modelagem Preditiva de Fraude:** Integração com modelo de Machine Learning (`Scikit-Learn` / `XGBoost`) para predição probabilística de transações fraudulentas com base em comportamento histórico.

---

## 👨‍💻 Autor

Desenvolvido por **[Ryan Aurélio](https://github.com/ryanaurelio2005)**.  
*Estudante de Ciência de Dados e Inteligência Artificial | Foco em Engenharia de Machine Learning.*
