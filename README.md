# Matring Decoder

Este programa decodifica uma "Matring", uma matriz de números que representa uma mensagem criptografada em ASCII. A Matring foi desenvolvida pela "UNILA" (União dos Nerds para Integração da Lógica e da Aventura) para transmitir mensagens seguras, onde cada caractere da mensagem original é codificado em uma coluna da Matring.

## Explicação do Problema

A Matring é uma matriz de tamanho `4 x (N+2)`, onde `N` é o número de caracteres na mensagem original:
- **Primeira coluna** (`F`): contém um número de 4 dígitos que é uma chave para decodificação.
- **Última coluna** (`L`): contém outro número de 4 dígitos que é outra chave para decodificação.
- **Colunas intermediárias** (`M`): cada coluna representa um número de 4 dígitos, que corresponde a um caractere codificado em ASCII na mensagem.

Para decodificar cada caractere `Cᵢ` na posição `i`, usa-se a fórmula:
\[ Cᵢ = (F \times Mᵢ + L) \mod 257 \]

## Exemplo de Entrada e Saída

**Entrada**
```
41805
99934
39127
23659
```

**Saída**
```
OBI
```

## Estrutura do Código

1. **Entrada da Matring:** O programa recebe as 4 linhas de entrada, onde cada linha é uma string de números.
2. **Transformação em Colunas:** Cada coluna de 4 dígitos é extraída das linhas, formando as colunas da matriz 4x(N+2).
3. **Decodificação:** Com os valores `F`, `L`, e cada valor `Mᵢ`, a fórmula é aplicada para obter o caractere ASCII correspondente.
4. **Exibição da Mensagem:** A mensagem decodificada é impressa em uma única linha, com um caractere de fim de linha ao final.

## Como Executar

1. Execute o script em um ambiente Python 3.11+.
2. Digite as 4 linhas de números, cada linha representando uma das linhas da Matring.
3. O programa exibirá a mensagem decodificada.

## Exemplo de Uso

```plaintext
Entrada:
5686702
053144
5115038
2795214

Saída:
UNILA
```

## Requisitos

- Python 3.11 ou superior

## Considerações

- Certifique-se de que a Matring tem exatamente `4` linhas e `N+2` colunas.
- Para cada caractere decodificado, a fórmula depende das colunas intermediárias (`Mᵢ`) e das chaves (`F` e `L`), assegurando que a mensagem seja correta ao final.
