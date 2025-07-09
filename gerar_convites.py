import pandas as pd
import os

# Lê os dados do CSV
dados = pd.read_csv("parte_6_da_lista.csv", encoding="latin1", sep=";")
dados.columns = [col.strip().lower() for col in dados.columns]

# Lê o HTML base
with open("index.html", "r", encoding="utf-8") as f:
    template = f.read()

# Cria a pasta de saída, se não existir
os.makedirs("convidados", exist_ok=True)

# Gera um HTML por convidado
for _, row in dados.iterrows():
    nome = row["nome"]
    rg = str(row["rg"])
    nome_arquivo = nome.lower().replace(" ", "_") + ".html"

    # Substitui os marcadores no template
    html_personalizado = (
        template
        .replace("{{Nome}}", nome)
        .replace("{{RG}}", rg)
        .replace('href="css/style.css"', 'href="../css/style.css"')
    )

    # Salva o convite
    with open(f"convidados/{nome_arquivo}", "w", encoding="utf-8") as f:
        f.write(html_personalizado)

print("Convites gerados com sucesso!")
