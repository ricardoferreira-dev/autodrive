# 🚗 RF AutoDrive - Sistema de Gerenciamento de Carros

Projeto desenvolvido em Django para cadastro e gestão de veículos com interface moderna dark theme.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎯 Funcionalidades

- ✅ Cadastro completo de carros com fotos
- ✅ Sistema de autenticação de usuários
- ✅ Busca e filtros avançados
- ✅ Interface moderna com tema dark (preto/laranja/amarelo)
- ✅ Design 100% responsivo
- ✅ CRUD completo (Create, Read, Update, Delete)
- ✅ Formatação de valores em Real (R$)

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3.x, Django 5.x
- **Database:** PostgreSQL
- **Frontend:** HTML5, CSS3, JavaScript
- **Fontes:** Google Fonts (Poppins)
- **Ícones:** Font Awesome 6
- **Segurança:** python-decouple para variáveis de ambiente

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.8+
- PostgreSQL
- Git

### 1. Clone o repositório
```bash
git clone https://github.com/ricardoferreira-dev/autodrive.git
cd autodrive
```

### 2. Crie um ambiente virtual
```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o .env e adicione suas configurações
# Gere uma SECRET_KEY com:
python manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
```

Preencha o `.env`:
```env
SECRET_KEY=sua-chave-gerada-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=seu_banco
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
```

### 5. Crie o banco de dados no PostgreSQL
```sql
CREATE DATABASE autodrive_db;
```

### 6. Execute as migrações
```bash
python manage.py migrate
```

### 7. Crie um superusuário
```bash
python manage.py createsuperuser
```

### 8. Execute o servidor
```bash
python manage.py runserver
```

Acesse: **http://127.0.0.1:8000/**

## 📸 Screenshots

### 🏠 Tela Inicial
![Home](https://i.imgur.com/lAMuZ95.png)

### 📋 Listagem de Carros
![Car_List](https://i.imgur.com/JHWHPm2.png)

### 🚗 Detalhes do Carro
![Car_Detail](https://i.imgur.com/h95Y2g9.png)

## 🤖 Integração com IA

O projeto utiliza a **Gemini API (Google AI)** para gerar descrições automáticas de carros quando o usuário não preenche a descrição manualmente.

### Configuração da API:

1. Obtenha uma API Key gratuita em: https://makersuite.google.com/app/apikey
2. Adicione no arquivo `.env`:
```env
GEMINI_API_KEY=sua-chave-aqui
```

### Como funciona:

Quando um carro é cadastrado sem descrição, o sistema:
1. Captura marca, modelo e ano do veículo
2. Envia para a Gemini API
3. Recebe uma descrição profissional gerada por IA
4. Salva automaticamente no banco de dados
```

## 📂 Estrutura do Projeto
```
autodrive/
├── cars/                  # App principal
│   ├── models.py         # Modelos do banco
│   ├── views.py          # Lógica das views
│   ├── urls.py           # Rotas
│   └── templates/        # Templates HTML
├── app/                  # Configurações Django
│   ├── settings.py       # Configurações do projeto
│   └── urls.py           # URLs principais
├── static/               # Arquivos estáticos
├── media/                # Uploads de imagens
├── .env                  # Variáveis de ambiente (não versionado)
├── .env.example          # Exemplo de variáveis
├── .gitignore            # Arquivos ignorados pelo Git
├── manage.py             # Comando Django
├── requirements.txt      # Dependências Python
└── README.md             # Documentação
```

## 🎨 Tema Visual

- **Cores principais:** Preto (#0a0a0a), Laranja (#ff6b35), Amarelo (#ffd700)
- **Fonte:** Poppins (Google Fonts)
- **Estilo:** Dark theme moderno com efeitos glow

## 📚 Sobre o Projeto

Este projeto foi desenvolvido como parte do curso @PycodeBR, onde aprendi os fundamentos de Django e desenvolvimento web. 

**Stack de Desenvolvimento:**
- 🐍 **Backend:** Desenvolvido 100% por mim - Django, PostgreSQL, autenticação, CRUD completo
- 🎨 **Frontend:** Interface criada com auxílio de IA (Claude), permitindo foco na lógica de negócio


### 🎨 Personalizações e Melhorias Implementadas

O projeto foi significativamente modificado e aprimorado com:

- **Design Completo:** Interface dark theme moderna com paleta personalizada (preto/laranja/amarelo)
- **Landing Page:** Hero section com animações, estatísticas e call-to-action
- **UX/UI:** Cards responsivos com efeitos hover, transições suaves e glassmorphism
- **Segurança:** Implementação de variáveis de ambiente com python-decouple
- **Formatação:** Sistema de formatação de valores em Real brasileiro (R$)
- **Templates:** Todos os templates redesenhados do zero com tema consistente
- **Funcionalidades:** Sistema completo de CRUD com validações

### 🎯 Objetivo

Demonstrar habilidades práticas em:
- Django framework e ORM
- PostgreSQL e modelagem de dados
- Design responsivo e acessível
- Boas práticas de segurança
- Controle de versão com Git

## 📝 Aprendizados

Este projeto foi desenvolvido para aplicar conceitos de:
- Django ORM e relacionamentos de banco de dados
- Autenticação e autorização
- Upload de arquivos
- Variáveis de ambiente e segurança
- Design responsivo
- Git e versionamento

## 👨‍💻 Autor

**Ricardo Ferreira**

- GitHub: [@ricardoferreira-dev](https://github.com/ricardoferreira-dev)
- LinkedIn: [Ricardo Ferreira](https://linkedin.com/in/ricardferreiradev)
- Email: ricardferreira.dev@gmail.com

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

**Desenvolvido para fins educacionais e de portfólio.**
---

⭐ Se você gostou do projeto, deixe uma estrela! ⭐