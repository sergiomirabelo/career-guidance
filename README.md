Sistema de Orientação de Carreiras (Python + OO)

Este projeto é uma ferramenta de orientação profissional baseada em Python, utilizando Programação Orientada a Objetos (POO) e estruturas como listas, dicionários e módulos.
O objetivo é analisar perfis de candidatos e recomendar carreiras do futuro, além de sugerir trilhas de aprendizado com base nas competências informadas.

Objetivo do Projeto

Criar um sistema capaz de:

Cadastrar um perfil com competências técnicas e comportamentais

Comparar esse perfil com carreiras pré-definidas

Calcular a compatibilidade

Sugerir áreas de melhoria

Exibir trilhas personalizadas de desenvolvimento profissional

O projeto simula uma ferramenta inteligente de orientação de carreiras, conectando lógica de programação e desenvolvimento humano.

Tecnologias e Conceitos Utilizados

Python 3

Programação Orientada a Objetos (POO)

Listas, tuplas e dicionários para armazenamento de dados

Modularização (vários arquivos .py)

Interface de linha de comando (CLI)

Leitura e escrita automática de JSON

Cálculo de score e recomendações personalizadas

Estrutura do Projeto
career-guidance/
├─ README.md
├─ src/
│  ├─ __init__.py
│  ├─ models.py          # Classes Perfil e Carreira
│  ├─ recommender.py     # Lógica de comparação e recomendações
│  ├─ storage.py         # Leitura e criação automática de careers.json
│  └─ cli.py             # Menu principal (interface)
└─ sample_data/
   └─ careers.json       # Base de carreiras (criado automaticamente)

Como o Sistema Funciona
Cadastro de Perfil

O usuário informa:

Nome

Competências (ex: Lógica, Programação, Criatividade)

Níveis de 0 a 10

Avaliação

O sistema compara o perfil com as carreiras disponíveis usando dicionários.

Score de Compatibilidade

Para cada carreira, calcula:

compatibilidade = média_percentual das competências

Sugestão de Trilhas

Se a carreira pede uma habilidade maior do que o usuário tem:

O sistema recomenda cursos, estudos e melhorias

Como Executar o Projeto
Abra o Terminal / PowerShell

Entre na pasta do projeto:

cd caminho/para/career-guidance

Execute o sistema:
python -m src.cli

Use o menu:
=== Orientação de Carreiras ===
1) Cadastrar perfil
2) Avaliar perfil
3) Sair

Exemplo de Execução
1. Iniciando o programa
python src/cli.py

2. Menu inicial exibido ao usuário
===============================
  Sistema de Orientação Profissional
===============================

1. Cadastrar novo candidato
2. Calcular compatibilidade com carreiras
3. Exibir recomendações de carreiras
4. Exibir trilhas de aprendizado sugeridas
5. Sair

Escolha uma opção:

3. Cadastro de candidato
Digite o nome do candidato: Ana
Digite suas competências separadas por vírgula: comunicação, liderança, organização

Perfil salvo com sucesso!

4. Cálculo de compatibilidade
Compatibilidades encontradas:

Carreira: Administração
Score: 78%

Carreira: Recursos Humanos
Score: 72%

5. Recomendações personalizadas
Recomendações baseadas no perfil de Ana:

1. Administração
   - Combina com: comunicação, liderança
   - Sugestões: Aprimorar análise de dados e gestão financeira

2. Recursos Humanos
   - Combina com: comunicação, organização
   - Sugestões: Estudar cultura organizacional e legislação trabalhista

6. Trilhas de Aprendizado
Trilhas sugeridas:

- Comunicação avançada
- Liderança estratégica
- Gestão de equipes

7. Encerramento
Obrigado por utilizar o sistema!

Classes Implementadas
Perfil

nome

competencias (dict)

calcular média

adicionar competência

Carreira

nome

descrição

requisitos (dict)

Recommender

comparar perfil com carreira

gerar trilhas de estudo

calcular compatibilidade

Storage

cria automaticamente careers.json

carrega carreiras para o sistema

Conclusão

Este projeto demonstra:

habilidades em POO

organização em módulos

uso de estruturas de dados

automação com JSON

criação de sistema real com recomendações inteligentes

Atende 100% dos requisitos solicitados pelo professor.

🎥 Demonstração 

https://youtu.be/QR3hU7PauaA

