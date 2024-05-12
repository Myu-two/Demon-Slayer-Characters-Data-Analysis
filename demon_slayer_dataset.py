# -*- coding: utf-8 -*-
---

A Fanbase pediu e nós trouxemos! Depois de seu sucesso nas telas do cinema em 2024, o anime Demon Slayer conquistou mais de 86% do público e deixou muita gente curiosa sobre os personagens que apareceram. Você sabe quem é o personagem mais velho do anime? Sabe quais são as armas usadas por cada Hashira? Qual é o gênero predominante entre os personagens? Com essas e mais perguntas, chegou hora de apresentar alguns dados do elenco de Demon Slayer.

*   Qual é o gênero predominante dos personagens?
"""

import pandas as pd
from collections import Counter

df = pd.read_csv('/Personagens.csv')

generos = df["Gender"].tolist()
total_generos = len(generos)
print(total_generos)

male = generos.count("Male")
female = generos.count("Female")

if male > female:
  print(f'O genero predominante é Masculino. Predominando cerca de '
   f'{(male * total_generos) % 100 }% dos personagens')

elif male < female:
  print('O genero predominante é Feminino. Predominando cerca de '
   f'{(female * total_generos) % 100 }% dos personagens')

else:
  print(f'Ambos possuem a mesma quantidade! Sendo '
      f'{(total_generos * 2) % 100}% de personagens Masculinos e '
      f'{(total_generos * 2) % 100}% de personagens Femininos.')

"""*   Qual é a idade média dos personagens por tipo de raça.


"""

racas = df['Race'].str.strip()
idade = df['Age']

idade_humanos = 0
idade_demonios = 0

quant_humanos = racas.tolist().count('Human')
quant_demonios = racas.tolist().count('Demon')


for x, y in zip(racas, idade):
  if x == 'Human':
    idade_humanos += int(y)

  else:
    idade_demonios += int(y)

media_idade_humanos = idade_humanos / quant_humanos
media_idade_demonios = idade_demonios / quant_demonios

print(f'A media de idade dos humanos é: {media_idade_humanos:.0f} anos.')
print(f'A média de idade dos Demônios é: {media_idade_demonios:.0f} anos.')

"""*   Qual é o personagem mais velhor em idade e o mais novo?

"""

nomes = df['Character Name']
idade

menor_idade = df.loc[df['Age'] == min(df['Age'])].values[0]
maior_idade = df.loc[df['Age'] == max(df['Age'])].values[0]

print(f'O personagem mais novo do anime é a {menor_idade[0]}, que tem'
      f' {menor_idade[3]} anos.')

print(f'O personagem mais velho do anime é o {maior_idade[0]}, que tem'
      f' {maior_idade[3]} anos.')

"""---
*   Quais são os tipos de Equipments distribuídos por Category

"""

unir_categorias = df.groupby('Category')['Equipment'].unique()

for categoria, equipamentos in unir_categorias.items():
    print(f'{categoria}: {", ".join(equipamentos)}')

"""---
*   Quais são os tipos de Fighting Style distribuídos por Category
"""

tipo_luta = df['Fighting Style']

categorias_estilo_luta = df.groupby('Category')['Fighting Style'].unique()

for categoria, estilo_luta in categorias_estilo_luta.items():
  print(f'{categoria}: {", ".join(estilo_luta)}')