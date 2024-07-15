## Trabalho 2 - Inteligência Artificial - Diagnóstico de Farol de Bicicleta

Este repositório contém a solução da segunda questão do segundo trabalho de Inteligência Artificial, utilizando a biblioteca ProbLog para diagnosticar problemas em um farol de bicicleta movido a dínamo.

### Problema

O objetivo é construir um modelo probabilístico que represente o funcionamento do farol, considerando as seguintes variáveis e suas dependências:

**Variáveis:**

| Variável | Significado                                  | Valores        |
|----------|----------------------------------------------|---------------|
| Li       | Luz ligada (Light is on)                   | t/f           |
| Str      | Condição da rua (Street condition)        | dry, wet, snow_covered |
| Flw      | Volante do Dínamo desgastado (Dynamo flywheel worn out) | t/f           |
| R        | Dínamo deslizante (Dynamo sliding)         | t/f           |
| V        | Dínamos mostra a tensão (Voltagem) (Dynamo shows voltage) | t/f           |
| B        | Lâmpada ok (Light bulb ok)                | t/f           |
| K        | Cabo ok (Cable ok)                         | t/f           |

**Dependências:**

* As variáveis `Str`, `Flw`, `B` e `K` são independentes aos pares.
* As variáveis `(R, B)`, `(R, K)`, `(V, B)` e `(V, K)` são independentes.
* A seguinte equação é válida: 
    * `P(Li|V, R) = P(Li|V)`
    * `P(V|R, Str) = P(V|R)`
    * `P(V|R, Flw) = P(V|R)`

A tabela de probabilidades condicionais é fornecida no enunciado do trabalho.

### Solução

A solução utiliza a biblioteca ProbLog para modelar o problema como um programa lógico probabilístico. O código define as variáveis aleatórias, as probabilidades a priori e as relações de dependência entre elas. A consulta calcula a probabilidade da variável `dynamo_shows_voltage` ser verdadeira, dado que a `street_condition` é verdadeira.

### Arquivos

* `main.py`: Contém o código em ProbLog que modela o problema e realiza a consulta.

### Como executar

1. Certifique-se de ter o Python 3 instalado.
2. Instale a biblioteca ProbLog: `pip install problog`
3. Execute o script `main.py`: `python main.py`

### Saída

O script imprimirá no console a probabilidade calculada pela consulta, que representa a chance do dínamo mostrar voltagem dado que a condição da rua é verdadeira. 

### Observações

* O código foi desenvolvido com base no exemplo fornecido no enunciado do trabalho: [https://dtai.cs.kuleuven.be/problog/tutorial/basic/02_bayes.html](https://dtai.cs.kuleuven.be/problog/tutorial/basic/02_bayes.html).
* A interpretação dos resultados e a análise da solução são deixadas como exercício para o leitor. 
