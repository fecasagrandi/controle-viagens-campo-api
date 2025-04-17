# Controle de Viagens - API REST

API para gerenciamento de usuários, destinos, transportes, categorias e viagens.

## Sumário

- [Tecnologias](#tecnologias)
- [Como rodar o projeto](#como-rodar-o-projeto)
- [Autenticação](#autenticação)
- [Documentação Swagger](#documentação-swagger)
- [Endpoints da API](#endpoints-da-api)
  - [Usuários](#usuários)
  - [Destinos](#destinos)
  - [Transportes](#transportes)
  - [Categorias](#categorias)
  - [Viagens](#viagens)

---

## Tecnologias

- Python 3.12+
- Django 4.x
- Django REST Framework
- drf-yasg (Swagger)
- SQLite (default)

---

## Como rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/fecasagrandi/controle-viagens-campo-api.git
   cd controle-viagens-campo-api/viagens_project
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplique as migrações:**
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário (opcional, para acessar o admin):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Rode o servidor:**
   ```bash
   python manage.py runserver
   ```

---

## Autenticação

- As rotas da API exigem autenticação por padrão (`IsAuthenticated`).
- Utilize o endpoint `/admin/` para criar usuários ou implemente um endpoint de login/token conforme sua necessidade.

---

## Documentação Swagger

Acesse a documentação interativa em:  
[http://localhost:8000/swagger/](http://localhost:8000/swagger/)

---

## Endpoints da API

Todos os endpoints estão sob o prefixo `/api/`.

### Usuários

| Método | Endpoint             | Descrição                  |
|--------|----------------------|----------------------------|
| GET    | /api/usuarios/       | Lista todos os usuários    |
| POST   | /api/usuarios/       | Cria um novo usuário       |
| GET    | /api/usuarios/{id}/  | Detalha um usuário         |
| PUT    | /api/usuarios/{id}/  | Atualiza um usuário        |
| DELETE | /api/usuarios/{id}/  | Remove um usuário          |

#### Exemplo de requisição POST
```json
POST /api/usuarios/
{
  "nome": "Felipe",
  "email": "felipe@email.com"
}
```

---

### Destinos

| Método | Endpoint             | Descrição                  |
|--------|----------------------|----------------------------|
| GET    | /api/destinos/       | Lista todos os destinos    |
| POST   | /api/destinos/       | Cria um novo destino       |
| GET    | /api/destinos/{id}/  | Detalha um destino         |
| PUT    | /api/destinos/{id}/  | Atualiza um destino        |
| DELETE | /api/destinos/{id}/  | Remove um destino          |

---

### Transportes

| Método | Endpoint                 | Descrição                     |
|--------|--------------------------|-------------------------------|
| GET    | /api/transportes/        | Lista todos os transportes    |
| POST   | /api/transportes/        | Cria um novo transporte       |
| GET    | /api/transportes/{id}/   | Detalha um transporte         |
| PUT    | /api/transportes/{id}/   | Atualiza um transporte        |
| DELETE | /api/transportes/{id}/   | Remove um transporte          |

---

### Categorias

| Método | Endpoint                | Descrição                    |
|--------|-------------------------|------------------------------|
| GET    | /api/categorias/        | Lista todas as categorias    |
| POST   | /api/categorias/        | Cria uma nova categoria      |
| GET    | /api/categorias/{id}/   | Detalha uma categoria        |
| PUT    | /api/categorias/{id}/   | Atualiza uma categoria       |
| DELETE | /api/categorias/{id}/   | Remove uma categoria         |

---

### Viagens

| Método | Endpoint             | Descrição                  |
|--------|----------------------|----------------------------|
| GET    | /api/viagens/        | Lista todas as viagens     |
| POST   | /api/viagens/        | Cria uma nova viagem       |
| GET    | /api/viagens/{id}/   | Detalha uma viagem         |
| PUT    | /api/viagens/{id}/   | Atualiza uma viagem        |
| DELETE | /api/viagens/{id}/   | Remove uma viagem          |

---

## Observações

- Para autenticação, utilize o painel admin ou implemente JWT/Token Authentication.
- Todos os endpoints e exemplos podem ser testados na interface Swagger.
- Para dúvidas, sugestões ou problemas, abra uma issue no repositório.
