import os
import csv
from pathlib import Path

def listar_arquivos_html_para_csv():
    """
    Função que lista todos os arquivos HTML da pasta 'convidados' 
    e cria um arquivo CSV com os nomes dos arquivos.
    """
    
    # Caminho para a pasta convidados
    pasta_convidados = Path("convidados")
    
    # Verificar se a pasta existe
    if not pasta_convidados.exists():
        print("Erro: A pasta 'convidados' não foi encontrada!")
        return
    
    # Listar todos os arquivos HTML
    arquivos_html = []
    
    for arquivo in pasta_convidados.glob("*.html"):
        # Pegar o nome do arquivo com a extensão
        nome_arquivo = arquivo.name
        arquivos_html.append(nome_arquivo)
    
    # Ordenar a lista alfabeticamente
    arquivos_html.sort()
    
    # Criar o arquivo CSV
    nome_arquivo_csv = "lista_convidados.csv"
    
    with open(nome_arquivo_csv, 'w', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        
        # Escrever cabeçalho
        writer.writerow(['Nome do Arquivo'])
        
        # Escrever os nomes dos arquivos
        for nome in arquivos_html:
            writer.writerow([nome])
    
    print(f"✅ Arquivo CSV '{nome_arquivo_csv}' criado com sucesso!")
    print(f"📊 Total de arquivos HTML encontrados: {len(arquivos_html)}")
    print(f"📁 Arquivos processados da pasta: {pasta_convidados}")
    
    # Mostrar os primeiros 10 arquivos como exemplo
    print("\n📋 Primeiros 10 arquivos da lista:")
    for i, nome in enumerate(arquivos_html[:10], 1):
        print(f"  {i}. {nome}")
    
    if len(arquivos_html) > 10:
        print(f"  ... e mais {len(arquivos_html) - 10} arquivos")

if __name__ == "__main__":
    listar_arquivos_html_para_csv() 