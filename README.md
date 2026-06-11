RPG Manager - Sistema de Fichas de RPG

Este é um projeto web desenvolvido em Django, com o objetivo de permitir que jogadores criem, visualizem, editem e excluam fichas de personagens de RPG de forma simples e organizada.

FUNCIONALIDADES

- Criar fichas de personagens de RPG
- Armazenar informações como:
  - Nome do personagem
  - Nome do jogador
  - Vida (HP)
  - Classe
  - Outras características do personagem
- Listar todos os personagens cadastrados
- Editar fichas existentes
- Excluir personagens
- Sistema de login para controle de usuários

TECNOLOGIAS UTILIZADAS

- Python
- Django
- HTML5
- CSS3
- JavaScript (básico)
- PostgreSQL (ou SQLite em desenvolvimento)

ESTRUTURA DO PROJETO

RPGManager/
|
├── fichas/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   └── urls.py
|
├── config/
│   ├── settings.py
│   ├── urls.py
|
├── manage.py
└── db.sqlite3

COMO EXECUTAR O PROJETO

1. Clonar o repositório:
git clone https://github.com/Vyamaral/RPGManager
cd rpg-manager

2. Criar ambiente virtual:
python -m venv venv

3. Ativar ambiente virtual:

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

4. Instalar dependências:
pip install -r requirements.txt

5. Rodar migrações:
python manage.py migrate

6. Criar superusuário (opcional):
python manage.py createsuperuser

7. Iniciar servidor:
python manage.py runserver

Acesse:
http://127.0.0.1:8000/

LOGIN

O sistema possui autenticação para proteger as fichas dos usuários.

OBJETIVO

Projeto acadêmico para praticar:
- Django
- CRUD
- MVC
- Banco de dados
- Autenticação

AUTORA

Evelyn Cardoso
