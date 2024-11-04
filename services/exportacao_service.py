from utils import get_csv_data
from schemas import ExportacaoSchema, AnoValorSchema
from db.database import engine
from sqlalchemy.orm import Session


def convert_to_produtos(df):
    df.fillna('', inplace=True)
    anos = df.columns[3:].to_list()
    produtos = []
    for index, row in df.iterrows():
        pais = row['País']
        dados = []
        for ano in anos:
            valor = row[ano]
            dados.append(AnoValorSchema(ano=ano, valor=valor))
        produtos.append(ExportacaoSchema(index=index, pais=pais, dados=dados))
    return produtos


async def get_exportacao_data():
    try:
        data = await get_csv_data('http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv')
        data.to_csv('src/ProcessaViniferas.csv', index=False, encoding='utf-8')
        return convert_to_produtos(data)
    except:
        data = await get_csv_data('src/ExpVinho.csv')
        return convert_to_produtos(data)


async def save_exportacao_data():
    from db.crud import create_exp_vinho
    async with Session(engine) as session:
        produtos = await get_exportacao_data()
        for produto in produtos:
            create_exp_vinho(session, produto)
