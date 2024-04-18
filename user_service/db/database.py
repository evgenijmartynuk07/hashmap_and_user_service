from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from config import DB_HOST, DB_NAME, DB_PORT, DB_USER, DB_PASSWORD


Base = declarative_base()

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL
)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        return session


