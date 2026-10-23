# Projeto de Álgebra Linear

Solução do torneio de Álgebra Linear da disciplina CIN0138: estimar os valores
ocultos de um lote de matrizes.

## Estrutura

```text
.
├── src/
│   ├── __init__.py
│   └── principal.py          # arquivo compatível com o avaliador
├── tests/
│   └── test_principal.py      # testes locais do contrato da função
├── docs/
│   └── relatorio.md           # relatório curto exigido na entrega
├── dados/
│   └── README.md              # instruções para dados do avaliador
└── README.md
```

O arquivo `src/principal.py` contém uma única função pública:

```python
def principal(observada, mascara):
    ...
```

As funções auxiliares devem permanecer dentro de `principal`, conforme as
regras. O baseline atual preenche posições ocultas com a média dos valores
conhecidos; ele serve apenas como ponto de partida para o desenvolvimento.

## Desenvolvimento em dupla

1. Cada integrante cria uma branch a partir de `main`:
   `git switch -c feat/nome-da-melhoria`.
2. Antes de alterar o algoritmo, a dupla registra a hipótese e o resultado no
   `docs/relatorio.md`.
3. Toda alteração em `src/principal.py` deve passar pelos testes locais:
   `python -m unittest discover -s tests -v`.
4. A dupla deve comparar as estratégias no avaliador local usando as 10
   matrizes públicas, registrando o NRMSE e o tempo de execução.
5. Fazer pull request para `main` e revisar o código juntos. A branch de entrega
   deve conter somente a versão final validada.

## Entrega

O ZIP deve conter o arquivo `principal.py` e o relatório final. Copie
`src/principal.py` para a raiz do ZIP e converta `docs/relatorio.md` para o
formato solicitado pelo professor, nomeando o arquivo como
`Grupo<numero>.zip`. Não inclua `.venv`, banco local, logs, caches ou o lote
privado do avaliador.

O avaliador possui ambiente próprio. Para testar a interface local, siga o
`README.md` do pacote `pacote_equipe` fornecido pelos monitores e execute
`docker compose up` nessa pasta, sem versionar o pacote no repositório.
