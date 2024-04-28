<img src="https://images.sympla.com.br/62f50b75e7404.png" alt="Amicci Logo"></img>

# Amicci - Teste prático para BackEnd Developer.

## Acesse o site!

https://teste-backend-amicci.fly.dev/

## Techs

- [x] Django;
- [x] Python 3.10 (3.12 em Produção);
- [x] Django Rest Framework;
- [x] PostgreSQL;
- [x] DJ Rest Auth;
- [x] DRF YASG;
- [x] Docker;
- [x] Unittest.

## Executando

1. Copie o conteúdo de `.env.example` para `.env`;
2. Instale as dependências com `poetry install`;
3. Execute o projeto com `docker compose up -d`;
4. Acesse `http://localhost:8000/swagger/`.

## Publicação

1. Instale a CLI do [Fly.io](https://fly.io/docs/hands-on/install-flyctl/);
2. Execute `fly deploy`.
3. Configure a secret DATABASE_URL com o endereço do banco de dados.

## Endpoints disponíveis

Consulte mais detalhes em https://teste-backend-amicci.fly.dev/swagger/.

* POST `/auth/login/`: Realiza o login de um usuário via Cookie;
* POST `/auth/logout/`: Realiza o logout do usuário atual;
* POST `/auth/register/`: Cadastra um novo usuário;
* POST `/auth/user/`: Retorna os dados do usuário atual;
* GET `/briefing/`: Lista todos os Briefings;
* GET `/briefing/{id}`: Busca o Briefing pelo ID;
* PUT `/briefing/{id}`: Atualiza um Briefing pelo ID;
* POST `/briefings/`: Cria um novo Briefing;
* GET `/vendor/`: Lista todos os Fornecedor;
* GET `/vendor/{id}`: Busca o Fornecedor pelo ID;
* PUT `/vendor/{id}`: Atualiza um Fornecedor pelo ID;
* POST `/vendors/`: Cria um novo Fornecedor;
* GET `/retailer/`: Lista todos os Varejista;
* GET `/retailer/{id}`: Busca o Varejista pelo ID;
* PUT `/retailer/{id}`: Atualiza um Varejista pelo ID;
* POST `/retailers/`: Cria um novo Varejista;
* GET `/category/`: Lista todos as Categorias;
* GET `/category/{id}`: Busca a Categoria pelo ID;
* PUT `/category/{id}`: Atualiza uma Categoria pelo ID;
* POST `/categories/`: Cria uma nova Categoria.

## Instruções

* Utilizar Django/Python como linguagem e framework primários;
* Utilizar a biblioteca django-rest-framework;
* A aplicação deverá ser disponibilizada em container;
* Deverá persistir os dados;
* No setup, os dados de Categorias devem ser populados caso ainda não tenham sido;
* Readme deverá conter instruções de como executar o container e os endpoints disponíveis;
* Disponibilizar o projeto em um repositório privado;
* Um documento descrevendo a API foi disponibilizado no anexo (desc_api.yaml). Os endpoints devem seguir esse documento.
* Categorias:
    - Novo Produto
    - Troca de Fornecedor
    - Reformulação de Produto

## Contatos

- Autor - [João Prado](https://www.linkedin.com/in/jppradoleal/)
- Website - [https://jprado.dev/](https://jprado.dev/)
