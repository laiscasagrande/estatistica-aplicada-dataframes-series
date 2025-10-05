import pandas as pd

rotatividade_alunos = pd.DataFrame({
    "aluno": [
        "Stefani Moretti",
        "João Vitor Trevizani",
        "Adriéli Souza",
        "Gustavo Belegante",
        "Augusto Justi Hoffman",
        "Lavínia Marques Mendes",
        "Willeam Manenti",
        "Larissa De Biasi Pereira",
        "Pedro Vitor Ouriques Albino",
        "Karine de Abraham Louis",
        "Tiago Fontana",
        "Verônica",
        "José Luiz Giassi Lino",
        "Débora Moschen",
        "Ana Luiza Gonçalves Ouriques",
        "Lucas Oliverio",
        "Samuel André da Silva",
        "Maria Eduarda Wolter",
        "Suyanny Daros",
        "Fernanda Rodrigues de Aguiar",
        "Lucas Zilli Mariot",
        "Lucas Gomes",
        "Letícia Gomes Ruchert",
        "Éric Dagostim do Nascimento",
        "Jaqueline Marangoni",
        "Andrew Dutra Jorge",
        "Luana Kaminski Casagrande",
        "Beatriz Vieira Guollo",
        "Maria Laura dos Santos Vieira",
        "Matheus Carminatti Pacheco",
        "Letícia Stefany Bonomi",
        "Magali da Rosa Kaminsksi Casagrande",
        "Bernardo Santos da Silva",
        "Nicolas Andrade de Freitas",
        "Guilherme Spillere da Rosa",
        "Gabriel Ferreira da Silva",
        "Flavia da Rosa Kaminsk",
        "Nelson Casagrande",
        "Morgana da rosa Kaminski Porfirio",
        "Karina Kaminski"
    ],
    "plano": [
        "Anual",
        "Outro",
        "Mensal",
        "Outro",
        "Anual",
        "Mensal",
        "Anual",
        "Mensal",
        "Anual",
        "Mensal",
        "Anual",
        "Anual",
        "Mensal",
        "Anual",
        "Mensal",
        "Mensal",
        "Anual",
        "Anual",
        "Anual",
        "Anual",
        "Mensal",
        "Anual",
        "Mensal",
        "Anual",
        "Anual",
        "Anual",
        "Anual",
        "Trimestral",
        "Anual",
        "Anual",
        "Outro",
        "Mensal",
        "Anual",
        "Anual",
        "Mensal",
        "Mensal",
        "Mensal",
        "Trimestral",
        "Trimestral",
        "Mesal"
    ],
    "data_matricula": [
        "2017-02-01",
        "2021-10-01",
        "2024-04-18",
        "2022-01-01",
        "2024-02-02",
        "2025-07-02",
        "2025-08-01",
        "2020-08-28",
        "2025-07-07",
        "2024-04-10",
        "2022-08-30",
        "2024-11-29",
        "2023-10-01",
        "2024-04-27",
        "2024-03-13",
        "2025-02-17",
        "2021-09-20",
        "2023-09-04",
        "2025-04-09",
        "2022-10-13",
        "2020-07-30",
        "2025-01-01",
        "2023-02-15",
        "2023-04-01",
        "2022-10-01",
        "2024-01-15",
        "2023-07-01",
        "2025-07-22",
        "2024-01-01",
        "2025-03-01",
        "2017-02-02",
        "2016-02-01",
        "2025-09-01",
        "2022-09-05",
        "2020-02-10",
        "2015-07-04",
        "2025-09-01",
        "2025-04-21",
        "2022-06-01",
        "2016-05-02"
    ],
    "data_saida": [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        "2024-12-30",
        "2025-09-30",
        "2024-06-20",
        None,
        "2026-05-20",
        None,
        None,
        "2025-09-30",
        None,
        "2022-10-25",
        None,
        None,
        None,
        None,
        None,
        "2023-04-30",
        "2023-07-01",
        "2023-06-01",
        "2025-01-31",
        "2024-01-01",
        None,
        "2024-07-01",
        None,
        "2024-12-15",
        "2016-12-10",
        None ,
        None,
        "2025-05-09",
        "2024-02-29",
        None,
        None,
        "2022-09-05",
        "2017-06-01"

    ],
    "status_aluno": [
        "Ativo",
        "Ativo",
        "Ativo",
        "Ativo",
        "Ativo",
        "Ativo",
        "Ativo",
        "Cancelado",
        "Cancelado",
        "Cancelado",
        "Ativo",
        "Cancelado",
        "Ativo",
        "Ativo",
        "Cancelado",
        "Ativo",
        "Cancelado",
        "Ativo",
        "Ativo",
        "Ativo",
        "Ativo",
        "Ativo",
        "Cancelado",
        "Cancelado",
        "Cancelado",
        "Cancelado",
        "Cancelado",
        "Ativo",
        "Cancelado",
        "Ativo",
        "Cancelado",
        "Cancelado",
        "Ativo",
        "Ativo",
        "Cancelado",
        "Cancelado",
        "Ativo",
        "Ativo",
        "Cancelado",
        "Cancelado"
    ]
})

