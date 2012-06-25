# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Índices invertidos e busca booleana
# ===================================
# 
# _Flávio Codeço Coelho (Com a ajuda dos alunos do curso de Sistemas de recuperação de Informações da EMAp)_
# 
# Nesta prática, vamos contruir um indice invertido e uma máquina de busca booleana simples.
# 
# Para agilizar nosso trabalho, vamos utilizar a biblioteca [NLTK](http://nltk.org) para processamento de linguagem natural.

# <codecell>

import nltk

# <markdowncell>

# Em seguida vamos importar mais coisas necessárias para o nosso trabalho. Note que estamos baixando a obra completa de Machado de Assis, com a qual iremos alimentar nosso índice.

# <codecell>

from nltk.corpus import machado
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
import string
from collections import defaultdict
from nltk.stem.snowball import PortugueseStemmer
from nltk

# <markdowncell>

# Vamos também baixar o banco de *stopwords* do NLTK. Stop words são um conjunto de palavras que normalmente carregam baixo conteúdo semântico e portanto não são alvo de buscas.

# <codecell>

nltk.download('stopwords')

# <markdowncell>

# Lendo o texto *puro* dos livros de Machado:

# <codecell>

textos = [machado.raw(id) for id in machado.fileids()]
len(textos)

# <markdowncell>

# Carregando a  lista de stopwords em lingua portuguesa para limpeza dos textos. Note que é preciso trazer as palavras para *UTF-8* antes de usá-las.

# <codecell>

sw = stopwords.words('portuguese') + list (string.punctuation)
swu = [word.decode('utf8') for word in sw]

# <markdowncell>

# Um outro ingrediente essencial é um stemmer para a nossa língua. O Stemmer reduz as palavras a uma abreviação que se aproxima da "raiz" da palavra.

# <codecell>

stemmer = PortugueseStemmer()

# <markdowncell>

# Preparando o Texto
# ------------------
# 
# Na célula abaixo, vamos normalizar os nossos textos trazendo todas as palavras para caixa baixa e abreviando-as de forma a deixar apenas as suas raízes. Neste passo, removeremos também as *stopwords*. Tenha paciência, esta análise vai levar algum tempo...

# <codecell>

textos_limpos = []
for texto in textos:
    tlimpo = [stemmer.stem(token.lower()) for token in WordPunctTokenizer().tokenize(texto) if token not in swu]
    textos_limpos.append(tlimpo)

# <markdowncell>

# Vejamos uma amostra do resultado:

# <codecell>

textos_limpos[0][150:160]

# <markdowncell>

# Construindo um Índice Invertido
# -------------------------------
# 
# De posse da nossa lista de termos *normalizados*, podemos agora construir o nosso índice invertido.

# <codecell>

indice = defaultdict(lambda:set([]))
for tid,t in enumerate(textos_limpos):
    for term in t:
        indice[term].add(tid)

# <markdowncell>

# Podemos verificar a estrutura interna do nosso índice, procurando por uma palavra:

# <codecell>

indice[stemmer.stem(u"Salário")]

# <markdowncell>

# Vamo ver o contexto em que a palavra *Salário* ocorre em um dos textos

# <codecell>

Text(textos[193].encode('utf8').split()).concordance("Salário")

# <codecell>

def busca(consulta):
    """
    A construção de uma função de busca é deixada com exercício ao leitor
    """
    pass
    
    

# <markdowncell>

# Mas já podemos utilizar nosso índice diretamente com alguns termos e verificar como o mesmo é eficiente. 

# <codecell>

%time
results = indice[stemmer.stem('nacional')]&indice[stemmer.stem('perdi')] - indice[stemmer.stem('campo')]
results

# <markdowncell>

# Para um exame mais preciso do tempo de execução da nossa consulta, podemos usar a mágica do *%%timeit*

# <codecell>

%%timeit
results = indice[stemmer.stem('nacional')]&indice[stemmer.stem('perdi')] - indice[stemmer.stem('campo')]
results

# <codecell>


