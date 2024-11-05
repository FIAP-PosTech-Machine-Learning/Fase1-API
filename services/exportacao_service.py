from utils import get_csv_data
from schemas import ExportacaoSchema, AnoValorSchema
from db.database import engine
from sqlalchemy.orm import Session


def convert_to_produtos(df):
    df.fillna('', inplace=True)
    anos = []

    # Coleta os anos da coluna do DataFrame
    for col in df.columns[2:]:
        if col not in anos:
            anos.append(col)

    produtos = []
    for index, row in df.iterrows():
        pais = row['País']
        dados = []
        valor_dict = {}

        # Organiza os valores em um dicionário
        for i, ano in enumerate(row[2:]):
            valor_dict[anos[i // 2]] = ano

        for ano in anos:
            valor = valor_dict.get(ano, '')

            # Garantir que o ano seja um inteiro
            try:
                # Converte o ano para float e depois para int
                ano_inteiro = int(float(ano))
            except ValueError:
                ano_inteiro = 0  # ou trate o erro conforme necessário

            # Garantir que o valor seja um número, caso contrário, defina como 0
            if valor == '':
                valor_float = 0.0  # ou use None, dependendo do que faz mais sentido
            else:
                try:
                    valor_float = float(valor)
                except ValueError:
                    valor_float = 0.0  # ou trate o erro conforme necessário

            dados.append(AnoValorSchema(ano=ano_inteiro, valor=valor_float))

        produtos.append(ExportacaoSchema(id=index, pais=pais, dados=dados))

    return produtos


async def get_exportacao_data():
    try:
        data = await get_csv_data('http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv')
        data.to_csv('src/ProcessaViniferas.csv', index=False, encoding='utf-8')
        return convert_to_produtos(data)
    except:
        data = await get_csv_data('src/ExpVinho.csv')
        return convert_to_produtos(data)


async def get_exportacao_by_id(id: int):
    produtos = await get_exportacao_data()
    for produto in produtos:
        if produto.id == id:
            return produto
    return None


async def save_exportacao_data():
    from db.crud import create_exp_vinho
    async with Session(engine) as session:
        produtos = await get_exportacao_data()
        for produto in produtos:
            create_exp_vinho(session, produto)
