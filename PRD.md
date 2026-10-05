# PRD — Sistema de Reserva de Hotel

## 1. Visão geral

O Sistema de Reserva de Hotel tem como objetivo validar os dados de uma reserva e calcular o valor total da hospedagem de acordo com a quantidade de hóspedes, número de noites, tipo de quarto e aplicação de cupons promocionais.

O sistema será desenvolvido em Python e terá como foco a implementação de regras de negócio determinísticas que possam ser verificadas por meio de testes unitários.

---

## 2. Objetivo

Implementar uma função capaz de validar uma reserva de hotel e calcular seu valor total, aplicando as regras de negócio definidas neste documento.

O sistema deve rejeitar entradas inválidas por meio de exceções e retornar o valor calculado para reservas válidas.

---

## 3. Dados de entrada

Uma reserva possui os seguintes campos:

- **adultos** *(int)* — quantidade de adultos na reserva.
- **criancas** *(int)* — quantidade de crianças.
- **noites** *(int)* — quantidade de noites da hospedagem.
- **tipo_quarto** *(str)* — tipo de quarto escolhido.
- **cupom** *(str ou None)* — código promocional opcional.

---

## 4. Tipos de quarto

O sistema disponibiliza três tipos de quarto:

- **standard** — R$ 200,00 por noite.
- **luxo** — R$ 350,00 por noite.
- **suite** — R$ 500,00 por noite.

O tipo de quarto informado deve corresponder a uma das opções disponíveis.

---

# 5. Regras de negócio

## RN01 — Quantidade mínima de adultos

Uma reserva deve possuir pelo menos 1 adulto.

- Se `adultos < 1`, a reserva deve ser rejeitada.
- Se `adultos >= 1`, a quantidade de adultos é considerada válida.

---

## RN02 — Quantidade de crianças

A reserva pode possuir de 0 a 4 crianças.

- `0` crianças é válido.
- Valores entre `1` e `4` são válidos.
- Valores maiores que `4` são inválidos.
- Valores negativos são inválidos.

---

## RN03 — Quantidade de noites

A hospedagem deve possuir entre 1 e 30 noites.

- `0` noites é inválido.
- `1` noite é válido.
- Valores entre `1` e `30` são válidos.
- `30` noites é válido.
- Valores superiores a `30` são inválidos.

---

## RN04 — Tipo de quarto

O tipo de quarto deve ser um dos valores disponíveis:

- `standard`
- `luxo`
- `suite`

Qualquer outro valor deve ser rejeitado.

---

## RN05 — Valor adicional por criança

Cada criança adiciona R$ 50,00 ao valor da diária.

O valor da diária é calculado da seguinte forma:

`valor da diária = valor do quarto + (quantidade de crianças × R$ 50,00)`

O valor total da hospedagem é:

`valor total = valor da diária × quantidade de noites`

### Exemplo

Para:

- 2 adultos;
- 1 criança;
- 3 noites;
- quarto `standard`;

o cálculo será:

`(R$ 200,00 + R$ 50,00) × 3 = R$ 750,00`

---

## RN06 — Cupons promocionais

O sistema possui dois cupons promocionais:

- **HOTEL10** — 10% de desconto.
- **HOTEL20** — 20% de desconto.

Quando nenhum cupom for informado, o valor total permanece sem desconto.

Quando um cupom válido for informado, o desconto correspondente deve ser aplicado ao valor total.

Um cupom diferente de `HOTEL10` ou `HOTEL20` deve ser rejeitado.

---

# 6. Validações e comportamento esperado

O sistema deve validar os dados antes de realizar o cálculo.

Quando uma entrada violar uma regra de negócio, a função deve lançar uma exceção apropriada.

Quando todos os dados forem válidos, a função deve retornar o valor total da reserva.

---

# 7. Critérios de aceitação

Uma implementação será considerada correta quando:

1. Rejeitar reservas sem adultos.
2. Aceitar reservas com pelo menos um adulto.
3. Aceitar de 0 a 4 crianças.
4. Rejeitar quantidades negativas de crianças.
5. Rejeitar mais de 4 crianças.
6. Aceitar reservas de 1 a 30 noites.
7. Rejeitar reservas com 0 ou mais de 30 noites.
8. Aceitar os tipos de quarto `standard`, `luxo` e `suite`.
9. Rejeitar tipos de quarto inexistentes.
10. Calcular corretamente o adicional por criança.
11. Calcular corretamente o valor total considerando a quantidade de noites.
12. Aplicar corretamente o cupom `HOTEL10`.
13. Aplicar corretamente o cupom `HOTEL20`.
14. Calcular corretamente uma reserva sem cupom.
15. Rejeitar cupons desconhecidos.
16. Tratar entradas inválidas de forma defensiva por meio de exceções.

---

# 8. Estratégia de testes

A implementação será acompanhada por uma suíte de testes unitários utilizando Pytest.

Serão utilizadas as seguintes técnicas:

- Particionamento de Equivalência (EP);
- Análise do Valor Limite (BVA);
- Error Guessing;
- Testes parametrizados com `@pytest.mark.parametrize`;
- Testes organizados no padrão AAA (Arrange, Act, Assert);
- Cobertura de linhas e ramificações utilizando `pytest-cov`.

O objetivo é atingir 100% de cobertura de código e 100% de cobertura de ramificações no módulo responsável pelas regras de negócio.
