# 🎲 RPGManager

Sistema web para gerenciamento de personagens de RPG desenvolvido com Django.

## 📌 Descrição

O RPGManager é uma aplicação web criada para facilitar o gerenciamento de fichas de personagens de RPG. O sistema permite que usuários criem contas, façam login e gerenciem seus próprios personagens de forma organizada e segura.

Cada usuário possui acesso apenas às suas próprias fichas, enquanto administradores possuem controle total através do painel administrativo do Django.

O projeto está hospedado na nuvem utilizando Railway e PostgreSQL.

---

## 🚀 Funcionalidades

* Cadastro de usuários
* Login e logout
* Criação de fichas de personagens
* Edição de fichas
* Exclusão de fichas
* Upload de imagem para personagens
* Controle de permissões por usuário
* Painel administrativo para administradores
* Interface temática inspirada em RPG
* Armazenamento persistente em PostgreSQL
* Hospedagem em produção utilizando Railway

---

## 🛠️ Tecnologias Utilizadas

### Backend

* Python 3
* Django 6
* PostgreSQL
* Gunicorn
* WhiteNoise

### Frontend

* HTML5
* CSS3

### Hospedagem

* Railway
* PostgreSQL Railway

---

## 🌐 Acesso Online

O sistema está disponível em:

https://rpgmanager-production.up.railway.app

---

## 📦 Instalação Local

### Clonar o repositório

```bash
git clone https://github.com/Vyamaral/RPGManager.git
cd RPGManager
```

### Criar ambiente virtual

```bash
python -m venv venv
```

### Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar migrações

```bash
python manage.py migrate
```

### Criar administrador (opcional)

```bash
python manage.py createsuperuser
```

### Iniciar servidor

```bash
python manage.py runserver
```

Acesse:

```text
http://127.0.0.1:8000/
```

---

## 📁 Estrutura do Projeto

```text
RPGManager/
│
├── config/
├── fichas/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   └── forms.py
│
├── media/
├── staticfiles/
├── manage.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🔒 Controle de Acesso

### Usuário comum

* Criar personagens
* Editar seus próprios personagens
* Excluir seus próprios personagens

### Administrador

* Gerenciar todos os personagens
* Acessar o painel administrativo
* Gerenciar usuários do sistema

---

## 📈 Melhorias Futuras

* Sistema de campanhas
* Sistema de sessões
* Inventário para personagens
* Exportação de fichas em PDF
* Perfil de usuário
* Recuperação de senha por e-mail
* API REST
* Interface responsiva para dispositivos móveis

---

## 👨‍💻 Autor

Desenvolvido por **Vyamaral**

GitHub:
https://github.com/Vyamaral

---

## 📄 Licença

Este projeto está sob a licença MIT.
