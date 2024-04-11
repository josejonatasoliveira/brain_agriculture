**README.md**

# Brain Agriculture API

## Sumário

- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Docker](#docker)


## Requisitos

Certifique-se de ter o Python instalado com uma versão maior que 3.8. Você pode instalar os requisitos executando:

```bash
   pip install -r requirements.txt
```

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/josejonatasoliveira/brain_agriculture.git
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd brain_agriculture
   ```
3. Crie um ambiente virtual:
    ```bash
   python -m venv .env
   ```

    Ative o ambiente virtual

   ```bash
   .env\\Scripts\\activate.bat
   ```

4. Instale os requisitos:

   ```bash
   pip install -r requirements.txt
   ```

5. Migre as tabelas padrões do Django

   ```bash
   python manage.py migrate

6. Rodar
Após os passos anteriores esta na hora de rodar a api, para isso bastar executar o seguinte comando.
    ```bash
   python manage.py runserver 8040
   ```

##  Docker
Para instalar via docker basta executar o seguinte comando dentro da pasta `brain_agriculture`.

```bash
   docker-compose up --build
```

Após a execução destes comandos a api estará rodando na porta 8040 do localhost.
http://localhost:8040