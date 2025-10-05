dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

frequencia_por_dia = frequencia_academia[dias_semana].sum()

print(frequencia_por_dia)

import matplotlib.pyplot as plt
import pandas as pd

frequencia_por_dia_df = frequencia_por_dia.reset_index()
frequencia_por_dia_df.columns = ["Dia", "Total"]

fig, ax = plt.subplots(figsize=(8, 3))
ax.axis("off")

tabela = ax.table(
    cellText=frequencia_por_dia_df.values,
    colLabels=frequencia_por_dia_df.columns,
    loc="center",
    cellLoc="center",
    colLoc="center"
)

tabela.auto_set_font_size(False)
tabela.set_fontsize(12)
tabela.scale(1.2, 1.2)

for (row, col), cell in tabela.get_celld().items():
    if row == 0: 
        cell.set_facecolor("#4CAF50")
        cell.set_text_props(color="white", weight="bold")
    elif col == 1: 
        total = frequencia_por_dia_df.iloc[row-1, col]
        intensidade = min(1, total / frequencia_por_dia_df["Total"].max())
        cell.set_facecolor((1-intensidade, 1, 1-intensidade)) 

plt.show()

#**************************************************************************************************

quantidade_status = rotatividade_alunos['status_aluno'].value_counts()

print(quantidade_status)

import matplotlib.pyplot as plt
import pandas as pd

quantidade_status_df = quantidade_status.reset_index()
quantidade_status_df.columns = ["Status", "Quantidade"]

fig, ax = plt.subplots(figsize=(6, 2))
ax.axis("off")

tabela = ax.table(
    cellText=quantidade_status_df.values,
    colLabels=quantidade_status_df.columns,
    loc="center",
    cellLoc="center",
    colLoc="center"
)

tabela.auto_set_font_size(False)
tabela.set_fontsize(12)
tabela.scale(1.2, 1.2)

for (row, col), cell in tabela.get_celld().items():
    if row == 0:
        cell.set_facecolor("#4CAF50")
        cell.set_text_props(color="white", weight="bold")
    elif col == 0:  
        status = quantidade_status_df.iloc[row-1, col]
        if status == "Ativo":
            cell.set_facecolor("#A5D6A7")  
        else:
            cell.set_facecolor("#FF9999") 

plt.show()

#**************************************************************************************************

import pandas as pd
from datetime import datetime

rotatividade_alunos['data_matricula'] = pd.to_datetime(rotatividade_alunos['data_matricula'])
rotatividade_alunos['data_saida'] = pd.to_datetime(rotatividade_alunos['data_saida'])


hoje = pd.to_datetime(datetime.today().date())

rotatividade_alunos['dias_frequencia'] = rotatividade_alunos.apply(
    lambda row: (row['data_saida'] if pd.notnull(row['data_saida']) else hoje) - row['data_matricula'],
    axis=1
)

rotatividade_alunos['dias_frequencia'] = rotatividade_alunos['dias_frequencia'].dt.days

rotatividade_alunos[['aluno', 'dias_frequencia']]

media = rotatividade_alunos['dias_frequencia'].mean()

mediana = rotatividade_alunos['dias_frequencia'].median()

moda = rotatividade_alunos['dias_frequencia'].mode().tolist()

variancia = rotatividade_alunos['dias_frequencia'].var()

desvio_padrao = rotatividade_alunos['dias_frequencia'].std()

print(f"Média: {media:.2f} dias")
print(f"Mediana: {mediana} dias")
print(f"Moda: {moda} dias")
print(f"Variância: {variancia:.2f}")
print(f"Desvio padrão: {desvio_padrao:.2f}")

import matplotlib.pyplot as plt
import pandas as pd

estatisticas = pd.DataFrame({
    "Estatística": ["Média", "Mediana", "Moda", "Variância", "Desvio Padrão"],
    "Valor": [media, mediana, moda[0], variancia, desvio_padrao]
})

fig, ax = plt.subplots(figsize=(6, 2))
ax.axis("off")

tabela = ax.table(
    cellText=estatisticas.values,
    colLabels=estatisticas.columns,
    loc="center",
    cellLoc="center",
    colLoc="center"
)

tabela.auto_set_font_size(False)
tabela.set_fontsize(12)
tabela.scale(1.2, 1.2)

for (row, col), cell in tabela.get_celld().items():
    if row == 0:
        cell.set_facecolor("#4CAF50")
        cell.set_text_props(color="white", weight="bold")

plt.show()

#**************************************************************************************************

import pandas as pd

evasao_filtrada = evasao_inverno[evasao_inverno['mes_saida'].notna()]

evasao_por_mes = evasao_filtrada['mes_saida'].value_counts().sort_values(ascending=False)

print(evasao_por_mes)

import matplotlib.pyplot as plt
import pandas as pd

evasao_por_mes_df = evasao_por_mes.reset_index()
evasao_por_mes_df.columns = ["Mês", "Quantidade"]

fig, ax = plt.subplots(figsize=(6, len(evasao_por_mes_df)*0.5))
ax.axis("off")

tabela = ax.table(
    cellText=evasao_por_mes_df.values,
    colLabels=evasao_por_mes_df.columns,
    loc="center",
    cellLoc="center",
    colLoc="center"
)

tabela.auto_set_font_size(False)
tabela.set_fontsize(10)
tabela.scale(1.2, 1.2)

max_val = evasao_por_mes_df["Quantidade"].max()
for (row, col), cell in tabela.get_celld().items():
    if row == 0:
        cell.set_facecolor("#4CAF50")
        cell.set_text_props(color="white", weight="bold")
    elif col == 1:
        intensidade = evasao_por_mes_df.iloc[row-1, col] / max_val
        cell.set_facecolor((1-intensidade, 1, 1-intensidade)) 

plt.show()