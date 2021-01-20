import pandas as pd


df = pd.read_csv('data/kc_house_data.csv')

# Para verificar o dataset
#print(df.head())

# Para verificar os tipos das variáveis das colunas
#print(df.dtypes)

print("Primeiras Perguntas dos CEO da House Rocket")

# 1- Quantas casas estão disponíveis para comprar?

print("1- Quantidade de casas disponíveis para compra: {}".format(df.shape[0]))
print("\n")

# 2- Quantos atributos as casas possuem?
print("2- Quantidade de atributos as casas possuem: {}".format(df.shape[1]))
print("\n")

# 3- Quais são os atributos das casas?
print("3- Os atributos são: {}".format(df.columns))
print("\n")

# 4- Qual a casa mais cara ( casa com o maior valor de venda)?
#preciso que mostre o ID da casa
sales = df[['id','price']].sort_values('price', ascending=False)
print("4- A casa com o maior valor de venda é \n {}".format(sales.head(1)))
print("\n")


# 5- Qual a casa com o  maior número de quartos?
bedroom = df[['id','bedrooms']].sort_values('bedrooms',ascending=False)
print("5- A casa com o maior quantidade de quartos: \n {}".format(bedroom.head(1)))
print("\n")

# 6- Qual a soma total de quartos do conjunto de dados?
print(' 6- Total de quartos que tem no dataset: {}'.format(df['bedrooms'].sum()))
print("\n")

# 7- Quantas casas possuem 2 banheiros?
a = df.query('bathrooms == 2')['bathrooms'].count()
print(' 7- Quantidade de casas com 2 banheiros no dataset: {}'.format(a))
print("\n")

# 8- Qual o preço médio de todas as casas no conjunto de dados?
b = df['price'].mean()
print('8- Preço médio de todas as casas: {}'.format(round(b,2)))
print("\n")

# 9- Qual o preço médio de casas com 2 banheiros?
c = df.loc[df['bathrooms'] == 2, 'price'].mean()
print('9- Preço médio das casas com 2 banheiro: {}'.format(round(c,2)))
print("\n")


# 10- Qual o preço mínimo entre as casas com 3 quartos?
d = df.query('bedrooms == 3')['price'].min()
print('10- Preço minimo em casas com dois andares: {}'.format(round(d,2)))
print("\n")

# 11- Quantas casas possuem mais de 300 metros quadrados na sala de estar?
df['m2_living'] = df['sqft_living']*0.092
print('Quantidade de casa que possuem mais de 300 metros quadrados é {}'.format(df[df['m2_living']>300].shape[0]))
print("\n")

# 12- Quantas casas tem mais de 2 andares?
e = df[df['floors'] > 2].shape[0]
print('Quantidade de casas com mais de 2 andares no dataset: {}'.format(e))
print("\n")

# 13- Quantas casas tem vista para o mar?
print('Casas com vista para o mar: {}'.format(df[df['waterfront']==1].shape[0]))
print("\n")

# 14- Das casas com vista para o mar, quantas tem 3 quartos?
f = df[(df['waterfront'] == 1) & (df['bedrooms'] == 3)].shape[0]
print('Casas com vista para o mar e com 3 quartos: {}'.format(f))
print("\n")

# 15- Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros banheiros?
print('Total de casas com mais de 2 banheiros e que tenha 300 m² de sala de estar: {}'.format(df[(df['m2_living'] > 300) & (df['bathrooms']> 2)].shape[0]))
