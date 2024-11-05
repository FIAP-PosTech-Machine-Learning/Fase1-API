from utils import get_csv_data
from schemas import ComercializacaoSchema, AnoValorSchema
from db.database import engine
from sqlalchemy.orm import Session


def convert_to_produtos(df):
    df.fillna('', inplace=True)
    anos = df.columns[3:].to_list()
    produtos = []
    for index, row in df.iterrows():
        controle = row['control']
        nome = row['Produto']
        dados = []
        for ano in anos:
            valor = row[ano]
            dados.append(AnoValorSchema(ano=ano, valor=valor))
        produtos.append(ComercializacaoSchema(
            id=index, controle=controle, nome=nome, dados=dados))
    return produtos


async def get_comercializacao_data():
    try:
        data = await get_csv_data('http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv')
        data.to_csv('src/ProcessaViniferas.csv', index=False, encoding='utf-8')
        return convert_to_produtos(data)
    except:
        data = await get_csv_data('src/Comercio.csv')
        return convert_to_produtos(data)


async def get_comercializacao_by_id(id: int):
    produtos = await get_comercializacao_data()
    for produto in produtos:
        if produto.id == id:
            return produto
    return None


async def save_comercializacao_data():
    from db.crud import create_comercio
    async with Session(engine) as session:
        produtos = await get_comercializacao_data()
        for produto in produtos:
            create_comercio(session, produto)


async def load_comercializacao_data():
    pass  # implementar gravacao dos dados no banco de dados
