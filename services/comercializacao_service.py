from utils import get_csv_data
from schemas import ComercializacaoSchema, AnoValorSchema


def convert_to_produtos(df):
    df.fillna('', inplace=True)
    anos = df.columns[3:].to_list()
    produtos = []
    for index, row in df.iterrows():
        id = index
        controle = row['control']
        nome = row['Produto']
        dados = []
        for ano in anos:
            valor = row[ano]
            dados.append(AnoValorSchema(ano=ano, valor=valor))
        produtos.append(ComercializacaoSchema(id=id, controle=controle, nome=nome, dados=dados))
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
    data = await get_comercializacao_data()
    for produto in data:
        if produto.id == id:
            return produto
    return None