print(rotatividade_alunos)


import matplotlib.pyplot as plt

rotatividade_alunos_filtrado = rotatividade_alunos[[
    "aluno", "plano", "data_matricula", "data_saida", "status_aluno"
]]

fig, ax = plt.subplots(figsize=(20, 20))
ax.axis("off")

tabela = ax.table(
    cellText=rotatividade_alunos_filtrado.values,
    colLabels=rotatividade_alunos_filtrado.columns,
    loc="center",
    cellLoc="center",
    colLoc="center"
)

tabela.auto_set_font_size(False)
tabela.set_fontsize(9)
tabela.scale(1.2, 1.2)

for (row, col), cell in tabela.get_celld().items():
    if row == 0:  
        cell.set_facecolor("#4CAF50")
        cell.set_text_props(color="white", weight="bold")
    if col == 4: o
        if row > 0 and rotatividade_alunos_filtrado.iloc[row-1, col] == "Cancelado":
            cell.set_facecolor("#FF9999")  
        elif row > 0 and rotatividade_alunos_filtrado.iloc[row-1, col] == "Ativo":
            cell.set_facecolor("#A5D6A7")  

plt.savefig("rotatividade_alunos.png", bbox_inches="tight", dpi=300)
plt.show()

#**************************************************************************************************

inadimplencia_financeira = pd.DataFrame({
    "aluno": [
        "Stefani Moretti",
        "João Vitor Trevizani",
        "Adriéli Souza",
        "Gustavo Belegante",
        "Augusto Justi Hoffman",
        "Lavínia Marques Mendes",
        "Willeam Manenti",
        "Larissa De Biasi Pereira",
        "Pedro Vitor Ouriques Albino",
        "Karine de Abraham Louis",
        "Tiago Fontana",
        "Verônica",
        "José Luiz Giassi Lino",
        "Débora Moschen",
        "Ana Luiza Gonçalves Ouriques",
        "Lucas Oliverio",
        "Samuel André da Silva",
        "Maria Eduarda Wolter",
        "Suyanny Daros",
        "Fernanda Rodrigues de Aguiar",
        "Lucas Zilli Mariot",
        "Lucas Gomes",
        "Letícia Gomes Ruchert",
        "Éric Dagostim do Nascimento",
        "Jaqueline Marangoni",
        "Andrew Dutra Jorge",
        "Luana Kaminski Casagrande",
        "Beatriz Vieira Guollo",
        "Maria Laura dos Santos Vieira",
        "Matheus Carminatti Pacheco",
        "Letícia Stefany Bonomi",
        "Magali da Rosa Kaminsksi Casagrande",
        "Bernardo Santos da Silva",
        "Nicolas Andrade de Freitas",
        "Guilherme Spillere da Rosa",
        "Gabriel Ferreira da Silva",
        "Flavia da Rosa Kaminsk",
        "Nelson Casagrande",
        "Morgana da rosa Kaminski Porfirio",
        "Karina Kaminski"
    ],
    "plano": [
        "Anual",   
        "Outro",   
        "Mensal",  
        "Outro",   
        "Anual",   
        "Mensal",  
        "Anual",   
        "Mensal",  
        "Anual",   
        "Mensal",  
        "Anual", 
        "Anual", 
        "Mensal",  
        "Anual", 
        "Mensal",
        "Mensal", 
        "Anual", 
        "Anual", 
        "Anual", 
        "Anual", 
        "Mensal", 
        "Anual", 
        "Mensal", 
        "Anual", 
        "Anual",
        "Anual", 
        "Anual", 
        "Trimestral", 
        "Anual", 
        "Anual", 
        "Outro", 
        "Mensal", 
        "Anual", 
        "Anual", 
        "Mensal", 
        "Mensal", 
        "Mensal", 
        "Trimestral",
        "Mensal",
        "Mensal"
    ],
    "valor_mensalidade": [
        110.00,
        120.00,
        90.00,
        60.00,
        89.90,
        90.00,
        60.00,
        90.00,
        120.00,
        100.00,
        80.00,
        120.00,
        90.00,
        120.00,
        100.00,
        100.00,
        70.00,
        150.00,
        80.00,
        112.00,
        110.00,
        120.00,
        105.00,
        192.00,
        100.00,
        99.00,
        100.00,
        120.00,
        120.00,
        79.90,
        139.90,
        110.00,
        60.00,
        119.90,
        110.00,
        110.00,
        120.00,
        110.00,
        80.00,
        90.00,
    ],
    "status_pagamento": [
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Não lembra",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Atrasado",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
        "Em dia",
    ],
})
print(inadimplencia_financeira)

