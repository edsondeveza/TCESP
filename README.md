# Repositório de Material de Estudo - Portal da Transparência

Este repositório contém material de estudo que inclui arquivos de despesas e receitas baixados do Portal da Transparência do Tribunal de Contas do Estado de São Paulo (TCESP). O objetivo deste repositório é consolidar e analisar dados financeiros de diversas prefeituras como parte de um exercício de aprendizado.

## Estrutura do Repositório

- **Despesas/**: Contém arquivos CSV com dados de despesas das prefeituras.
- **Receitas/**: Contém arquivos CSV com dados de receitas das prefeituras.
- **Scripts/**: Contém o script Python utilizado para consolidar e processar os dados.

## Descrição do Script

O script Python `consolidar_dados.py` realiza as seguintes operações:

1. **Importação de Dados**:
   - Lê arquivos CSV das pastas `Despesas` e `Receitas`.
   - Concatena os dados de múltiplos arquivos em dois DataFrames: `consolidado_despesas` e `consolidado_receitas`.

2. **Processamento de Dados**:
   - Seleciona colunas específicas de interesse.
   - Substitui vírgulas por pontos em valores monetários e converte para tipo `float64`.
   - Converte datas para o formato `datetime`.

3. **Exportação de Dados**:
   - Salva os DataFrames processados em arquivos Excel com nomes baseados na data atual.

## Dados

Os dados foram obtidos do Portal da Transparência do TCESP (https://transparencia.tce.sp.gov.br/) e incluem informações financeiras de quatro prefeituras. Os arquivos estão organizados por ano e tipo de dado (despesas e receitas).
