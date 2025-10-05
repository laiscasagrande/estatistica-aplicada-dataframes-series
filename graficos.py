import pandas as pd
import matplotlib.pyplot as plt

evasao_filtrada = evasao_inverno[evasao_inverno['mes_saida'].notna()]

evasao_por_mes = evasao_filtrada['mes_saida'].value_counts()

meses_ordem = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", 
               "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
evasao_por_mes = evasao_por_mes.reindex(meses_ordem, fill_value=0)

plt.figure(figsize=(10,6))
evasao_por_mes.plot(kind='bar', color='salmon')
plt.title("Distribuição da Evasão por Mês")
plt.xlabel("Mês")
plt.ylabel("Quantidade de Evasões")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#**************************************************************************************************

import pandas as pd
import matplotlib.pyplot as plt

dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

presenca_por_dia = frequencia_academia[dias_semana].sum()

plt.figure(figsize=(10,6))
presenca_por_dia.plot(kind='bar', color='skyblue')
plt.title("Distribuição de Presença por Dia da Semana")
plt.xlabel("Dia da Semana")
plt.ylabel("Quantidade de Alunos Presentes")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#**************************************************************************************************


import pandas as pd
import matplotlib.pyplot as plt

status_counts = rotatividade_alunos['status_aluno'].value_counts()

plt.figure(figsize=(6,5))
status_counts.plot(kind='bar', color=['#66b3ff','#ff9999'])
plt.title("Distribuição de Alunos Ativos x Cancelados")
plt.xlabel("Status do Aluno")
plt.ylabel("Quantidade de Alunos")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()