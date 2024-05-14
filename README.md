**Olá, este é um repositório que propõe a criação de um projeto simples, abordando as principais tecnologias usadas na empresa.**

Você deve se sentir à vontade para adicionar conteúdo ao escopo do projeto. Obviamente, cumprindo as premissas exigidas! :smile:

---

## Construa um sistema de Login

Você deve criar um sistema de login que recebe 2 credenciais: email e senha. Valide as informações da seguinte maneira:

1. O Email deve ser um email institucional, portanto deve conter como domínio "@senfio.com"! 
2. Para os emails institucionais da Senfio são exigidos nome e sobrenome separados por '.' antes do domínio. Então o email ficará desta forma: "nome.sobrenome@senfio.com".
3. A senha deve conter no mínimo 8 caracteres.

- ### Frontend(ReactJS)::

    Construa o frontend no framework [ReactJS](https://reactjs.org/docs/getting-started.html)

    1. O app deve exibir uma página de login e uma página Home.
    2. As credenciais devem ser um email e senha. :lock:
    3. Após receber as credenciais, o frontend deve enviar um JSON ao backend com as informações, e esperar o retorno sobre a validade das credenciais.
    4. Caso as credenciais não estejam corretas, exiba um alerta de credenciais inválidas! :x:
    5. Caso contrário, siga para a página Home. :white_check_mark:

    **O app deve rodar num container [Docker](https://docs.docker.com/get-started/).** :whale:

- ### Backend(Django + DRF)

    Construa o backend com framework [Django](https://docs.djangoproject.com/en/):snake:

    1. O app deve receber as credenciais do frontend, num JSON, e validar as informações.
    2. A camada de API deve ser feita com a lib [DRF-DjangoRestFramework](https://www.django-rest-framework.org/). 
    3. O email deve conter o domínio ‘@senfio.com’, nome e sobrenome do usuário.
    4. O backend retorna ao front a informação sobre a validade das credenciais!
    5. A criação de usuários deve ser feita através do Django Admin. 
    6. Banco de dados deve ser ou o padrão, sqlite3, ou o postgres através de um container também. 
    7. A infraestrutura de containers pode ser avulso ou no docker compose(recomendado).

    **O app também deve estar num container [Docker](https://docs.docker.com/get-started/).**:whale:




