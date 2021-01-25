import pandas as pd
import plotly.express as px

df = pd.read_csv('data/kc_house_data.csv')
print(df.head())
print(df.columns) # Ver os índices das colunas
print(df['date'])

# Excluir linhas duplicadas
#df.drop_duplicates(subset ="id",  keep = False, inplace = True) 
#print(df.shape)
#print(df.dtypes)

df['date'] = pd.to_datetime(df['date'], errors='coerce')
print(df['date'])

# 1. Crie um anova coluna chamada: "house_age"
# - Se o valor da coluna "date" for maior que 2014-01-01 => 'new_house
# - Se o valor da coluna "date" for menor que 2014-01-01 => 'old_house

print('\n')
print('Questão 1')
df['house_age'] = ''
date_house = pd.to_datetime('2014-01-01')
df.loc[df['date'] >= date_house,'house_age'] = 'new_house'
df.loc[df['date'] < date_house,'house_age'] = 'old_house'
print('New House:{}'.format(df.loc[df['house_age'] == 'new_house'].value_counts().count()))
print('\n')


# 2. Crie uma nova coluna chamada: "dormitory_type"
# - Se o valor da coluna "bedrooms" for igual à 1 => 'studio'
# - Se o valor da coluna "bedrooms" for igual à 2 => 'apartament'
# - Se o valor da coluna "bedrooms" for maior que 2 => 'house'

print('Questão 2')
df['dormitory_type'] = ''
df.loc[df['bedrooms'] == 1,'dormitory_type'] = 'studio'
df.loc[df['bedrooms'] == 2,'dormitory_type'] = 'apartament'
df.loc[df['bedrooms'] > 2, 'dormitory_type'] = 'house'
print(df['dormitory_type'].value_counts())
print(df.sample(5))
print('\n')

# 3. Crie uma nova coluna chamada: "condition_type"
# - Se o valor da coluna "condition" for menor ou igual à 2 => 'bad'
# - Se o valor da coluna "condition" for igual à 3 ou 4 => 'regular'
# - Se o valor da coluna "condition" for igual à 5 => 'good'

print('Questão 3')
df['condition_type'] = ''
df.loc[df['condition'] <= 2,'condition_type'] = 'bad'
df.loc[df['condition'] == 3,'condition_type'] = 'regular'
df.loc[df['condition'] == 4,'condition_type'] = 'regular'
df.loc[df['condition'] == 5,'condition_type'] = 'good'
print(df.sample(5))
print('\n')


# 4. Modifique o TIPO da coluna "condition" para STRING
print('Questão 4')
df['condition'] = df['condition'].astype(object)
print(df.dtypes)
print('\n')

# 5. Delete as colunas "sqft_living15" e "sqft_lot15"
cols = ['sqft_living15','sqft_lot15']
df = df.drop(cols, axis = 1)
print('\n')
#print(df.columns)

# 6. Modifique o TIPO da coluna "yr_built" para DATE
df['yr_built'] = pd.to_datetime(df['yr_built'],format='%Y',errors='coerce')
print('\n')

# 7. Modifique o TIPO da coluna "yr_renovated" para DATE
print('Questão 7')
df['yr_renovated'] = pd.to_datetime(df['yr_renovated'],format='%Y',errors='coerce')
print(df.dtypes)
print('\n')

# 8. Qual a data mais antiga de construção de um imóvel?
print('Questão 8')
a = df[['id','yr_built']].sort_values('yr_built', ascending=True)
print(a)
print('\n')

# 9. Qual a data mais antiga de renovação de um imóvel? (Preciso voltar nessa)

print('Questão 9')
b = df[['id','yr_renovated']].sort_values('yr_renovated', ascending=True)
print(b)
print('\n')

# 10. Quantos imóveis tem 2 andares?
print('Questão 10')
print('Quantidade de valores unicos na colunas floors {}'.format(df['floors'].unique()))
c = df[df['floors'] == 2.].shape[0]
print('Quantidade de casas com mais de 2 andares no dataset: {}'.format(c))
print("\n")

