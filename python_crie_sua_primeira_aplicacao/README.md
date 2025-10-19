## Organização de pastas e padrão MVC

Este projeto foi organizado seguindo o padrão MVC (Model–View–Controller) para separar responsabilidades e facilitar manutenção e evolução.

## Organização de pastas

```
PythonCrieSuaprimeiraAplicacao/
  app.py                       # ponto de entrada (inicia o menu da CLI)
  mvc/
    controllers/               # Controller: orquestra fluxo e entradas do usuário
      menu_controller.py       # loop do menu e ações da CLI
    models/                    # Model: regras de dados e persistência
      repository.py            # operações de domínio (listar, adicionar, buscar, alternar)
      storage.py               # persistência em JSON (load/save e defaults)
    views/                     # View: exibição no console (sem regra de negócio)
      console_view.py          # utilitários de console (limpar tela, subtítulo)
      menu_view.py             # impressão do título, opções e listagem
  data/
    restaurants.json           # arquivo de dados (criado/atualizado automaticamente)
  exercicios/                  # exercícios do curso (não fazem parte do app)
```

## Como o MVC funciona aqui

- **Model (mvc/models/)**
  - `repository.py`: expõe as operações de domínio sobre restaurantes (ex.: `listar`, `adicionar`, `buscar_por_nome`, `alternar_status`). Não cuida de interface com o usuário.
  - `storage.py`: abstrai a persistência (leitura/escrita em `data/restaurants.json`) e mantém dados iniciais padrão.

- **View (mvc/views/)**
  - `menu_view.py`: imprime o título, o menu e a listagem formatada. Exibe mensagens de sucesso/erro. Não acessa dados diretamente.
  - `console_view.py`: utilidades de exibição, como `limpar_tela` e `exibir_subtitulo`.

- **Controller (mvc/controllers/)**
  - `menu_controller.py`: executa o loop do menu, lê entradas (`input`), decide a ação, chama o Model e delega a exibição para a View.

## Fluxo (em alto nível)

1. `app.py` define e chama `run()` 
2. O Controller mostra o menu (View) e lê a opção do usuário.
3. Para cada ação, o Controller chama funções do Model (`repository.py`).
4. O Model obtém/salva dados via `storage.py` (JSON em `data/restaurants.json`).
5. O Controller usa a View para imprimir resultados no console.

## Benefícios desta organização

- **Coesão por camada**: cada parte faz apenas o que lhe compete.
- **Baixo acoplamento**: trocar JSON por banco real afeta só `storage.py` (e o `repository.py` se necessário), sem mexer em Controller/View.
- **Testabilidade**: Model e Controller podem ser testados sem a View.


