# Sistema de Reserva de Hotel

Sistema de validação e cálculo de reservas de hotel, desenvolvido em Python com foco em regras de negócio determinísticas e cobertura de testes unitários.

## Domínio

O sistema valida os dados de uma reserva (adultos, crianças, noites, tipo de quarto e cupom promocional) e calcula o valor total da hospedagem, rejeitando entradas inválidas por meio de exceções.

As regras de negócio estão documentadas em detalhes no [PRD.md](PRD.md).

## Requisitos

- [uv](https://docs.astral.sh/uv/) (gerenciador de projetos Python)
- Python 3.12+

## Instalação

Clone o repositório e instale as dependências de desenvolvimento:

```bash
git clone <url-do-repositorio>
cd sistema-reserva-hotel
uv sync
```

## Execução dos testes

### Rodar todos os testes com saída detalhada

```bash
uv run pytest -v
```

### Rodar com cobertura de linhas e ramificações

```bash
uv run pytest --cov=app --cov-branch --cov-report=term-missing
```

A suíte deve atingir **100% de cobertura** de linhas e ramificações no módulo `app/reserva.py`.

## Estrutura do projeto

```
sistema-reserva-hotel/
├── app/
│   ├── __init__.py
│   └── reserva.py        # Regras de negócio (SUT)
├── tests/
│   └── test_reserva.py   # Suíte de testes unitários
├── AGENTS.md             # Regras de contexto para IA
├── AI_USAGE.md           # Relatório de transparência de uso de IA
├── PRD.md                # Especificação das regras de negócio
├── pyproject.toml        # Configuração do projeto (uv)
└── README.md
```

## Técnicas de teste aplicadas

- **Particionamento de Equivalência (EP):** grupos de valores válidos e inválidos para cada campo.
- **Análise do Valor Limite (BVA):** valores nos limites exatos das regras (ex: 0, 1, 4, 5, 30, 31 noites/crianças).
- **Error Guessing:** entradas inesperadas como strings no lugar de inteiros, cupons com case errado, objetos de tipo incorreto.
- **Testes parametrizados:** `@pytest.mark.parametrize` para cenários semelhantes.
- **Padrão AAA:** todos os testes organizam o código em Arrange, Act e Assert.
- **Marcação:** todos os testes são marcados com `@pytest.mark.unit`.

## Governança de IA

O uso de inteligência artificial no desenvolvimento deste projeto está documentado em [AI_USAGE.md](AI_USAGE.md).
