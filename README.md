# API de consultas médicas - Desafio Lacrei

## 1. Sobre
<!--Adicionar descrição do projeto-->
Uma API com um CRUD de consultas médicas utilizando Python, Django e Django Rest Framework

## 2. Instalação da aplicação

* Create venv
    ```
    python -m venv venv
    ```
* Ativando o ambiente virtual
   
    Para ativar o ambiente virtual no Linux:
    ```
    source venv/bin/activate
    ```
    Para ativar o ambiente virtual no Windows:
    ```
    .\venv\Scripts\activate
    ```
  Após o comando inserido, deve aparecer o nome do ambiente virtual
* Install requirements
    ```
    pip install -r requirements.txt
    ```
* Run
    ```
    python manage.py runserver
    ```
* Testes
    ```
    python manage.py test consultas
    ```

## 3. Endpoints

### Profissional
#### GET lista de profissionais
##### Request
    `GET /profissionais`
        curl --location --request GET 'http://localhost:8000/consultas/profissionais'

##### Response
    Status: 200 OK
    Content-Type: application/json
    
    ```
    [
        {
            "id": 1,
            "nome": "Maria",
            "nome_social": "",
            "especialidade": "Ginecologista"
        }
    ]
    ```

#### GET profissional
##### Request
    `GET /profissionais/:id`
        curl --location --request GET 'http://localhost:8000/consultas/profissionais/:id'

##### Response
    Status: 200 OK
    Content-Type: application/json
    
    ```
    {
        "id": 1,
        "nome": "Maria",
        "nome_social": "",
        "especialidade": "Ginecologista"
    }
    ```

### POST profissional
##### Request
    `POST /profissionais`
        curl --location --request POST 'http://localhost:8000/consultas/profissionais'

    **Parametros**:
        
    ```
    {
        `nome`: string, obrigatório,
        `nome_social`: string, opcional,
        `especialidade`: string, obrigatório
    } 
    ```

##### Response
    Status: 201 CREATED
    Content-Type: application/json
    
    ```
    {
        "mensagem": "Profissional cadastrado com sucesso",
        "detalhes": {
            "id": 1,
            "nome": "Maria",
            "nome_social": "",
            "especialidade": "Ginecologia"
        }
    }   
    ```

### PUT profissional
##### Request
    `PUT /profissionais/:id`
        curl --location --request PUT 'http://localhost:8000/consultas/profissionais/:id'

    **Parametros**:
        
    ```
    {
        `nome`: string, obrigatório,
        `nome_social`: string, opcional,
        `especialidade`: string, obrigatório
    } 
    ```

##### Response
    Status: 200 OK
    Content-Type: application/json
    
    ```
    {
        "mensagem": "Profissional atualizado com sucesso",
        "detalhes": {
            "id": 1,
            "nome": "Maria",
            "nome_social": "",
            "especialidade": "Ginecologia"
        }
    }   
    ```

### DELETE profissional
##### Request
    `DELETE /profissionais/:id`
        curl --location --request DELETE 'http://localhost:8000/consultas/profissionais/:id'

##### Response
    Status: 200 OK
    Content-Type: application/json
    
    ```
    {
        "mensagem": "Profissional excluído com sucesso",
    }   
    ```

### Consulta

#### GET lista de consultas
##### Request
    `GET /consultas`
        curl --location --request GET 'http://localhost:8000/consultas'

##### Response
    Status: 200 OK
    Content-Type: application/json
    
    ```
    [
        {
            "id": 4,
            "paciente": "Maria",
            "nome_social": "",
            "profissional": 2,
            "data_consulta": "2023-06-19"
        }
    ]
    ```

#### GET lista de consultas por profissional
##### Request
    `GET /consultas/profissional/:id_profissional`
        curl --location --request GET 'http://localhost:8000/consultas/profissional/:id_profissional'

##### Response
    Status: 200 OK
    Content-Type: application/json
    
    ```
    [
        {
            "id": 4,
            "paciente": "Maria",
            "nome_social": "",
            "profissional": 2,
            "data_consulta": "2023-06-19"
        }
    ]
    ```


#### GET consulta
##### Request
    `GET /consultas/:id`
        curl --location --request GET 'http://localhost:8000/consultas/:id'

##### Response
    Status: 200 OK
    Content-Type: application/json
    
    ```
    {
        "id": 4,
        "paciente": "Maria",
        "nome_social": "",
        "profissional": 2,
        "data_consulta": "2023-06-19"
    }
    ```

### POST Consulta
##### Request
    `POST /consultas`
        curl --location --request POST 'http://localhost:8000/consultas'

    **Parametros**:
        
    ```
    {
        `paciente`: string, obrigatório,
        `nome_social`: string, opcional,,
        `data_consulta`: string, obrigatório, ex: "19-06-2022",
        `profissional`: number, obrigatório, ex: 1

    }
    ```

##### Response
    Status: 201 CREATED
    Content-Type: application/json
    
    ```
    {
        "mensagem": "Consulta cadastrada com sucesso",
        "detalhes": {
            "id": 1,
            "paciente": "Maria",
            "nome_social": "",
            "profissional": 3,
            "data_consulta": "2023-06-19"
        }
    }
    ```

### PUT consulta
##### Request
    `PUT /consultas/:id`
        curl --location --request PUT 'http://localhost:8000/consultas/:id'

    **Parametros**:
        
    ```
   ```
    {
        `paciente`: string, obrigatório,
        `nome_social`: string, opcional,,
        `data_consulta`: string, obrigatório, ex: "19-06-2022",
        `profissional`: number, obrigatório, ex: 1
    }
    ```

##### Response
    Status: 200 OK
    Content-Type: application/json
    
    ```
    {
        "mensagem": "Consulta atualizada com sucesso",
        "detalhes": {
            "id": 1,
            "paciente": "Maria",
            "nome_social": "",
            "profissional": 3,
            "data_consulta": "2023-06-19"
        }
    }
    ```

### DELETE consulta
##### Request
    `DELETE /consultas/:id`
        curl --location --request DELETE 'http://localhost:8000/consultas/consultas/:id'

##### Response
    Status: 200 OK
    Content-Type: application/json
    
    ```
    {
        "mensagem": "Consulta excluída com sucesso",
    }   
    ```