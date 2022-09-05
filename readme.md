# Curso Python 3

```python
'Por' : 'Gustsavo Guanabara'
```

## Utilizando módulos

O Python, assim como a linguagem Java, trabalha a partir de pacotes, a partir de módulos instalados e módulos pré-definidos.

Os programas em Python, por padrão, têm um conjunto limitado de comandos. Isso garante que os programas sejam rápidos, pequenos e não gastem memória e não tenham outros gastos adicionais sem necessidade. Se o programa precisar de alguma funcionalidade que não esteja fornecida pelos módulos pré-definidos, basta importar o módulo correspondente.

Para incluir um módulo ao programa, basta usar o comando `import`:

```python
import bebida
import doce
```

Ao importar `bebida` todas as bebidas são disponibilizadas ao program. O mesmo ocorre ao importar `doce`. Acontece que nem todas as bebidas e/ou doces serão utilizados. Da biblioteca de doces pode-se querer apenas um pudim e da biblioteca de bebidas pode-se querer apenas um café. Para fazer essas importações únicas o comando se modifica:

```python
from bebida import café
from doce import pudim
```

É o que ocorre com a biblioteca `math`. Ela contém uma série de funcionalidades matemáticas extras ao conjunto de módulos pré-definidos disponibilizados pelo Python, como `ceil`, `floor`, `trunc`, `pow`, `sqrt` e `factorial`. 

Importando o módulo matemático inteiro:

```python
import math
```

Importando apenas a função que calcula a raiz quadrada:

```python
from math import sqrt
```

Ao importar somente a função `sqrt` nenhuma outra funcionalidade pode ser utilizada no programa.

Para importar mais de uma funcionalidade, basta adicionar a vírgula acrescida do nome da função:

```python
from math import sqrt, ceil
```

## Manipulando texto

Considere:

'Curso em Vídeo Python'

Para qualquer pessoa é uma frase, mas qualquer linguagem de programação chama de cadeia de caracteres, string ou, simplesmente, cadeia de texto.

Para o Python toda cadeia de texto deve estar entre aspas simples ou entre aspas duplas. Existe também a possibilidade de usar três aspas duplas.

Atribuindo a string acima a uma variável:

```python
frase = 'Curso em Vídeo Python'
```

O Python vai colocar essa frase na memória do computador, mas não de forma inteira. Ele vai criar mini espaços dentro da memória do computador e dentro de cada mini espaço vai uma letra. Cada um desses mini espaços vai receber um índice, um número sequencial começando com 0 e indo até onde for necessário para caber todos caracteres da frase (incluindo os espaços entre palavras). Isso permite facilmente executar algumas operações:

- Fatiamento: fatiar uma string é conseguir pedaços dela. O Python faz isso de forma muito simples:

```python
# variável + número do índice
frase[9]

# Fatiando para conseguir os caracteres do índice 9 até o 12
# A técnica para de fatiar no 13, mas não o exibe
frase[9:13]
# Saída:
# V

# O mesmo acontece com o fatiamento de 9 até o 21
frase[9:21]
# Saída:
# Vídeo Python

# Fatiando de 9 até o 21 pulando de 2 em 2 caracteres
frase[9:21:2]
# Saída:
# VdoPto

# Fatiando de 0 até o 5
frase[:5]
# Saída:
# Curso

# Fatiando de 15 até o final
frase[15:]
# Saída:
# Python

# Fatiando do 9 até o final pulando de 3 em 3 caracteres
frase[9::13]
# Saída:
# VePh
```

- Análise: analisar uma string é saber algumas informações sobre ela, como: seu tamanho, com que letra ela começa, com que letra ela termina, a primeira palavra inteira. Veja:

```python
# A função len() informa o comprimento da frase
len(frase)
# Saída:
# 21

# A função count() informa quantas vezes determinado caractere aparece na frase
frase.count('o')
# Saída:
# 3

# A função count() informa quantas vezes determinado caractere aparece na frase já com o fatiamento (entre 0 e 13)
frase.count('o',0,13)
# Saída:
# 1

# A função find() faz busca na frase e retorna em qual posição ele encontrou
# Caso não encontre nada, retorna o valor -1
frase.find('deo')
# Saída:
# 11

# O operador in faz busca na frase e retorna um valor booleano
'Curso' in frase
# Saída:
# True
```

- Transformação: via de regra uma lista de string é imutável (não se pode mexer direto nos elementos dela), mas é possível através de métodos.

```python
# O método replace() vai encontrar um elemento e substituí-lo por outro
frase.replace('Python', 'Android')
# Saída:
# Curso em Vídeo Android

# O método upper() vai converter todo a string em maiúscula
frase.upper()
# Saída:
# CURSO EM VÍDEO PYTHON

# O método lower() vai converter todo a string em minúscula
frase.lower()
# Saída:
# curso em vídeo python

# O método capitalize() vai converter todo a string em minúscula e deixar o primeiro caractere em maiúscula
frase.capitalize()
# Saída:
# Curso em vídeo python

# O método title() vai analisar quantas palavras a string tem e vai capitalizar palavra por palavra
frase.title()
# Saída:
# Curso Em Vídeo Python

# O método strip() vai remover todos os espaços em branco no início e no final da string
frase = '   Aprenda Python  '
frase.strip()
# Saída:
# Aprenda Python

# O método rstrip() (right strip) vai remover todos os espaços em branco do final da string
frase = '   Aprenda Python  '
frase.rstrip()
# Saída:
#    Aprenda Python

# O método lstrip() (left strip) vai remover todos os espaços em branco do início da string
frase = '   Aprenda Python  '
frase.lstrip()
# Saída:
# Aprenda Python  
```

- Divisão: permite dividir strings.

```python
# O método split() faz a divisão da string pelos espaços. Cada palavra vai receber uma nova indexação. Tecnicamente o split() gera uma nova lista com todas as palavra de uma cadeia de caracteres.
frase.split()
# Saída:
# Curso
# em
# Vídeo
# Python
```

- Junção: junta palavras/caracteres

```python
# O método join() faz a divisão da string pelos espaços.
'-'.join(frase)
# Saída:
# Curso-em-Vídeo-Python
```