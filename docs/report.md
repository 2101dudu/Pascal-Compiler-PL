<h1 style="text-align: center">Processamento de Linguagens</h1>
<h3 style="text-align: center">Grupo 1</h1>
<p style="text-align: center">1 de junho de 2025</p>
<div style="text-align: center; display: flex; justify-content: space-around">
    <div>
        <div><b>Edgar Ferreira</b></div>
        <div>A99890</div>
    </div>
    <div style="margin-right: 18px;">
        <div><b>Eduardo Faria</b></div>
        <div>A104353</div>
    </div>
    <div>
        <div><b>Nuno Silva</b></div>
        <div>A104089</div>
    </div>
</div>

# Introdução
Este relatório tem como objetivo documentar e detalhar todo o processo de concepção do trabalho prático desenvolvido na unidade curricular de Processamento de Linguagens. O fundamento deste trabalho é o desenvolvimento de um compilador capaz de analisar, interpretar e traduzir código Pascal (_standard_) para código máquina de forma direta ou indireta. Neste caso, optou-se por por traduzir o código para um formato intermédio, a partir do qual se gerou, finalmente, o código máquina que será interpretado pela máquina virtual [EWV](https://ewvm.epl.di.uminho.pt/).

# 1. Arquitetura
Na implementação do nosso compilador, optámos por uma arquitetura modular e progressiva, que nos permitisse evoluir mantendo a clareza e separação das diversas responsabilidades. Os vários componentes que constituem o compilador encontram-se nos próximos subcapitulos. 

## 1.1 Lexer
O primeiro passo do processo de compilação é a análise léxica, que consiste em transformar o código fonte numa sequência de _tokens_, através de um _lexer_. Para esta tarefa, utilizámos o módulo `lex` da biblioteca [ply](https://www.dabeaz.com/ply/ply.html), uma ferramenta amplamente utilizada nas aulas práticas, que nos facilitou a construção do analisador léxico.

Dada a natureza relativamente estruturada da linguagem _Pascal_, a implementação do _lexer_ foi bastante direta. Ainda assim procurámos seguir uma abordagem modular e robusta, antecipando possíveis extensões futuras.

O _lexer_ desenvolvido reconhece um conjunto alargado de literais, plavras reservadas e _tokens_:

```python
literals = ['(', ')', ';', '.', ',', ':', '{', '}', '>', '<', '=', '*', '+', '-', '/', '[', ']']
tokens = (
    'PROGRAM', 'VAR', 'BEGIN', 'END', 'IF', 'THEN', 'ELSE', 'FOR', 'TO', 'DO', 'WHILE', 'DIV', 'MOD', 'AND', 'OR', 'NOT', 'ARRAY', 'OF', 'DOWNTO', 'FUNCTION', 'PROCEDURE',
    'id', 'string', 'num', 'boolean'
)
```

Uma das decisões que tomámos foi tratar todas as palavras reservadas de forma _case-insensitive_, à semelhança do comportamento tradicional do _Pascal_. 

Fazendo uso do `ply.lex`, e assegurando o reconhecimento dos padrões textuais através de expressões regulares, a "tokenização" dos textos de entrada conseguiu ser realizada, alertando com um erro para qualquer _token_ não reconhecido.

O seguimento do reconhecimento de um texto consegue, desta forma, ser encadeado com a biblioteca complementar `ply.yacc`.


## 1.2 _Parser_
Os _tokens_ e símbolos literais provenientes do _lexer_ são reutilizados para a criação de uma gramática de _Pascal_. Esta gramática independente de contexto (GIC) é responsável por determinar o comportamento esperado do _parser_ e é um pilar fundamental na criação de um pareser _yacc_. 


### 1.2.1 Gramática Independente de Contexto 
A GIC faz uso de um conjunto de símbolos terminais e não terminais e caracteres literais para estipular regras de _parsing_. Segue uma fundamentação teórica baseada na ... LALR1 e um reconhecimento _bottom-up_. Os axiomas utilizados foram estruturados de forma a erradicar o número de conflitos _reduce/reduce_ e minimzar o número de conflitos _shift/reduce_.

O grupo concebeu um pequeno programa em _python_ (`src/sin_gen.py`) que traduz um texto BNF-puro, por exemplo:
```txt
Unary : NOT Unary
      | Factor
```
em código _python_:
```python
def p_unary_not(p):
    """
    Unary : NOT Unary
    """

def p_unary_factor(p):
    """
    Unary : Factor
    """
```
A GIC final encontra-se no ficheiro `src/prod.txt`.

### 1.2.2 Analisador sintático
Com todas as produções da GIC traduzidas em código python, foi possível desenvolver toda a semântica necessária para a criação e estruturação de uma [árvore de sintátaxe abstrata](#visualizador-árvore-sintática), que será o pilar intermédio entre a gramática criada e a produção do código máquina.

De forma a promover uma interpretação mais fluida e familiar, decidiu-se que esta árvore seria constituída por nodos compostos pelo nome que os identifica, bem como por uma sequência de nodos filhos e folhas. Esta sequência inclui tanto nodos como folhas, e não apenas nodos, precisamente para permitir a máxima simplificação da árvore gerada. Ao utilizar folhas esclarecedoras e autoexplicativas em vez de nodos completos, é possível ‘podar’ a árvore em diversos ramos, reduzindo substancialmente a sua profundidade ou a profundidade de certas subárvores.

## 1.3 Tradutor
Toda a lógica do tradutor está "compilada" no ficheiro `src/gen.py` que, a partir do output gerado pelo _parser_, é capaz de gerar todo o código máquina que será futuramente interpretado pela máquina virtual.

Após construção da Árvore Sintática Abstrata (AST) durante a análise sintática, começamos a análise semântica e a geração de código da linguagem. 

A função de tradução percorre/visita recursivamente todos os nodos da árvore, analisando a sua estrutura e gerando as respetivas instruções de código máquina consoante o tipo de cada nodo.


# Visualizador Árvore Sintática
Durante o desenvolvimento da árvore de sintaxe abstrata, o grupo decidiu complementar o projeto com um _website_ local que gráficamente representasse a mesma. A localização de erros e incongruências foi vastamente facilitada com o auxílio da visualização das árvores.


# Exemplos