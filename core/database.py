import os
import time

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

try:
    load_dotenv()
except ImportError:
    pass

engine = None
SessionLocal = None

Base = declarative_base()

def init_db():
    global engine, SessionLocal

    POSTGRES_URL = os.getenv("POSTGRES_URL")

    if not POSTGRES_URL:
        raise RuntimeError("❌ POSTGRES_URL não definida")

    if POSTGRES_URL.startswith("postgres://"):
        POSTGRES_URL = POSTGRES_URL.replace("postgres://", "postgresql://", 1)

    for i in range(10):
        try:
            print(f"⏳ Tentando conectar no banco... ({i+1}/10)")

            engine = create_engine(
                POSTGRES_URL,
                pool_pre_ping=True
            )

            with engine.connect():
                print("✅ Banco conectado!")

            SessionLocal = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=engine
            )

            return

        except Exception as e:
            print(f"❌ Erro ao conectar: {e}")
            time.sleep(2)

    raise RuntimeError("❌ Não conseguiu conectar ao banco após várias tentativas")

def get_db():
    if SessionLocal is None:
        raise RuntimeError("❌ Banco de dados não inicializado")

    return SessionLocal

def create_tables():
    if engine is None:
        raise RuntimeError("❌ Banco não inicializado")

    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    pass