import os
import importlib
from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from db import models
from db.database import engine

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="authentication")
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Tech Challenge 1',
    description='API desenvolvida para o desafio técnico 1 da pós graduação em Engenharia de Machine Learning na FIAP.',
    version='0.1',
)


# @app.on_event("startup")
# async def startup():
#    await comercializacao_service.load_comercializacao_data()


app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=[
        'localhost',
        '127.0.0.1',
    ]
)


@app.get('/', include_in_schema=False)
def redirect_to__docs():
    return RedirectResponse(url='/docs')


# Dynamically load and mount routers from the 'routers' folder
for file in os.listdir('routers'):
    if file != "__init__.py" and file.endswith(".py"):
        module_name = file[:-3]  # Remove '.py'
        module_path = f"routers.{module_name}"
        try:
            module = importlib.import_module(module_path)
            app.include_router(module.router)
        except ModuleNotFoundError as e:
            print(f"ModuleNotFoundError: {e}")
        except AttributeError as e:
            print(f"AttributeError: {e} in module {module_path}")
