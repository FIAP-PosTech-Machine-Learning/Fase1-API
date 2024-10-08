from utils import get_csv_data
from schemas import ImportacaoSchema, AnoValorSchema


def convert_to_produtos(df):
    df.fillna('', inplace=True)
    anos = df.columns[3:].to_list()
    produtos = []
    for index, row in df.iterrows():
        id = index
        pais = row['País']
        dados = []
        for ano in anos:
            valor = row[ano]
            dados.append(AnoValorSchema(ano=ano, valor=valor))
        produtos.append(ImportacaoSchema(id=id, pais=pais, dados=dados))
    return produtos
    
    
async def get_importacao_data():
    try:
        data = await get_csv_data('http://vitibrasil.cnpuv.embrapa.br/download/ImpVinho.csv')
        data.to_csv('src/ProcessaViniferas.csv', index=False, encoding='utf-8')
        
        return convert_to_produtos(data)
    except:
        data = await get_csv_data('src/ImpVinho.csv')
        return convert_to_produtos(data)
    
    
async def get_importacao_by_id(id: int):
    
    data = await get_importacao_data()
    for produto in data:
        if produto.id == id:
            return produto
    return None