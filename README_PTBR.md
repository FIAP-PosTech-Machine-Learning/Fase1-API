<table align="right">
 <tr><td><a href="README_PTBR.md"><img src="imgs/brazil.png" height="15"> Português</a></td></tr>
 <tr><td><a href="README.md"><img src="imgs/united-states.png" height="15"> Inglês</a></td></tr>
</table>

# **FIAP - Tech Challenge 1**

<br/>
<p align="center">
  <a href="https://www.fiap.com.br/"><img src="https://upload.wikimedia.org/wikipedia/commons/d/d4/Fiap-logo-novo.jpg" width="300" alt="FIAP"></a>
</p>
<br>

## **Tecnologias Utilizadas**

- **Python para o Back-End:** Python foi escolhido como a linguagem principal para o desenvolvimento do back-end devido à sua legibilidade, eficiência e ao extenso ecossistema de bibliotecas e frameworks que suportam o desenvolvimento rápido.

- **FastAPI para Desenvolvimento de API:** O FastAPI, um framework web moderno e de alto desempenho para construção de APIs, foi utilizado para desenvolver os serviços do back-end. Ele oferece suporte assíncrono, documentação interativa automática da API e alta velocidade, tornando-o ideal para criar APIs escaláveis e eficientes.

<br>

## **Como usar?**

Este projeto utiliza o FastAPI para o desenvolvimento do back-end. Siga os passos abaixo para configurar o ambiente e executar a aplicação.

### **Pré-requisitos**
Antes de executar a aplicação, certifique-se de ter os seguintes itens instalados:

- Python 3.12+
- pip (gerenciador de pacotes Python)
- FastAPI e dependências relacionadas
  
#### **01. Clone o repositório**

```bash
git clone https://github.com/FIAP-PosTech-Machine-Learning/Fase1-API.git
cd Fase1-API
```

#### **02. Configure o arquivo .env**
```bash
SECRET_KEY=<your_secret_key>
```

### **03. Crie o banco de dados através do Docker**
Use o Docker para implementar o banco através do comando do docker compose:
```bash
docker compose up -d
```

#### **04. Instale as dependências do Python**
Certifique-se de ter um ambiente virtual configurado para evitar conflitos de dependências. Em seguida, instale as dependências listadas em requirements.txt.
```bash
python -m venv venv        # Crie e ative o ambiente virtual
source venv/bin/activate   # Para Linux/Mac
venv\Scripts\activate      # Para Windows
```

```bash

pip install -r requirements.txt     # Instale as dependências
```

#### **05. Execute a aplicação FastAPI**
Após configurar o ambiente, você pode iniciar o servidor FastAPI:
```bash
fastapi dev main.py # para ambiente de desenvolvimento
```
ou
```bash
fastapi run main.py # para ambiente de produção
```

#### **06. Acesse a API**

- Abra seu navegador e navegue para http://127.0.0.1:8000/ para acessar a API.

O FastAPI gera automaticamente uma documentação interativa da API, que pode ser acessada em:
- Swagger UI: http://127.0.0.1:8000
- ReDoc: http://127.0.0.1:8000/redoc

#### **07. Testando a Aplicação**
Você pode usar o Swagger UI para testar os endpoints da API ou usar ferramentas como curl, Postman ou httpie para enviar requisições à API.

## Problemas Comuns
- **Dependências faltantes:** Se faltar alguma dependência, verifique o arquivo requirements.txt para garantir que tudo esteja instalado.
<br>

## **Desenvolvedores**

<table border="0" align="center">
  <tr>
  <td align="center">
      <img src="https://avatars.githubusercontent.com/u/71346377?v=4" width="160px" alt="Foto do Alexandre"/><br>
      <sub>
        <a href="https://www.github.com/alexandre-tvrs">@Alexandre Tavares</a>
      </sub>
    </td>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/160500127?v=4" width="160px" alt="Foto do Paulo"/><br>
      <sub>
        <a href="https://github.com/PauloMukai">@Paulo Mukai</a>
      </sub>
    </td>
    </td>
        <td align="center">
      <img src="https://avatars.githubusercontent.com/u/160500128?v=4" width="160px" alt="Foto da Vanessa"/><br>
      <sub>
        <a href="https://github.com/AnjosVanessa">@AnjosVanessa</a>
      </sub>
    </td>
    </td>
        <td align="center">
      <img src="https://avatars.githubusercontent.com/u/89281305?v=4" width="160px" alt="Foto da Vitor"/><br>
      <sub>
        <a href="https://github.com/vitorabreu29">@vitorabreu29</a>
      </sub>
    </td>
  </tr>
</table>
