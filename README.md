<table align="right">
 <tr><td><a href="README_PTBR.md"><img src="imgs/brazil.png" height="15"> Portuguese</a></td></tr>
 <tr><td><a href="README.md"><img src="imgs/united-states.png" height="15"> English</a></td></tr>
</table>

# **FIAP - Tech Challenge 1**

<br/>
<p align="center">
  <a href="https://www.fiap.com.br/"><img src="https://upload.wikimedia.org/wikipedia/commons/d/d4/Fiap-logo-novo.jpg" width="300" alt="FIAP"></a>
</p>
<br>

## **Technologies Used**

- **Python for the Back-End:** Python was chosen as the core programming language for the back-end development due to its readability, efficiency, and the extensive ecosystem of libraries and frameworks that support rapid development.

- **FastAPI for API Development:** FastAPI, a modern, high-performance web framework for building APIs, was used to develop the back-end services. It provides asynchronous support, automatic interactive API documentation, and high speed, making it optimal for creating scalable and efficient APIs.

<br>

## **How to use?**

This project uses a FastAPI for back-end development. Follow the steps below to configure the environment and run the application.

### **Pre-requisites**
Before running the application, ensure you have the following installed:

- Python 3.12+
- pip (Python package installer)
- FastAPI and related dependencies
- Docker

#### **01. Clone the repository**

```bash
git clone https://github.com/FIAP-PosTech-Machine-Learning/Fase1-API.git
cd Fase1-API
```

#### **02. Setup the .env file**
```bash
SECRET_KEY=<your_secret_key>
```

### **03. Setup the Database with Docker**
Use the docker compose to deploy the database with Docker.
```bash
docker compose up -d
```

#### **04. Install Python dependencies**
Make sure you have a virtual environment set up to avoid dependency conflicts. Then install the required dependencies from requirements.txt.
```bash
python -m venv venv        # Create and activate the virtual environment
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

```bash

pip install -r requirements.txt     # Install dependencies
```

#### **05. Run the FastAPI application**
Once the environment are set up, you can start the FastAPI server:
```bash
fastapi dev main.py # for development environment
```
or
```bash
fastapi run main.py # for production environment
```

#### **06. Access the API**

- Open your browser and navigate to http://127.0.0.1:8000/ to access the API.

FastAPI automatically generates interactive API documentation, which can be accessed at:
- Swagger UI: http://127.0.0.1:8000
- ReDoc: http://127.0.0.1:8000/redoc

#### **07. Testing the Application**
You can use the Swagger UI to test the API endpoints or use tools like curl, Postman, or httpie to send requests to the API.

## Common Issues
- **Missing dependencies:** If any dependencies are missing, check requirements.txt to ensure everything is installed.
<br>

## **Developers**

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
