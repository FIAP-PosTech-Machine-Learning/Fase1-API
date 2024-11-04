from utils import get_csv_data
from schemas import ImportacaoSchema, AnoValorSchema
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
        produtos.append(ImportacaoSchema(id=index, pais=pais, dados=dados))
    return produtos


async def get_importacao_data():
    try:
        data = await get_csv_data('http://vitibrasil.cnpuv.embrapa.br/download/ImpVinho.csv')
        data.to_csv('src/ProcessaViniferas.csv', index=False, encoding='utf-8')
        return convert_to_produtos(data)
    except:
        data = await get_csv_data('src/ImpVinho.csv')
        return convert_to_produtos(data)


async def save_importacao_data():
    from db.crud import create_imp_vinho
    async with Session(engine) as session:
        produtos = await get_importacao_data()
        for produto in produtos:
            create_imp_vinho(session, produto)
