# SisCurso

Sistema de gerenciamento de cursos desenvolvido em Django.

# Integrantes
- João Pedro Silva Brito Teixeira
- Gustavo Roberto Souza Bernardo
- Maria Fernanda Barbosa Firmo

## Como rodar o projeto

### 1. Clone o repositório
```bash
git clone [url-do-repositorio]
cd siscurso
```

### 2. Crie e ative o ambiente virtual
```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar no Windows
.venv\Scripts\activate

# Ativar no Linux/Mac
source .venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados
```bash
python manage.py migrate
```

### 5. Crie um superusuário (opcional)
```bash
python manage.py createsuperuser
```

### 6. Execute o servidor
```bash
python manage.py runserver
```
