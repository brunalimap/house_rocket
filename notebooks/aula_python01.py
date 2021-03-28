import pandas as pd

df = pd.read_csv('data/kc_house_data.csv')

# Para verificar o dataset
#print(df.head())

# Para verificar os tipos das variáveis das colunas
#print(df.dtypes)

# Primeiras Perguntas dos CEO

# 1- Quantas casas estão disponíveis para comprar?

# Estratégia
# 1. Selecionar a coluna 'id'
# 2. Contar o número de valores únicos

print("\nQuantidade de casas disponíveis para compra: {}".format(len(df['id'].unique())))
print("\n")

# 2- Quantos atributos as casas possuem?


# Considerando id e date 
print("\nQuantidade de atributos as casas possuem: {}".format(len(df.columns)))
print("\n")

# Se considerar id e date 
atributos = len(df.drop(['id','date'],axis=1).columns)
print("\nQuantidade de atributos que as  casas possuem não considerando id e data: {}".format(atributos))
print("\n")


# 3- Quais são os atributos das casas?
print("\nOs atributos são: {}".format(df.columns))
print("\n")

# 4- Qual a casa mais cara ( casa com o maior valor de venda)?
#preciso que mostre o ID da casa
sales = df[['id','price']].sort_values('price', ascending=False).reset_index(drop= True).loc[0,'id']
print("\n A casa com o maior valor de venda é {}".format(sales))
print("\n")


# 5- Qual a casa com o  maior número de quartos?
bedrooms = df[['id','bedrooms']].sort_values('bedrooms',ascending=False).reset_index(drop=True).loc[0,'id']
print("\n A casa com o maior quantidade de quartos: {}".format(bedrooms))
print("\n")

# 6- Qual a soma total de quartos do conjunto de dados?
print('Total de quartos que tem no dataset: {}'.format(df['bedrooms'].sum()))
print("\n")

# 7- Quantas casas possuem 2 banheiros?
a = df.query('bathrooms == 2')['bathrooms'].count()
print('O número de casas com 2 banheiros é de: {}'.format(a))
print("\n")

# 8- Qual o preço médio de todas as casas no conjunto de dados?
b = df['price'].mean()
print('Preço médio de todas as casas: {}'.format(round(b,2)))
print("\n")

# 9- Qual o preço médio de casas com 2 banheiros?
c = df.loc[df['bathrooms'] == 2, 'price'].mean()
print('Preço médio das casas com 2 banheiro: {}'.format(round(c,2)))
print("\n")


# 10- Qual o preço mínimo entre as casas com 3 quartos?
d = df.query('bedrooms == 3')['price'].min()
print('Preço minimo em casas com dois andares: {}'.format(round(d,2)))
print("\n")

# 11- Quantas casas possuem mais de 300 metros quadrados na sala de estar?
df['m2_living'] = df['sqft_living']*0.093
m2 = len(df.loc[df['m2_living'] > 300,'id'])
print('Quantidade de casa que possuem mais de 300 metros quadrados é {}'.format(m2))
print("\n")

# 12- Quantas casas tem mais de 2 andares?
e = df.loc[df['floors'] > 2,'id'].size
print('Quantidade de casas com mais de 2 andares no dataset: {}'.format(e))
print("\n")

# 13- Quantas casas tem vista para o mar?
print('Casas com vista para o mar: {}'.format(df[df['waterfront']==1].shape[0]))
print("\n")

# 14- Das casas com vista para o mar, quantas tem 3 quartos?
f = len(df.loc[(df['waterfront'] == 1) & (df['bedrooms'] == 3),'id'])
print('Casas com vista para o mar e com 3 quartos: {}'.format(f))
print("\n")

# 15- Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros banheiros?
print('Total de com mais de 2 banheiros: {}'.format(df[(df['m2_living'] > 300) & (df['bathrooms']> 2)].shape[0]))
