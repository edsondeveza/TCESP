import pandas as pd
import os
import datetime

# criando datetime
data = datetime.datetime.now()

# Criando df consolidado_despesas vazio

colunas_despesas = ['id_despesa_detalhe', 'ano_exercicio', 'ds_municipio', 'ds_orgao', 
           'mes_referencia', 'mes_ref_extenso', 'tp_despesa', 'nr_empenho',
           'identificador_despesa', 'ds_despesa', 'dt_emissao_despesa', 'vl_despesa', 
           'ds_funcao_governo', 'ds_subfuncao_governo', 'cd_programa', 'ds_programa', 
           'cd_acao', 'ds_acao', 'ds_fonte_recurso', 'ds_cd_aplicacao_fixo', 
           'ds_modalidade_lic', 'ds_elemento', 'historico_despesa']

consolidado_despesas = pd.DataFrame(columns=colunas_despesas)

# Criando df consolidado_receitas vazio

colunas_receitas = ['id_rec_arrec_detalhe', 'ano_exercicio', 'ds_municipio', 'ds_orgao',
                    'mes_referencia', 'mes_ref_extenso', 'ds_poder', 'ds_fonte_recurso',
                    'ds_cd_aplicacao_fixo', 'ds_cd_aplicacao_variavel', 'ds_categoria', 
                    'ds_fonte', 'ds_rubrica', 'ds_alinea', 'ds_subalinea', 'vl_arrecadacao']

consolidado_receitas = pd.DataFrame(columns=colunas_receitas)

# Criando variaveis com os arquivos

arquivos_despesas = os.listdir('Despesas')
arquivos_receitas = os.listdir('Receitas')

# concatenando arquivos csv de despesas

for arquivo_despesa in arquivos_despesas:
    
    if arquivo_despesa.endswith('.csv'):
        
        try:
            df = pd.read_csv(f'Despesas/{arquivo_despesa}', sep=(';'), encoding='ISO-8859-1')
            consolidado_despesas = pd.concat([df, consolidado_despesas], ignore_index=True)
        except Exception as e:
            with open('log_erros.txt', 'a') as file:
                file.write(f'Erro ao tentar consolidar o arquivo {arquivo_despesa}!\n')
                file.write(f'Detalhes do erro: {str(e)}\n\n')
                
    else:
        with open('log_erros.txt', 'a') as file:
                file.write(f'O arquivo {arquivo_despesa} não é um arquivo CSV válido!\n\n')
    
# concatenando arquivos csv de recitas

for arquivo in arquivos_receitas:
    
    if arquivo.endswith('.csv'):
        
        try:
            df = pd.read_csv(f'Receitas/{arquivo}', sep=(';'), encoding='ISO-8859-1')
            consolidado_receitas = pd.concat([df, consolidado_receitas], ignore_index=True)
        except Exception as e:
            with open('log_erros.txt', 'a') as file:
                file.write(f'Erro ao tentar consolidar o arquivo {arquivo}!\n')
                file.write(f'Detalhes do erro: {str(e)}\n\n')
                
    else:
        with open('log_erros.txt', 'a') as file:
                file.write(f'O arquivo {arquivo} não é um arquivo CSV válido!\n\n')

# Selecionando colunas desejadas e criando um novo df_despesas

colunas_desejadas = ['ano_exercicio', 'mes_ref_extenso', 'ds_municipio', 'ds_orgao',
                     'tp_despesa', 'identificador_despesa', 'dt_emissao_despesa',
                     'vl_despesa', 'ds_funcao_governo', 'ds_programa', 'ds_modalidade_lic']

df_despesas = consolidado_despesas[colunas_desejadas]

# Selecionando colunas desejadas e criando um novo df_receitas

colunas_desejadas = ['ano_exercicio', 'mes_ref_extenso','ds_municipio', 'ds_orgao', 
                     'ds_fonte_recurso', 'ds_categoria', 'vl_arrecadacao']

df_receitas = consolidado_receitas[colunas_desejadas]

# Trando dados substituindo , por . na colunas de valores monetários dos dfs
df_despesas.loc[:, 'vl_despesa'] = df_despesas['vl_despesa'].str.replace(',', '.')
df_receitas.loc[:, 'vl_arrecadacao'] = df_receitas['vl_arrecadacao'].str.replace(',', '.')

# alterando tipo de string para float64 das colunas de valores monetários
df_despesas = df_despesas.astype({'vl_despesa' : 'float64'})
df_receitas = df_receitas.astype({'vl_arrecadacao' : 'float64'})

# alterando tipo de string para data da coluna dt_emissao_despesa
df_despesas['dt_emissao_despesa'] = pd.to_datetime(df_despesas['dt_emissao_despesa'], format='%d/%m/%Y')

# gerando arquivo excel de despesas cosolidado
df_despesas.to_excel(f"Despesas-consolidado-{data.strftime('%d-%m-%Y')}.xlsx", 
                     index=False,
                     sheet_name='despesas_consolidado')

# gerando arquivo excel de receitas cosolidado

df_receitas.to_excel(f"Receitas-consolidado-{data.strftime('%d-%m-%Y')}.xlsx", 
                     index=False,
                     sheet_name='receitas_consolidado')