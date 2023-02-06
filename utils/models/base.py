from sqlalchemy import Column, BIGINT, select, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):

    id = Column(BIGINT, primary_key=True)

    engine = create_async_engine('postgresql+asyncpg://belhard:belhard@localhost:5432/ivibot')
    sync_engine = create_engine('postgresql://belhard:belhard@localhost:5432/ivibot')
    AsyncSession_ = async_sessionmaker(bind=engine)
    Session_ = sessionmaker(bind=sync_engine)

    @staticmethod
    def create_session(func):
        async def wrapper(*args, **kwargs):
            async with Base.AsyncSession_() as session:
                return await func(*args, **kwargs, session=session)

        return wrapper

    @create_session
    async def save(self, session: AsyncSession = None) -> None:
        session.add(self)
        await session.commit()
        await session.refresh(self)

    @classmethod
    @create_session
    async def get(cls, pk, session: AsyncSession = None):
        return await session.get(cls, pk)

    @create_session
    async def delete(self, session: AsyncSession = None):
        await session.delete(self)
        await session.commit()

    @classmethod
    @create_session
    async def all(
            cls,
            order_by: int = 'id',
            limit: int = None,
            offset: int = None,
            session: AsyncSession = None,
            **kwargs
    ):
        query = await session.scalars(
            select(cls)
            .filter_by(**kwargs)
            .limit(limit)
            .offset(offset)
            .order_by(order_by)
            .where()
        )
        return query.all()

    async def dict(self):
        data = self.__dict__
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data

    @classmethod
    @create_session
    async def scalars(cls, sql, session: AsyncSession):
        query = await session.scalars(sql)
        return query.all()
