# AI Usage — Governança e Transparência

## Ferramenta utilizada

Foi utilizada a ferramenta Kiro (assistente de IA da AWS), como apoio durante o desenvolvimento do projeto.

## Como a IA foi utilizada

A IA foi utilizada como ferramenta de apoio para:

- auxiliar na definição do domínio do projeto;
- estruturar as regras de negócio;
- auxiliar na criação da documentação (PRD.md, README.md, AGENTS.md);
- sugerir estruturas de código e testes;
- auxiliar na identificação de cenários de teste (EP, BVA e Error Guessing);
- auxiliar na análise de cobertura de código.

## Auditoria e validação

Todas as partes em que houve auxílio da IA — como a definição do `PRD.md`, os testes gerados e até mesmo a escrita deste arquivo e do `README.md` — foram revisadas e ajustadas conforme a necessidade antes de serem aceitas.

A validação da suíte de testes foi realizada executando localmente. Foi verificado se os testes que deveriam passar realmente passaram e se os cenários inválidos foram corretamente rejeitados pelo sistema, conforme esperado.