import matplotlib.pyplot as plt

inadimplencia_filtrado = inadimplencia_financeira[[
    "aluno", "plano", "valor_mensalidade", "status_pagamento"
]]

fig, ax = plt.subplots(figsize=(18, 20))
ax.axis("off")

tabela = ax.table(
    cellText=inadimplencia_filtrado.values,
    colLabels=inadimplencia_filtrado.columns,
    loc="center",
    cellLoc="center",
    colLoc="center"
)

tabela.auto_set_font_size(False)
tabela.set_fontsize(9)
tabela.scale(1.2, 1.2)

for (row, col), cell in tabela.get_celld().items():
    if row == 0:  
        cell.set_facecolor("#4CAF50")
        cell.set_text_props(color="white", weight="bold")

    if col == 3 and row > 0:  
        status = inadimplencia_filtrado.iloc[row-1, col]
        if status == "Em dia":
            cell.set_facecolor("#A5D6A7")  
        elif status == "Atrasado":
            cell.set_facecolor("#FF9999")  
        elif status == "Não lembra":
            cell.set_facecolor("#FFF59D")  

plt.savefig("inadimplencia_financeira.png", bbox_inches="tight", dpi=300)
plt.show()

#**************************************************************************************************

evasao_inverno = pd.DataFrame({
    "aluno": [
        "Stefani Moretti",
        "João Vitor Trevizani",
        "Adriéli Souza",
        "Gustavo Belegante",
        "Augusto Justi Hoffman",
        "Lavínia Marques Mendes",
        "Willeam Manenti",
        "Larissa De Biasi Pereira",
        "Pedro Vitor Ouriques Albino",
        "Karine de Abraham Louis",
        "Tiago Fontana",
        "Verônica",
        "José Luiz Giassi Lino",
        "Débora Moschen",
        "Ana Luiza Gonçalves Ouriques",
        "Lucas Oliverio",
        "Samuel André da Silva",
        "Maria Eduarda Wolter",
        "Suyanny Daros",
        "Fernanda Rodrigues de Aguiar",
        "Lucas Zilli Mariot",
        "Lucas Gomes",
        "Letícia Gomes Ruchert",
        "Éric Dagostim do Nascimento",
        "Jaqueline Marangoni",
        "Andrew Dutra Jorge",
        "Luana Kaminski Casagrande",
        "Beatriz Vieira Guollo",
        "Maria Laura dos Santos Vieira",
        "Matheus Carminatti Pacheco",
        "Letícia Stefany Bonomi",
        "Magali da Rosa Kaminsksi Casagrande",
        "Bernardo Santos da Silva",
        "Nicolas Andrade de Freitas",
        "Guilherme Spillere da Rosa",
        "Gabriel Ferreira da Silva",
        "Flavia da Rosa Kaminsk",
        "Nelson Casagrande",
        "Morgana da rosa Kaminski Porfirio",
        "Karina Kaminski"
    ],
    "mes_saida": [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        "dezembro",
        "setembro",
        "junho",
        None,
        "maio",
        None,
        None,
        "setembro",
        None,
        "outubro",
        None,
        None,
        None,
        None,
        None,
        "abril",
        "julho",
        "junho",
        "janeiro",
        "janeiro",
        None,
        "julho",
        None,
        "dezembro",
        "dezembro",
        None,
        None,
        "maio",
        "fevereiro",
        None,
        None,
        "setembro",
        "junho"
    ],
    "status": [
        "Ativo",
        "Ativo",
        "Ativo",
        "Ativo",
        "Ativo",
        "Ativo",
        "Ativo",
        "Cancelado",
        "Cancelado",
        "Cancelado",
        "Ativo",
        "Cancelado",
        "Ativo",
        "Ativo",
        "Cancelado",
        "Ativo",
        "Cancelado",
        "Ativo",
        "Ativo",
        "Ativo",
        "Ativo",
        "Ativo",
        "Cancelado",
        "Cancelado",
        "Cancelado",
        "Cancelado",
        "Cancelado",
        "Ativo",
        "Cancelado",
        "Ativo",
        "Cancelado",
        "Cancelado",
        "Ativo",
        "Ativo",
        "Cancelado",
        "Cancelado",
        "Ativo",
        "Ativo",
        "Cancelado",
        "Cancelado"
    ]
})
print(evasao_inverno)

