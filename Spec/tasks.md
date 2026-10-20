# Tasks — Motor de Reembolso

## T-001 — Criar estrutura inicial do projeto

**Atende:** organização geral do projeto.

**O que fazer:** criar estrutura de código, testes e configuração inicial.

**Critério de aceite:** estrutura criada e projeto preparado para executar testes.

---

## T-002 — Criar leitura da entrada JSON

**Atende:** interface de entrada definida no desafio.

**O que fazer:** receber o arquivo de despesas e carregar os dados necessários para o cálculo.

**Critério de aceite:** teste de leitura de um arquivo JSON válido passa.

---

## T-003 — Validar valores e período de competência

**Atende:** seções 7, 9 e 10 da spec.

**O que fazer:** recusar valores iguais ou menores que zero e despesas fora do período.

**Critério de aceite:** testes de valor inválido e período passam.

---

## T-004 — Validar categorias permitidas

**Atende:** seção 2 da spec.

**O que fazer:** permitir alimentação, transporte urbano e hospedagem e recusar outras categorias.

**Critério de aceite:** testes de categoria permitida e não permitida passam.

---

## T-005 — Identificar despesas duplicadas

**Atende:** seção 8 da spec.

**O que fazer:** manter a primeira ocorrência e recusar repetições consideradas duplicadas.

**Critério de aceite:** teste com despesas duplicadas passa.

---

## T-006 — Aplicar regra de nota fiscal

**Atende:** seção 5 da spec.

**O que fazer:** exigir nota apenas para valores maiores que R$ 100,00.

**Critério de aceite:** testes com R$ 100,00 e acima de R$ 100,00 passam.

---

## T-007 — Aplicar limite diário de alimentação

**Atende:** seções 3, 4 e 11 da spec.

**O que fazer:** limitar alimentação a R$ 60,00 por dia, acumulando as despesas na ordem da entrada.

**Critério de aceite:** testes com uma e várias despesas no mesmo dia passam.

---

## T-008 — Aplicar limite diário de transporte urbano

**Atende:** seções 3, 4 e 11 da spec.

**O que fazer:** limitar transporte urbano a R$ 80,00 por dia, acumulando as despesas na ordem da entrada.

**Critério de aceite:** testes com uma e várias despesas no mesmo dia passam.

---

## T-009 — Aplicar limite de hospedagem

**Atende:** seções 3 e 4 da spec.

**O que fazer:** limitar cada registro de hospedagem a R$ 250,00.

**Critério de aceite:** testes de hospedagem dentro e acima do limite passam.

---

## T-010 — Gerar resultado por despesa

**Atende:** seções 12 e 13 da spec.

**O que fazer:** gerar situação, motivo, valor solicitado, reembolsável e não reembolsável para cada item.

**Critério de aceite:** teste do formato do resultado individual passa.

---

## T-011 — Calcular resumo do período

**Atende:** seção 13 da spec.

**O que fazer:** calcular os totais solicitado, reembolsável e não reembolsável.

**Critério de aceite:** teste dos totais passa.

---

## T-012 — Criar CLI e saída JSON

**Atende:** interface fixa do desafio e seção 13 da spec.

**O que fazer:** permitir execução com `calcular --input ... --output ...` e gravar o resultado em JSON.

**Critério de aceite:** teste de ponta a ponta gera o arquivo de saída corretamente.

---

## T-013 — Validar o exemplo oficial e revisar documentação

**Atende:** critérios de aceite gerais.

**O que fazer:** executar o sistema com o exemplo fornecido, revisar README e conferir rastreabilidade.

**Critério de aceite:** todos os testes passam e o projeto pode ser executado seguindo o README.
