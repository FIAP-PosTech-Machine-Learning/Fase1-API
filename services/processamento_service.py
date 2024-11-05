from utils import get_csv_data
from schemas import ProcessamentoSchema, AnoValorSchema
from db.database import engine
from sqlalchemy.orm import Session


def convert_to_produtos(df):
    df.fillna('', inplace=True)
    anos = df.columns[3:].to_list()
    produtos = []
    for index, row in df.iterrows():
        controle = row['control']
        cultivar = row['cultivar']
        dados = []
        for ano in anos:
            valor = row[ano] if isinstance(row[ano], int) else 0
            dados.append(AnoValorSchema(ano=ano, valor=valor))
        produtos.append(ProcessamentoSchema(
            id=index, controle=controle, cultivar=cultivar, dados=dados))
    return produtos


async def get_processamento_data():
    try:
        data = await get_csv_data('http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv')
        data.to_csv('src/ProcessaViniferas.csv', index=False, encoding='utf-8')
        return convert_to_produtos(data)
    except:
        data = await get_csv_data('src/ProcessaViniferas.csv')
        return convert_to_produtos(data)


async def get_processamento_by_id(id: int):
    produtos = await get_processamento_data()
    for produto in produtos:
        if produto.id == id:
            return produto
    return None


async def save_processamento_data():
    from db.crud import create_processamento
    async with Session(engine) as session:
        produtos = await get_processamento_data()
        for produto in produtos:
            create_processamento(session, produto)
