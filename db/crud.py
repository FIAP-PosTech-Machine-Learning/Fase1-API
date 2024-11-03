from sqlalchemy.orm import Session
from db.models import Comercio, ComercioAno, ExpVinho, ExpVinhoAno, ImpVinhos, ImpVinhosAno, ProcessaViniferas, \
    ProcessaViniferasAno, Producao, ProducaoAno, User
from schemas import ComercializacaoSchema, ExportacaoSchema, ImportacaoSchema, ProcessamentoSchema, ProducaoSchema, \
    AnoValorSchema, TokenResponseSchema, UserSchema
from services.authentication_service import get_password_hash


def get_comercio(db: Session, comercio_id: int):
    return db.query(Comercio).filter(Comercio.id == comercio_id).first()


def create_comercio(db: Session, comercio: ComercializacaoSchema):
    db_comercio = Comercio(control=comercio.controle, produto=comercio.nome)
    db.add(db_comercio)
    db.commit()
    db.refresh(db_comercio)

    for ano_valor in comercio.dados:
        db_comercio_ano = ComercioAno(comercio_id=db_comercio.id, ano=ano_valor.ano, valor=ano_valor.valor)
        db.add(db_comercio_ano)

    db.commit()
    return db_comercio


def get_exp_vinho(db: Session, exp_vinho_id: int):
    return db.query(ExpVinho).filter(ExpVinho.id == exp_vinho_id).first()


def create_exp_vinho(db: Session, exp_vinho: ExportacaoSchema):
    db_exp_vinho = ExpVinho(pais=exp_vinho.pais)
    db.add(db_exp_vinho)
    db.commit()
    db.refresh(db_exp_vinho)

    for ano_valor in exp_vinho.dados:
        db_exp_vinho_ano = ExpVinhoAno(exp_vinho_id=db_exp_vinho.id, ano=ano_valor.ano, valor=ano_valor.valor)
        db.add(db_exp_vinho_ano)

    db.commit()
    return db_exp_vinho


def get_imp_vinho(db: Session, imp_vinho_id: int):
    return db.query(ImpVinhos).filter(ImpVinhos.id == imp_vinho_id).first()


def create_imp_vinho(db: Session, imp_vinho: ImportacaoSchema):
    db_imp_vinho = ImpVinhos(pais=imp_vinho.pais)
    db.add(db_imp_vinho)
    db.commit()
    db.refresh(db_imp_vinho)

    for ano_valor in imp_vinho.dados:
        db_imp_vinho_ano = ImpVinhosAno(imp_vinho_id=db_imp_vinho.id, ano=ano_valor.ano, valor=ano_valor.valor)
        db.add(db_imp_vinho_ano)

    db.commit()
    return db_imp_vinho


def get_processamento(db: Session, processamento_id: int):
    return db.query(ProcessaViniferas).filter(ProcessaViniferas.id == processamento_id).first()


def create_processamento(db: Session, processamento: ProcessamentoSchema):
    db_processamento = ProcessaViniferas(control=processamento.controle, cultivar=processamento.cultivar)
    db.add(db_processamento)
    db.commit()
    db.refresh(db_processamento)

    for ano_valor in processamento.dados:
        db_processamento_ano = ProcessaViniferasAno(processa_vinifera_id=db_processamento.id, ano=ano_valor.ano,
                                                    valor=ano_valor.valor)
        db.add(db_processamento_ano)

    db.commit()
    return db_processamento


def get_producao(db: Session, producao_id: int):
    return db.query(Producao).filter(Producao.id == producao_id).first()


def create_producao(db: Session, producao: ProducaoSchema):
    db_producao = Producao(control=producao.controle, produto=producao.nome)
    db.add(db_producao)
    db.commit()
    db.refresh(db_producao)

    for ano_valor in producao.dados:
        db_producao_ano = ProducaoAno(producao_id=db_producao.id, ano=ano_valor.ano, valor=ano_valor.valor)
        db.add(db_producao_ano)

    db.commit()
    return db_producao

def create_user(db: Session, data: UserSchema):
    db_user = User(email=data.email, password=get_password_hash(data.password), is_active=True)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()