import matplotlib.pyplot as plt

evasao_filtrado = evasao_inverno[["aluno", "mes_saida", "status"]]

fig, ax = plt.subplots(figsize=(18, 18))
ax.axis("off")

tabela = ax.table(
    cellText=evasao_filtrado.values,
    colLabels=evasao_filtrado.columns,
    loc="center",
    cellLoc="center",
    colLoc="center"
)

tabela.auto_set_font_size(False)
tabela.set_fontsize(9)
tabela.scale(1.2, 1.2)

for (row, col), cell in tabela.get_celld().items():
    if row == 0:  
        cell.set_facecolor("#4CAF50")
        cell.set_text_props(color="white", weight="bold")

    if col == 2 and row > 0:  
        status = evasao_filtrado.iloc[row-1, col]
        if status == "Ativo":
            cell.set_facecolor("#A5D6A7")  
        elif status == "Cancelado":
            cell.set_facecolor("#FF9999")  

plt.savefig("evasao_inverno.png", bbox_inches="tight", dpi=300)
plt.show()

#**************************************************************************************************

frequencia_academia = pd.DataFrame({
    "aluno": ["Karine de abraham louis", 
              "Pedro Vitor Ouriques Albino", 
              "Larissa De biasi Pereira", 
              "Willeam Manenti", 
              "Lavínia Marques Mendes", 
              "Augusto Justi Hoffman", 
              "Gustavo Belegante", 
              "Adriéli Souza",
              "João Vitor Trevizani",
              "Stefani Moretti",
              "Fernanda Rodrigues de Aguiar",
              "Suyanny Daros",
              "Maria Eduarda Wolter",
              "Samuel André da Silva",
              "Lucas Oliverio",
              "josé luiz giassi lino",
              "Ana Luiza Gonçalves Ouriques",
              "Débora Moschen",
              "Verônica",
              "Tiago Fontana",
              "Lucas Zilli Mariot",
              "Lucas Gomes",
              "Letícia Gomes Ruchert",
              "Éric Dagostim do Nascimento",
              "Jaqueline Marangoni",
              "Andrew Dutra Jorge",
              "Luana Kaminski Casagrande",
              "Beatriz Vieira Guollo",
              "Maria Laura dos Santos Vieira",
              "Matheus Carminatti Pacheco",
              "Letícia Stefany Bonomi",
              "Magali da Rosa Kaminsksi Casagrande",
              "Bernardo Santos da Silva",
              "Nicolas Andrade de Freitas",
              "Guilherme Spillere da Rosa",
              "Gabriel Ferreira da Silva",
              "Flavia da Rosa Kaminski",
              "Nelson  Casagrande",
              "Morgana da rosa Kaminski Porfirio",
              "Karina Kaminski"
              ],
    "Segunda": [False, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, False, True, True, True, True, True, False, True, True, True, True, True, True, True, False],
    "Terça": [True, False, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, False, True, True, False, True, True, True, False, True, True, True, False, True, True, False, True, True],
    "Quarta": [False, True, True, True, False, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, False],
    "Quinta": [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, False, False, True, False, False, True, True, False, True, False, True, False, True, True, False, True, True],
    "Sexta": [True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, False, True, True, True, True, True, True, True, True, True, False, False, False],
    "Sábado": [False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False],
    "Domingo": [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False],
})

print(frequencia_academia)

import matplotlib.pyplot as plt

frequencia_filtrado = frequencia_academia[[
    "aluno", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"
]]

fig, ax = plt.subplots(figsize=(25, 20))
ax.axis("off")

tabela = ax.table(
    cellText=frequencia_filtrado.values,
    colLabels=frequencia_filtrado.columns,
    loc="center",
    cellLoc="center",
    colLoc="center"
)

tabela.auto_set_font_size(False)
tabela.set_fontsize(9)
tabela.scale(1.2, 1.2)

for (row, col), cell in tabela.get_celld().items():
    if row == 0: 
        cell.set_facecolor("#4CAF50")
        cell.set_text_props(color="white", weight="bold")
    elif col > 0:  
        valor = frequencia_filtrado.iloc[row-1, col]
        if valor == True:
            cell.set_facecolor("#A5D6A7")  
        else:
            cell.set_facecolor("#FF9999") 

plt.savefig("frequencia_academia.png", bbox_inches="tight", dpi=300)
plt.show()

