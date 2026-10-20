# Spec — Motor de Reembolso

## 1. Objetivo

Analisar as despesas de um colaborador em um período e informar quanto pode ser reembolsado.

Para cada despesa, o sistema deve informar:

- valor solicitado;
- valor reembolsável;
- valor não reembolsável;
- situação;
- motivo da decisão.

Também deve informar os totais do período.

## 2. Categorias aceitas

São reembolsáveis somente:

- alimentação;
- transporte urbano;
- hospedagem.

Categorias diferentes dessas não são reembolsáveis.

## 3. Limites

### Alimentação

Limite de R$ 60,00 por dia.

Se houver mais de uma despesa de alimentação no mesmo dia, os valores serão acumulados até o limite diário.

### Transporte urbano

Limite de R$ 80,00 por dia.

Se houver mais de uma despesa de transporte no mesmo dia, os valores serão acumulados até o limite diário.

### Hospedagem

Limite de R$ 250,00 por diária.

Cada registro de hospedagem será tratado como uma diária.

## 4. Despesas acima do limite

Quando o valor ultrapassar o limite aplicável, o sistema deve reembolsar somente o valor permitido.

O excedente não será reembolsado.

## 5. Nota fiscal

Nota fiscal é obrigatória somente para despesas com valor maior que R$ 100,00.

Uma despesa de exatamente R$ 100,00 não exige nota fiscal.

Se a nota for obrigatória e não estiver presente, a despesa não será reembolsada.

## 6. Colaborador em viagem

A política prevê aumento de 50% nos limites para colaboradores em viagem.

Como a entrada disponível não informa se o colaborador está em viagem, essa regra não será aplicada nesta versão.

## 7. Período de competência

Somente despesas com data dentro do período de competência serão reembolsáveis.

Despesas fora do período devem aparecer no resultado como não reembolsáveis.

## 8. Duplicatas

Uma despesa será considerada duplicada quando repetir os mesmos dados principais de outra despesa:

- data;
- categoria;
- valor;
- identificação da nota ou comprovante, quando disponível.

A primeira ocorrência será considerada válida. As seguintes serão recusadas como duplicadas.

## 9. Valores inválidos

Despesas com valor igual ou menor que zero não são reembolsáveis.

## 10. Ordem das validações

Cada despesa será analisada nesta ordem:

1. validar o valor;
2. validar o período;
3. validar a categoria;
4. verificar duplicidade;
5. verificar necessidade de nota fiscal;
6. aplicar o limite da categoria;
7. calcular o valor reembolsável.

## 11. Distribuição do limite diário

Quando houver várias despesas da mesma categoria no mesmo dia, elas serão consideradas na ordem em que aparecem na entrada.

O saldo diário disponível será consumido nessa mesma ordem.

## 12. Situações possíveis

Cada despesa deve receber uma situação:

- `reembolsada`;
- `parcialmente_reembolsada`;
- `nao_reembolsada`.

## 13. Saída esperada

A saída deve ser um JSON contendo:

- resumo do período;
- lista com o resultado individual de cada despesa.

### Resumo

Deve conter:

- `total_solicitado`;
- `total_reembolsavel`;
- `total_nao_reembolsavel`.

### Resultado por despesa

Cada item deve conter:

- referência ou identificador da despesa, quando existir na entrada;
- `valor_solicitado`;
- `valor_reembolsavel`;
- `valor_nao_reembolsavel`;
- `situacao`;
- `motivo`.

## 14. Ambiguidades resolvidas

### A01 — Limite por dia ou por despesa

**Decisão:** o limite de alimentação e transporte será aplicado ao total da categoria no dia.

**Motivo:** a política usa a expressão “por dia”.

### A02 — Despesa acima do limite

**Decisão:** reembolsar até o limite e recusar apenas o excedente.

**Motivo:** a política diz que despesas acima do limite são reembolsadas parcialmente.

### A03 — Despesa de exatamente R$ 100,00

**Decisão:** não exige nota fiscal.

**Motivo:** a política exige nota somente acima de R$ 100,00.

### A04 — Viagem

**Decisão:** não aplicar o aumento de 50% nesta versão.

**Motivo:** a entrada não informa se o colaborador está em viagem.

### A05 — Duplicatas

**Decisão:** manter a primeira ocorrência e recusar as seguintes.

**Motivo:** evita pagamento duplicado sem descartar uma despesa válida.

### A06 — Ordem entre despesas do mesmo dia

**Decisão:** consumir o limite na ordem da entrada.

**Motivo:** cria um comportamento determinístico e fácil de testar.

### A07 — Hospedagem

**Decisão:** cada registro de hospedagem representa uma diária.

**Motivo:** não há outra informação de quantidade de diárias disponível.

### A08 — Despesa fora do período

**Decisão:** retornar a despesa como não reembolsável, em vez de ignorá-la.

**Motivo:** mantém rastreabilidade sobre tudo o que foi recebido.

### A09 — Valor zero ou negativo

**Decisão:** considerar inválido e não reembolsar.

**Motivo:** não representa uma despesa válida para reembolso.

## 15. Critérios de aceite

O sistema deve:

- aplicar corretamente os limites das três categorias;
- acumular alimentação e transporte por dia;
- reembolsar parcialmente valores acima do limite;
- exigir nota fiscal somente acima de R$ 100,00;
- recusar despesa sem nota quando ela for obrigatória;
- identificar duplicatas;
- recusar categorias fora da política;
- recusar despesas fora do período;
- recusar valores iguais ou menores que zero;
- informar motivo para cada decisão;
- calcular corretamente os totais finais;
- possuir testes automatizados para esses comportamentos.

## 16. Fora de escopo

Não fazem parte desta versão:

- pagamento do reembolso;
- aprovação manual;
- integração com sistemas financeiros;
- conversão de moedas;
- leitura ou validação do conteúdo da nota fiscal;
- autenticação de usuário;
- regra de viagem enquanto essa informação não existir na entrada.