# 11. Quantos imóveis estão com a condição igual à "regular"?
print('Questão 11')
print('Quantidade de valores unicos na colunas condition_type {}'.format(df['condition_type'].unique()))
print("\n")
d = df[df['condition_type'] == 'regular'].shape[0]
print('Quantidade de casas com situação regular no conjunto de dados: {}'.format(d))
print("\n")


# 12. Quantos imóveis estão com a condição igual a "bad" e possuem "vista para água"?
print('Questão 12')
e=(df[(df['condition_type'] == 'bad') & (df['waterfront'] == 1)].shape[0])
print('Quantidade de imóveis que estão com condição igual a "bad" e possuem "vista para água": {}\n'.format(e))

# 13. Quantos imóveis estão com a condição igual a "good" e são "new_house"?
print('Questão 13')
f = df[(df['condition_type'] == 'good') & (df['house_age'] == 'new_house')].shape[0]
print('Quantidade de imóveis que estão em condição "good" e são "new_house": {}\n'.format(f))


# 14. Qual o valor do imóvel mais caro do tipo "studio"?
print('Questão 14')
g = df['price'].loc[df['dormitory_type'] == 'studio'].max()
print('O imóvel mais caro do tipo "studio": {}\n'.format(g))
print('\n')


# 15. Quantos imóveis do tipo "apartament" foram reformados em 2015?
print('Questão 15')
h = df[(df['dormitory_type'] == 'apartament') & (df['yr_renovated'] == '2015-01-01')].shape[0]
print(' Quantidade de imóveis do tipo "apartament" que foram reformados em 2015: {}\n'.format(h))



# 16. Qual o maior número de quartos que um imóvel do tipo "house" possui?
print('Questão 16')
print('Casa com o maior número de quartos tipo "House" é: {}'.format(df['bedrooms'].loc[df['dormitory_type'] == 'house'].max()))
print('\n')

# 17. Quandos imóveis "new_house" foram reformados no ano de 2014?
print('Questão 17')
print('Quantidade de imóveis "new_house" foram reformados no ano de 2014: {}'.format(df[(df['house_age'] == 'new_house') & (df['yr_renovated'] == '2014-01-01')].shape[0]))
print('\n')

# 18. Selecione as colunas: "id", "date", "price", "floors", "zipcode" pelo método:

print('Questão 18')

# - Direto pelo nome das colunas
print(df[['id', 'date', 'price', 'floors', 'zipcode']])

# - Pelos índices
print('='*70)
print(df.iloc[:,[0,1,2,7,16]])

# - Pelos índices das linhas e o nome das colunas 
print('='*70)
print(df.loc[:,['id', 'date', 'price', 'floors', 'zipcode']])


# - Índices booleanos
print('='*70)
cols_boolean = [True,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False]
print(df.loc[:,cols_boolean])
print('\n')

# 19. Salve um arquivo .csv com somente as colunas do item 10 ao 17
df1 = df.iloc[:,10:18]
df1.to_csv('data/arquivo01.csv')
print('\n')

# 20. Modifique a cor dos pontos no mapa de "pink" para "verde-escuro"

#selecionando as colunas necessárias
cols_maps = df[['id','price','lat','long']]

#criando o mapa
maps_v1 = px.scatter_mapbox(data_frame= df,
lat='lat',
lon='long',
hover_name='id',
hover_data=['price'],
color_discrete_sequence=['darkgreen'],
zoom=3,
mapbox_style='open-street-map',
height=300)

# definindo as margens do mapa
maps_v1.update_layout(margin={'r':0, 't':0, 'l':0, 'b':0})

# color_discrete_sequence=['fuchsia'] cor rosa

maps_v1.show()

#salvando o mapa
maps_v1.write_html('img/maps_v1.html')


