# Plan — Motor de Reembolso

## 1. Stack

### Linguagem

Python.

### Motivo

Foi escolhida por permitir uma implementação simples para leitura e escrita de JSON, criação de CLI e testes automatizados.

### Testes

Pytest.

### Motivo

Permite escrever testes pequenos e objetivos para cada regra da spec.

## 2. Visão da solução

A solução será dividida em quatro partes simples:

1. CLI recebe os caminhos dos arquivos de entrada e saída.
2. Leitura e validação básica do JSON de entrada.
3. Motor de regras calcula o reembolso de cada despesa.
4. Resultado é gravado em JSON.

## 3. Fluxo

```text
JSON de entrada
      ↓
Leitura dos dados
      ↓
Validações
      ↓
Aplicação das regras
      ↓
Cálculo dos totais
      ↓
JSON de saída
```

## 4. Organização do código

A implementação deve permanecer pequena e fácil de entender.

Responsabilidades principais:

- entrada e saída de arquivos;
- regras de reembolso;
- cálculo dos limites diários;
- identificação de duplicatas;
- geração do resultado.

## 5. Modelo de processamento

Cada despesa será processada na ordem da entrada.

Durante o processamento, o sistema manterá controle do valor já utilizado por dia e categoria para alimentação e transporte.

Hospedagem será tratada por registro.

## 6. Decisões técnicas

### Usar números decimais para valores monetários

**Decisão:** utilizar representação decimal adequada para dinheiro.

**Alternativa descartada:** números de ponto flutuante comuns.

**Motivo:** evitar erros de precisão em valores monetários.

### Processar despesas em sequência

**Decisão:** manter a ordem original da entrada.

**Alternativa descartada:** ordenar as despesas por data ou valor antes do cálculo.

**Motivo:** a spec define que o limite diário é consumido na ordem recebida.

### Manter regras separadas da CLI

**Decisão:** o cálculo não deve depender diretamente da interface de linha de comando.

**Alternativa descartada:** colocar leitura, cálculo e escrita em um único bloco.

**Motivo:** facilita testes e manutenção.

## 7. Estratégia de testes

Serão criados testes automatizados para:

- alimentação dentro do limite;
- alimentação acima do limite;
- várias despesas de alimentação no mesmo dia;
- transporte dentro e acima do limite;
- hospedagem dentro e acima do limite;
- despesa exatamente de R$ 100,00 sem nota;
- despesa acima de R$ 100,00 sem nota;
- categoria não permitida;
- despesa fora do período;
- duplicata;
- valor zero;
- valor negativo;
- cálculo dos totais;
- geração da saída JSON.

## 8. Validação final

Antes da entrega:

1. executar todos os testes;
2. validar o exemplo de entrada do desafio;
3. conferir o JSON de saída;
4. revisar a rastreabilidade entre spec, tasks, commits e testes;
5. exportar as sessões do Claude Code;
6. atualizar o relatório final.
