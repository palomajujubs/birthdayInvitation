import pandas as pd

# Lê os dados do CSV
dados = pd.read_csv("parte_6_da_lista.csv", encoding="latin1", sep=";", low_memory=False)

print("=== ESTRUTURA DOS DADOS ===")
print(f"Colunas: {list(dados.columns)}")
print(f"Total de linhas: {len(dados)}")
print(f"Tipos de dados:")
print(dados.dtypes)

print("\n=== PRIMEIRAS 5 LINHAS ===")
print(dados.head())

print("\n=== VERIFICANDO VALORES NULOS ===")
print(dados.isnull().sum())

print("\n=== VERIFICANDO VALORES ÚNICOS NA COLUNA NOME ===")
if 'nome' in dados.columns:
    print("Valores únicos na coluna 'nome':")
    print(dados['nome'].unique())
else:
    print("Coluna 'nome' não encontrada!")
    print("Colunas disponíveis:", list(dados.columns)) 