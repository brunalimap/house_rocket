# 1.0- Sobre o dataset

Este conjunto de dados contém preços de venda de casas para King County, que inclui Seattle. Inclui casas vendidas entre maio de 2014 e maio de 2015.

# 2.0- Tópicos
- [Exercício- Aula 01](https://github.com/brunalimap/house_rocket/blob/main/notebooks/aula_python01.py) 
- [Exercício- Aula 02](https://github.com/brunalimap/house_rocket/blob/main/notebooks/aula_python02.py)   
- [Exercício- Aula 03](https://github.com/brunalimap/house_rocket/blob/main/notebooks/aula_python03.ipynb)
- [Exercício- Aula 04](https://github.com/brunalimap/house_rocket/blob/main/notebooks/aula_python04.ipynb)
- [Exercício- Aula 05](https://github.com/brunalimap/house_rocket/blob/main/notebooks/aula_python05.ipynb)
- [Exercício- Aula 06](https://github.com/brunalimap/house_rocket/blob/main/notebooks/aula_python06.py)
- [Exercício- Aula 07](https://github.com/brunalimap/house_rocket/blob/main/notebooks/aula_python07.py)


# 3.0- Biblioteca dos Dados

- <b>id</b>: ID único para cada casa vendida
- <b>date</b>: Data da venda da casa
- <b>price</b>: Preço de cada casa vendida
- <b>bedrooms</b>: Número de quartos
- <b>bathrooms</b>: Número de banheiros, onde 0,5 corresponde a um quarto com banheiro, mas sem chuveiro
- <b>sqft_living</b>:  Metragem quadrada do espaço interior dos apartamentos
- <b>sqft_lot</b>: Metragem quadrada do espaço terrestre
- <b>floors</b>: Número de andares
- <b>waterfront</b>: -  Uma variável fictícia para saber se o apartamento tinha vista para a beira-mar ou não
- <b>view</b>: Um índice de 0 a 4 de quão boa era a vista da propriedade
- <b>condition</b>: - Um índice de 1 a 5 sobre o estado do apartamento,
- <b>grade</b>: Um índice de 1 a 13, onde 1-3 fica aquém da construção e design do edifício, 7 tem um nível médio de 1. nível de construção e design e 11-13 tem um nível de construção e design de alta qualidade.
- <b>sqft_above</b>: A metragem quadrada do espaço habitacional interno que está acima do nível do solo
- <b>sqft_basement</b>: A metragem quadrada do espaço habitacional interno que está abaixo do nível do solo
- <b>yr_built</b>: O ano em que a casa foi construída inicialmente
- <b>yr_renovated</b>: O ano da última renovação da casa
- <b>zipcode</b>: Em qual CEP se encontra a casa
- <b>lat</b>: Latitude
- <b>long</b>: Longitude
- <b>sqft_living15</b>: A metragem quadrada do espaço interno de habitação para os 15 vizinhos mais próximos 
- <b>sqft_lot15</b>: A metragem quadrada dos lotes de terreno dos 15 vizinhos mais próximos.

# 4.0 Solução 

O objetivo final deste curso é entender os conceitos de manipulação de tabelas com python e a construção de visualizações com o intuito de responder questões de negócio e a construção de uma página usando a biblioteca do streamlit. E para visualizar o resultado foi realizado o deploy no Heroku que pode ser acessado através do link  construídos deste dataset é necessário acessar o link: https://analytics-house-rockets.herokuapp.com/ 

<img align="center" height="1500" width="800" src="https://github.com/brunalimap/house_rocket/blob/main/img/app_streamlit.gif">

<b>Observação:</b> Pode demorar um pouco para carregar a página, pois estou usando uma camada gratuita do Heroku e nesta camada o aplicativo hiberna após 30 min de inatividade.

# 5.0 Próximas Etapas
 
- [x] Exercícios aula 05
- [x] Exercícios aula 06
- [x] Exercícios aula 07
- [x] Apresentação das primeiras análises realizadas (streamlit)



