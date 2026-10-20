# DECISIONS — Motor de Reembolso

Este arquivo registra mudanças feitas na spec durante o projeto.

## D-001 — Definição inicial das ambiguidades

**Data:** preencher na data do commit.

**O que mudou:** a política original foi transformada em regras objetivas e testáveis.

**Por quê:** a política possuía pontos ambíguos que poderiam gerar comportamentos diferentes na implementação.

**Principais decisões:**

- limites de alimentação e transporte são diários e acumulados por categoria;
- valores acima do limite são reembolsados parcialmente;
- R$ 100,00 exatos não exigem nota fiscal;
- a regra de viagem ficou fora desta versão por falta de informação na entrada;
- duplicatas mantêm a primeira ocorrência e recusam as seguintes;
- despesas do mesmo dia consomem o limite na ordem da entrada;
- cada registro de hospedagem representa uma diária;
- despesas fora do período permanecem visíveis como não reembolsáveis;
- valores iguais ou menores que zero são inválidos.

**O que quebrou:** nada, pois esta decisão foi tomada antes da implementação.

**Tasks afetadas:** T-003 até T-012.

---

## Modelo para próximas mudanças

### D-XXX — Título da decisão

**Data:**

**O que mudou:**

**Por quê:**

**O que quebrou:**

**Tasks afetadas:**
