from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://user:HqUnMkh93q2yUb1WWqJ1nhL0Iw75rZSn@dpg-cskjmad6l47c73bkobug-a.oregon-postgres.render.com/vitivinicultura'

engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
