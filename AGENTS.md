# Regras de contexto do projeto

## Objetivo

Este projeto implementa um sistema de reserva de hotel em Python, com foco em regras de negócio determinísticas, testes unitários e cobertura de código.

## Tecnologias

- Python 3.12+
- Pytest
- pytest-cov
- uv

## Regras de desenvolvimento

1. O código deve utilizar Type Hints sempre que aplicável.
2. As regras de negócio devem permanecer determinísticas e independentes de serviços externos.
3. Entradas inválidas devem ser tratadas de forma defensiva.
4. As regras de negócio devem seguir o que está especificado no `PRD.md`.
5. Não adicionar funcionalidades que não estejam relacionadas ao escopo definido no `PRD.md` sem justificativa.
6. O código deve priorizar simplicidade, legibilidade e manutenção.
7. Os testes devem utilizar Pytest.
8. Os testes devem seguir o padrão AAA:
   - Arrange
   - Act
   - Assert
9. Sempre que houver cenários semelhantes, utilizar `@pytest.mark.parametrize`.
10. Os testes devem contemplar Particionamento de Equivalência (EP), Análise do Valor Limite (BVA) e Error Guessing.
11. O código de produção não deve ser alterado apenas para facilitar um teste.
12. Alterações realizadas com auxílio de IA devem ser revisadas e validadas manualmente.

## Testes e cobertura

A suíte deve ser executada utilizando:

```text
uv run pytest -v