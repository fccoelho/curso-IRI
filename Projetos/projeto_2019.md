# Projeto Final 2019
Neste projeto cada aluno deve eleger um corpus de documentos de tamanho medio (pelo menos milhares de documentos). Todas as tarefas a seguir serao realizadas sobre este corpus.

## Indexaçao
1. Utilizando o Whoosh indexar o seu corpus e implementar uma funçao que apresentes para os top 10 documentos da resposta a uma consulta, trechos dos documentos contendo os termos da consulta.
1. Contruir uma funçao de busca que aceite consultas frasais e facetaçao dos resultados.

## Modelagem de Assuntos
1. Usando a biblioteca Gensim, treine um modelo LSI e LDA para o seu corpus propondo uma metodologia para otimizaçao do numero de assuntos
2. Construa Uma matriz de similaridade entre os documentos do corpus a partir dos pesos 

## Word2vec
1. Ainda usando a biblioteca Gensim, Construa uma representaçao vetorial semantica(word2vec) do seu corpus de escolha. Podem seguir este [tutorial](https://rare-technologies.com/word2vec-tutorial/)
2. Construa uma representaçao simila usando [FastText](https://radimrehurek.com/gensim/models/fasttext.html#gensim.models.fasttext.FastText). Veja este [Tutorial](https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/FastText_Tutorial.ipynb)
