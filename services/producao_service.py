from utils import get_csv_data
from schemas import ProducaoSchema, AnoValorSchema


def convert_to_produtos(df):
    df.fillna('', inplace=True)
    anos = df.columns[3:].to_list()
    produtos = []
    for index, row in df.iterrows():
        id = index
        controle = row['control']
        nome = row['produto']
        dados = []
        for ano in anos:
            try:
                valor = int(row[ano])
            except:
                valor = None
            dados.append(AnoValorSchema(ano=ano, valor=valor))
        produtos.append(ProducaoSchema(id=id, controle=controle, nome=nome, dados=dados))
    return produtos
    
    
async def get_producao_data():
    try:
        data = await get_csv_data('http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv')
        data.to_csv('src/ProcessaViniferas.csv', index=False, encoding='utf-8')
        
        return convert_to_produtos(data)
    except:
        data = await get_csv_data('src/Producao.csv')
        return convert_to_produtos(data)
    
    
async def get_producao_by_id(id: int):
    data = await get_producao_data()
    for produto in data:
        if produto.id == id:
            return produto
    return None